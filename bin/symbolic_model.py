#%%
import sympy as sy
import math

class SymbolicModel:
    def __init__(self,eqs,pars=None):
        import simpy as sy
        self.eqs = eqs
        self.pars = None
        self._X = None
        self._F = None
        self._loadEqs(eqs)
        return None
        
    def _loadEqs(self,dict):
        """_summary_
        This function shuld initialize symbolic parameters
        for the functions
        """
        symbolic_vars = []
        symbolic_eqs = []
        for var in self.eqs.keys():
            exec(f"self.{var} = sy.sympify('{var}')")
            exec(f"symbolic_vars.append(self.{var})")
            exec(f"symbolic_eqs.append(sy.sympify(self.eqs['{var}']))")
        self._X = sy.Matrix(symbolic_vars)
        self._F = sy.Matrix(symbolic_eqs)

    def loadPars(self,pars):
        self.pars = pars.copy()
        
    def convertToExpr(self):
        for var,eq in self.eqs.items():
            _expr = sy.sympify(eq)
            self.expr[var]=_expr

    def evaluateParams(self):
        F_s = self._F.subs(self.pars)
        return F_s
    
    def getEqs(self):
        return None

    def _rk2(self):
        pass

    def simulate(self):
        return None
    
    def _lamdify(self,expr):
        return ()
    
    def saveExpressions():
        pass
    
    def getJacobian(self):
        return self._F.jacobian(self._X)

# %% lambdas for str substitution
phi_x = lambda x: f"exp(b_{x}*(v - v_{x})) - exp((b_{x} - 1)*(v - v_{x}))"
phi_u = phi_x('u')
phi_d = phi_x('d')
m_infty = "(1 + exp(g_m(v_m - v)))"
J_d = f"a_d*{m_infty}*(1-w)*({phi_d})" 
J_u = f"a_u*w*{phi_u}"
dtv = f"-{J_u} - {J_d}"
print(dtv)
#
alpha = "r_w*(exp(b_w*g_w*(v-v_w)))" 
beta =  "r_w*(exp((b_w-1)*g_w*(v-v_w)))"
dtw = f"(w**k)*({alpha}*(1-w) - {beta}*w)"
v_infty = f""
print(dtw)
#%%

eqs = {'v':dtv,
        'w':dtw
        }
pars = {'a_u': 1.0, 
        'a_d': 0.3, 
        'g_m':6, 
        'g_w':-4, 
        'v_w':0, 
        'v_m': -20,# falta normalizar V_T = 26.7 
        'b_w':0.6,
        'r_w':1,
        'k':0, #[0,1]
        'b_u':0.5,#[0,1]
        'b_d':0.5,#[0,1]
        'v_u':60,#duda
        'v_d':-90,#duda
        'g_m':0.5,#duda
        # 'v':'v_infty'
        }

#primera prueba sin sustituir parámetros.
#objetivo: obtener un jacobiano
sm = SymbolicModel(eqs)
sm.loadPars(pars)
sm.evaluateParams()
#%%
J = sm.getJacobian()
#%%
sm.loadEqs(dict)
sm.loadPars(pars)
sm.convertToExpr()
print(sm.eqs)
print(sm.pars)
print(sm.evaluateParams())
sm._J
# %%
import sympy as sy

expr = sy.sympify('x+y')
expr.subs({'x':3})
# %%
sy.sympify(dtv)

# %%

#meter parámetros
#sacar tripletas
#lambdificaciones para obtener fuciones numéricas
# y = exp(b) luego y^c = exp(cb)

#valores propios
#buscar que sea sobre funciones de numpy
#quiver, ceroclinas, puntos fijos trayectoiras
#en funcion de un conjunta 

