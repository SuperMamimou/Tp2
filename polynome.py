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
    