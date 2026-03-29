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
        return Addition_de_Polynome(deriver_exp1, deriver_exp2)
    
    def __str__(self):
        return f"{self.exp1} + {self.exp2}"


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
        return Addition(
            Multiplication(deriver_exp1, self.exp2),
            Multiplication(self.exp1, deriver_exp2)
        )
    def __str__(self):
        return f"{self.exp1} * {self.exp2}"
