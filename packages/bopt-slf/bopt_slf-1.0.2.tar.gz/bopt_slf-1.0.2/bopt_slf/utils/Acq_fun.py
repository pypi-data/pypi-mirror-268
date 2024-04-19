import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler

# *******************************************************

def UCB(x, xi, model):
    # Predict the model
    mean, std = model.predict(x)
    af = mean + xi*std
    
    return af

# *******************************************************

def PI(x, x_best, xi, model):

    mean, std = model.predict(x)
    with np.errstate(divide='warn'):
        imp = mean - x_best - xi
        Z = imp / std
        sld = StandardScaler().fit_transform(Z)
        af = norm.cdf(sld)
        af[std == 0.0] = 0.0

    return af

# *******************************************************

def EI(x, x_best, xi, model):
    
    mean, std = model.predict(x)
    with np.errstate(divide='warn'):
        imp = mean - x_best - xi
        Z = imp / std
        sld = StandardScaler().fit_transform(Z)
        af = imp * norm.cdf(sld) + std * norm.pdf(sld)
        af[std == 0.0] = 0.0
    
    return af

# *******************************************************

def PoF(x, models):
    
    pof = []

    for model in models:
        mean, std = model.predict(x)
        std[(std < 1e-100) & (std > 0)] = 1e-99
        Z = -mean/std
        sld = StandardScaler().fit_transform(Z)
        pof.append(norm.cdf(sld))

    return np.prod(np.array(pof), axis=0)

# *******************************************************

def Prob_GPC(x, model):

    gpc, _ = model.predict(x)

    return gpc

# *******************************************************

def AF(x, params, constraints_method, model, models_const):

    xi, _, x_best, AF_name = params.values()

    if AF_name == 'UCB':
        score = UCB(x, xi, model)
    elif AF_name == 'PI':
        score = PI(x, xi, x_best, model)
    elif AF_name == 'EI':
        score = EI(x, xi, x_best, model)
    else:
        pass

    if models_const is None:
        pass
    else:
        if constraints_method == "PoF":
            score_const = PoF(x, models_const)
        elif constraints_method == "GPC":
            score_const = Prob_GPC(x, models_const)
        else:
            pass
        score = score.reshape(-1,1)
        score_const = score_const.reshape(-1,1)
        score = score*score_const

    return score
