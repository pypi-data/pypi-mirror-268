import numpy as np
import sympy as sp
import multiprocess as mp
import GPy
import warnings
from ..utils.Initialize import Space, Problem_type, Get_constraints, Times_fun, Points_initial_design, x_Generator, Bounds, Points_mesh, AF_params
from ..utils.Dimension_reduction import Reduce, Inverse, Train_reducer, Train_inverter, Find_reducer, Find_inverter, Red_bounds
from ..utils.Models import Select_model, Train_model, Train_models_const, Kernel_discovery
from ..utils.Acq_fun import AF
from ..utils.Set_level_filtration import Slf
from ..utils.Querry_points import Querry
from ..utils.Update import Up_mesh
from ..utils.Aux import Errors, Data_eval, Eval_fun, Eval_const, Regret, Print_results, Create_results

class BO():

    def __init__(self, function, domain, sense,
                 surrogate = "GP",
                 acquisition_function = "UCB",
                 xi = 2,
                 xi_decay = "yes",
                 kernel = None,
                 kern_discovery = "yes",
                 kern_discovery_evals = 2,
                 x_0 = None, 
                 z_0 = None,
                 design = "LHS",
                 p_design = None,
                 parallelization = "no",
                 max_iter = 100, 
                 n_restarts = 5,
                 constraints = None,
                 constraints_method = "PoF",
                 reducer = None,
                 n_components = None,
                 inverter_transform = "No",
                 verbose = 0,
                 ):

        self.function = function
        self.domain = domain
        self.constraints = constraints
        self.x_0 = x_0
        self.z_0 = z_0
        self.sense = sense
        self.surrogate = surrogate
        self.acquisition_function = acquisition_function
        self.kernel = kernel
        self.parallelization = parallelization
        self.kern_discovery = kern_discovery
        self.design = design
        self.p_design = p_design
        self.max_iter = max_iter
        self.n_restarts = n_restarts
        self.kern_discovery_evals = kern_discovery_evals
        self.xi = xi
        self.xi_decay = xi_decay
        self.constraints_method = constraints_method
        self.reducer = reducer
        self.n_components = n_components
        self.inverter_transform = inverter_transform
        self.verbose = verbose

    def optimize(self):

        # *************** Main program ********************
        # Ignore warnings
        warnings.filterwarnings("ignore")
        #sys.setrecursionlimit(10000)
        #
        dims, n_x, n_d, n_c, n_y, x_l, x_u, y_v, dis_val, cat_val, enc_cat, names = Space(self.domain)
        Errors(n_x, n_y, self.design, self.surrogate, self.constraints_method, self.acquisition_function)
        problem_type = Problem_type(n_x, n_y)
        # 
        if self.constraints is None:
            const, n_const = None, None
        else:
            const, n_const = Get_constraints(self.constraints, self.constraints_method)
        # If an initial database in not provided, create using the design of experiments
        if self.x_0 is None:
            # Evaluate an arbitrary point to determine the computation time of the function
            x_trial = x_Generator(x_l, x_u, y_v, n_x, n_y, dims, 1, problem_type, "random")
            x_eval = Data_eval(x_trial, n_c, dims, enc_cat)
            times, z_trial = Times_fun(self.function, x_eval)
            if self.p_design == None:
                self.p_design = Points_initial_design(times, dims, self.design)
            self.x_0 = x_Generator(x_l, x_u, y_v, n_x, n_y, dims, self.p_design, problem_type, self.design)
            x_eval = Data_eval(self.x_0, n_c, dims, enc_cat)
            self.z_0 = self.function(x_eval).reshape(-1,1)
            x, z = np.vstack((self.x_0, x_trial)), np.vstack((self.z_0, z_trial))
        else:
            x = self.x_0
            if self.z_0 is None:
                x_eval = Data_eval(self.x_0, n_c, dims, enc_cat)
                z = self.function(x_eval).reshape(-1,1)
            else:
                self.p_design = len(self.z_0)
                z = self.z_0
        # Generate mesh, or grid
        p_mesh = Points_mesh(dims)
        if p_mesh > 3: 
            mesh = x_Generator(x_l, x_u, y_v, n_x, n_y, dims, p_mesh, problem_type, "Mesh")
        else:
            mesh = x_Generator(x_l, x_u, y_v, n_x, n_y, dims, 1024, problem_type, "Sobol")
        # Find reducer and perform dimensionality reduction
        if self.reducer is None:
            if (problem_type == "Continuous") and (n_x < 5):
                self.reducer = "No"
                reducer_trained = None
                dims_red = dims
                x_red = x
            else:
                self.reducer, reducer_trained, dims_red = Find_reducer(x, n_x, dims, self.n_components, problem_type)
                x_red = Reduce(x, n_x, dims, problem_type, reducer_trained)
        elif self.reducer == "No":
            reducer_trained = None
            dims_red = dims
            x_red = x
        else:
            dims_red = self.n_components
            x_red, reducer_trained = Train_reducer(x, n_x, dims, problem_type, dims_red, self.reducer)
        # Reduce bounds
        x_l_red, x_u_red = Red_bounds(mesh, x_l, x_u, n_x, dims, dims_red, problem_type, reducer_trained)
        # Find inverter
        if self.inverter_transform == "Yes":
            if self.reducer.__module__ == 'prince.mca' or self.reducer.__module__ == 'prince.famd':
                raise ValueError("Reducer module has no inverse_transform")
            else:
                inverter = reducer_trained
        elif self.inverter_transform == "No":
            if self.reducer == "No":
                inverter = None
            else:
                inverter = Find_inverter(x, x_red, n_x, n_y, dims, problem_type)
                inverter = Train_inverter(x, x_red, dims, inverter)
        else:
            pass
        # Generate mesh in the reduced space
        p_mesh_red = Points_mesh(dims_red)
        mesh_red = x_Generator(x_l_red, x_u_red, 0, 0, 0, dims_red, p_mesh_red, "Continuous", "Mesh")
        p_mesh_0 = p_mesh_red
        p_mesh_red, mesh_red = [p_mesh_red], [mesh_red]
        # Tuple of the bounds
        bounds = Bounds(x_l_red, x_u_red, dims_red)
        # Spawning processes
        if self.parallelization == "yes":
            jobs = mp.cpu_count()
        else:
            jobs = 1
        # Select covariance
        if self.kern_discovery == "yes":
            model = Kernel_discovery(x_red, z, dims_red, self.surrogate, self.kern_discovery_evals)
            kernel = model.kern
        elif self.kern_discovery == "no" and self.kernel is None:
            kernel = GPy.kern.RBF(input_dim=dims_red, variance=1.0, lengthscale=1.0)
        else:
            kernel = self.kernel
        # Eval and train constraints
        if self.constraints is None:
            models_const = None
        else:
            g_hat = Eval_const(x, const, n_const, self.constraints_method)
            models_const = Train_models_const(x, g_hat, n_const, self.constraints_method)
        # Initialize parameters of acquisition function
        af_params = AF_params(z, self.xi, self.xi_decay, self.max_iter, self.acquisition_function, self.sense)
        #
        x_symb = sp.Matrix(sp.symbols('x:' + str(dims_red)))
        x_symb_names = sp.Matrix(sp.symbols('x:' + str(dims)))
        q0 = 25
        qf = 75
        delta_q = (qf-q0)/self.max_iter
        q_inc = q0
        q = q0
        flag = 0
        rt = []
        #
        if self.sense == "maximize":
            ix_best = np.argmax(z)
            z_best = np.max(z)
        elif self.sense == "minimize":
            ix_best = np.argmin(z)
            z_best = np.min(z)
        x_best = x[ix_best]
        af_params["f_best"] = z_best
        # Print results if vervose is active
        if self.verbose == 1:
            if names is None:
                header = 'ite  ' +  '  f      ' + str(x_symb_names[0])
            else:
                header = 'ite  ' +  '  f      ' + str(names[0])
            for i in range(1, dims):
                if names is None:
                    header += '      ' + str(x_symb_names[i])
                else:
                    header += '      ' + str(names[i])
            print(header)
            x_best_eval = Data_eval(x_best.reshape(1,-1), n_c, dims, enc_cat)
            x_print = Print_results(x_best_eval, enc_cat)
            z_print = "%.5f" % z_best if 1e-3 < abs(z_best) < 1e3 else "%0.1e" % z_best
            print(0, ' ', z_print, *x_print)
        # Cycle
        for ite in range(1, self.max_iter+1):
            model = Select_model(x_red, z, kernel, self.surrogate)
            # Train model
            model = Train_model(model, self.n_restarts)
            if self.constraints is None:
                models_const = None
            else:
                x_eval = Data_eval(x, n_c, dims, enc_cat)
                g_hat = Eval_const(x_eval, const, n_const, self.constraints_method)
                models_const = Train_models_const(x_red, g_hat, n_const, self.constraints_method)
            # Find conected elements
            connected_elements, n_elements = Slf(mesh_red, p_mesh_red, dims_red, q, jobs, af_params, self.constraints_method, self.sense, model, models_const, AF)
            # Querry point
            x_red_new = Querry(x_symb, connected_elements, n_elements, bounds, dims_red, af_params, self.constraints_method, self.sense, model, models_const, AF)
            #
            if self.reducer == "No":
                x_new = x_red_new
            else:
                x_new = Inverse(x_red_new, self.inverter_transform, inverter)
            #
            x_eval = Data_eval(x_new, n_c, dims, enc_cat)
            z_new = Eval_fun(x_eval, n_elements, self.parallelization, jobs, self.function)
            #
            if jobs == 1:
                z_new_best = z_new
            else:
                if self.sense == "maximize":
                    z_new_best = np.max(z_new)
                elif self.sense == "minimize":
                    z_new_best = np.min(z_new)
                else:
                    pass
            # Update train data
            x, z = np.vstack((x, x_new)), np.vstack((z, z_new))
            if self.reducer == "No":
                x_red = np.vstack((x_red, x_red_new))
            else:
                x_red, reducer_trained = Train_reducer(x, n_x, dims, problem_type, dims_red, self.reducer)
                if self.inverter_transform == "No":
                    inverter = Train_inverter(x, x_red, dims, inverter)
                elif self.inverter_transform == "Yes":
                    inverter = reducer_trained
                else:
                    pass
            # 
            if self.sense == "maximize":
                if z_new_best > z_best:
                    flag = 1
            elif self.sense == "minimize":
                if z_new_best < z_best:
                    flag = 1
            # Update parameters
            if flag == 1:
                if self.reducer != "No":
                    connected_elements_inv = [Inverse(connected_elements[i], self.inverter_transform, inverter) for i in range(n_elements)]
                    connected_elements = [Reduce(connected_elements_inv[i], n_x, dims, problem_type, reducer_trained) for i in range(n_elements)]
                mesh_red, p_mesh_red = Up_mesh(connected_elements, n_elements, p_mesh_0, dims_red)
                af_params["xi"] *= af_params["xi_decay"]
                q_inc += delta_q
                q = int(round(q_inc/5.0)*5.0)
            rt.append(Regret(z_new, np.array(x_red_new), n_elements, model))
            # Print results
            if self.sense == "maximize":
                ix_best = np.argmax(z)
                z_best = np.max(z)
            elif self.sense == "minimize":
                ix_best = np.argmin(z)
                z_best = np.min(z)
            x_best = x[ix_best]
            af_params["f_best"] = z_best
            flag = 0
            if self.verbose == 1:
                x_best_eval = Data_eval(x_best.reshape(1,-1), n_c, dims, enc_cat)
                x_print = Print_results(x_best_eval, enc_cat)
                z_print = "%.5f" % z_best if 1e-3 < abs(z_best) < 1e3 else "%0.1e" % z_best
                print(ite, ' ', z_print, *x_print)

        res = Create_results(x_best, z_best, x, z, x_l, x_u, dims, self.max_iter, self.p_design, self.design, af_params, self.constraints_method, rt, models_const, model)

        return res