from sympy import oo, symbols, integrate, Piecewise, Max, Min, And, Expr, refine, Q
from sympy.stats import density, Beta
from copy import copy


class BoundedDist:
    def __init__(self, var = None, lwr=0, upr=1):
        if var is None:
            var = symbols("x", real=True)
        self.var = var

        if not isinstance(lwr, Expr) and not isinstance(upr, Expr):
            if not lwr < upr:
                raise Exception(f"{lwr} >= {upr}. Parameter lwr must be less than upr.")

    def set_var(self, var):
        self.pdf = self.pdf.subs(self.var, var)
        self.var = var

    def reflected(self):
        reflected_dist = copy(self)
        reflected_dist.pdf = reflected_dist.pdf.subs(self.var, -self.var)
        return reflected_dist

    def __str__(self):
        return str(self.pdf)

    def __repr__(self):
        return repr(self.pdf)

class UniformBD(BoundedDist):
    def __init__(self, lwr=0, upr=1, var = None):
        super().__init__(var, lwr, upr)

        self.pdf = Piecewise(
            (1/(upr-lwr), And(self.var>=lwr, self.var<=upr)),
            (0, True)
        )

class BetaBD(BoundedDist):
    def __init__(self, a, b, lwr=0, upr=1, var = None):
        lwr, upr = 0, 1
        super().__init__(var, lwr, upr)

        self.pdf = Piecewise(
            (density(Beta("x", a, b))(self.var), And(self.var>=lwr, self.var<=upr)),
            (0, True)
        )

def conv_dists(dist1, dist2, var):
    tau = symbols('tau', real=True)
    pdf = integrate(dist1.pdf.subs(var, tau) * dist2.pdf.subs(var, var - tau), (tau, -oo, +oo))
    return pdf

def diff_dists(dist1, dist2, var):
    return conv_dists(dist1, dist2.reflected(), var)

def calculate_prob(k_dist, c1_dist, c2_dist):

    y = symbols("y", real=True)
    x = symbols("x", real=True)

    c1_dist = c1_dist(var=y)
    ky_dist = k_dist(var=y)

    y_expr = diff_dists(c1_dist, ky_dist, y)

    n, o = Max(y, 0), Min(1, 1+y)

    c2_dist = c2_dist(var=x)
    kx_dist = k_dist(var=x, lwr=n, upr=o)

    x_expr = diff_dists(c2_dist, kx_dist, x)

    a = 0 - o
    d = 1 - n

    return 2*integrate(y_expr*refine(x_expr, Q.negative(y)), (x, a, Min(d, 0)), (y, -1, 0)).evalf()
