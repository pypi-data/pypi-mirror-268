# Class to find the optimal points of each of the conected components, and the constrains using the Mahalanobis distance

# *******************************************************
# Import libraries

import numpy as np
import sympy as sp
from scipy.optimize import minimize

# *******************************************************

def Querry(x, x_matrix, n_elements, bounds, dims, af_params, constraints_method, sense, model, models_const, Acq_fun):

    # Acquisition function for the optimization
    def Acquisition_function_opt(x, af_params, sense, model, models_const):

        if sense == "maximize":
            af_opt = -Acq_fun(x.reshape(1,-1), af_params, constraints_method, model, models_const)
        elif sense == "minimize":
            af_opt = Acq_fun(x.reshape(1,-1), af_params, constraints_method, model, models_const)
        
        return af_opt

    def Mahalanobis_distance(matrix, n_elements):

        mu = [np.mean(matrix[i], axis=0).reshape(-1, 1) for i in range(n_elements)]
        P = []
        chi = []
        Sigma = []

        if dims == 1:
            for i in range(n_elements):
                var = np.var(matrix[i]/np.sqrt(len(matrix[i])), axis=0)
                if var == 0:
                    Sigma.append(1e-6)
                    P.append(1/(1e-6))
                    chi.append(1.4)
                else:
                    Sigma.append(var)
                    var_inv = 1/var
                    P.append(var_inv)
                    y = matrix[i] - mu[i]
                    dist = [(y[j]*np.sqrt(var_inv)) for j in range(len(y))]
                    chi.append(np.percentile(dist, 95))
        else:                
            for i in range(n_elements):
                if (len(matrix[i]) < 3):
                    cov = np.eye(dims)
                    Sigma.append(cov)
                    P.append(cov)
                    chi.append(1.4)
                else:
                    # Covariance matrix
                    cov = np.cov(matrix[i].T)
                    # Check if the covariance matrix is singular, if so, add a small value to the diagonal
                    if np.linalg.det(cov) == 0:
                        cov = cov + 1e-6*np.eye(dims)
                        # Inverse of the covariance matrix
                    cov_inv = np.linalg.inv(cov)
                    y = matrix[i]-mu[i].T
                    dist = [np.sqrt(y[j].T@cov_inv@y[j]) for j in range(len(y))]
                    Sigma.append(cov_inv)
                    P.append(cov)
                    chi.append(np.percentile(dist, 95))

        return mu, Sigma, P, chi

    def Constrains(x, n_elements, mu, P, chi):

        const = []

        for i in range(n_elements):
            y = (x-mu[i])
            dist = y.T*P[i]*y
            const.append(sp.LessThan(dist[0], chi[i]))
            
        const_lamb = [sp.lambdify(x, (const[i].rhs - const[i].lhs), 'numpy') for i in range(n_elements)]
        # lambda function for the constrains
        def Constraint_lambify(fun):

            lam = lambda x: fun(*x)
            return lam

        constraints = [Constraint_lambify(const_lamb[i]) for i in range(n_elements)]
        
        return constraints
    
    # Main program
    # Check if the initial database is empty
    if x_matrix is None:
        raise ValueError('Initial database is empty')
    # Compute the confidence region
    mu, Sigma, P, chi = Mahalanobis_distance(x_matrix, n_elements)
    # Define the constrains
    constraints = Constrains(x, n_elements, mu, Sigma, chi)
    # Define the optimization problem
    x_opt = []
    for i in range(n_elements):
        res = minimize(Acquisition_function_opt, x0=mu[i], args=(af_params, sense, model, models_const), method='SLSQP', bounds=bounds, constraints={'type': 'ineq', 'fun': constraints[i]})
        x_opt.append(res.x)        

    return x_opt