from expression import Expression

class Polynome(Expression):
    """Polynome represente par une liste de coefficients [a0, a1, a2, ...]."""
    def __init__(self, expression: Expression):
        self.expression = expression
    
    def evaluer(self, x: float) -> float:
        total = 0
        for i in range(0, len(self.expression), 1):
            total += self.expression[i] * x ** i
        return total
    
    def deriver(self) -> "Expression":
        list_derivee = []
        for i in range(1, len(self.expression), 1): # on skip l'index zero car f'(n) = 0
            if i == 1:
                list_derivee.append(self.expression[1])
            else:
                list_derivee.append(self.expression[i]*i)
        return Polynome(list_derivee)
    
    def __str__(self) -> str:
        return f"{list(self.expression)}"
    

def Addition_de_Polynome(exp1: Polynome, exp2: Polynome) -> Polynome:
    """Prend comme argument deux Polynomes et retourne l'addtion des deux Polynomes"""
    if len(exp1.expression) >= len(exp2.expression):
        for i in range(0, len(exp2.expression), 1):
            exp1.expression[i] = exp1.expression[i] + exp2.expression[i]
        return Polynome(exp1.expression)
    else:
        for i in range(0, len(exp1.expression), 1):
            exp2.expression[i] = exp1.expression[i] + exp2.expression[i]
        return Polynome(exp2.expression)
    
def Multiplication_de_Polynome(exp1:Polynome, exp2:Polynome) -> Polynome:
    """Prend comme argument deux Polynomes et retourne la multiplication des deux Polynomes"""
    Mult = []
    for i in range(0, len(exp1.expression)+len(exp2.expression)-1, 1):
        Mult.append(0)
    
    for i in range(0, len(exp1.expression), 1):
        for j in range(0, len(exp2.expression), 1):
            Mult[j+i] = exp1.expression[i] * exp2.expression[j] + Mult[j+i]
    return Polynome(Mult)