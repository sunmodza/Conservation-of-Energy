from sympy import Eq,solve,symbols
celcius,roamer,fahrenheit,kelvin = symbols("celcius roamer fahrenheit kelvin")
def unitconverter(s,d,v):
        equation={'c':[celcius/100,celcius],
                'r':[roamer/80,roamer],
                'k':[(kelvin-273)/100,kelvin],
                'f':[(fahrenheit-32)/180,fahrenheit]}
        return(solve(Eq(equation[s][0],equation[d][0]).subs({equation[s][1]:v}),equation[d][1]))