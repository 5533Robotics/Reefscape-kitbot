def linear_remap(x, si, ei, sf, ef):
    slope = (sf - ef) / (si - ei)
    y_intercept = sf - (si * slope)
    return slope * x + y_intercept