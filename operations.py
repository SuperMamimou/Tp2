from expression import Expression
from polynome import Polynome, Addition_de_Polynome, Multiplication_de_Polynome

class Addition(Expression):
    """Expression representant u + v."""
    def __init__(self, exp1: Expression, exp2: Expression):
        self.exp1 = exp1
        self.exp2 = exp2

    def evaluer(self, x:float) -> float:
        return self.exp1.evaluer(x) + self.exp2.evaluer(x)
    
    def deriver(self) -> Expression:
        deriver_exp1: Expression = self.exp1.deriver()
        deriver_exp2: Expression = self.exp2.deriver()
        return Addition_de_Polynome(deriver_exp1.expression, deriver_exp2.expression)
    
    def __str__(self):
        return f"{list(self.exp1.expression)} + {list(self.exp2.expression)}"


class Multiplication(Expression):
    """Expression representant u * v."""
    def __init__(self, exp1: Expression, exp2: Expression):
        self.exp1 = exp1
        self.exp2 = exp2

    def evaluer(self, x:float) -> float:
        return self.exp1.evaluer(x) * self.exp2.evaluer(x)

    def deriver(self) -> Expression:
        deriver_exp1: Expression = self.exp1.deriver()
        deriver_exp2: Expression = self.exp2.deriver()
        return Addition_de_Polynome(
                Multiplication_de_Polynome(deriver_exp1, self.exp2),
                Multiplication_de_Polynome(deriver_exp2, self.exp1)
            )
        


    def __str__(self):
        return f"{list(self.exp1.expression)} * {list(self.exp2.expression)}"
    

exp1 = Polynome([2,1,3])
exp2 = Polynome([1,6,1,9])

print(Multiplication(exp1, exp2).deriver())
