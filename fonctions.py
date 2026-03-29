from expression import Expression
from polynome import Multiplication_de_Polynome
from operations import Multiplication
import math

class Sin(Expression):
    """Expression representant sin(u)."""
    def __init__(self, exp: Expression):
        self.expression = exp
    
    def evaluer(self, x: float) -> float:
        return math.sin(self.expression.evaluer(x))
    
    def deriver(self):
        return Multiplication(
            Cos(self.expression),
            self.expression.deriver()
        )

    def __str__(self):
        return f"Sin({list(self.expression.expression)})"
    


class Cos(Expression):
    """Expression representant cos(u)."""
    def __init__(self, exp: Expression):
        self.expression = exp
    
    def evaluer(self, x: float) -> float:
        return math.cos(self.expression.evaluer(x))
    
    def deriver(self):
        return Multiplication(
            Multiplication(
                Sin(self.expression),
                -1
            ),
            self.expression.deriver()
        )

    def __str__(self):
        return f"Cos({list(self.expression.expression)})"


class Exp(Expression):
    """Expression representant exp(u)."""
    def __init__(self, exp: Expression):
        self.expression = exp
    
    def evaluer(self, x: float) -> float:
        return math.e ** self.expression.evaluer(x)
    
    def deriver(self):
        return Multiplication(
            Exp(self.expression),
            self.expression.deriver()
        )

    def __str__(self):
        return f"e^{list(self.expression.expression)}"
