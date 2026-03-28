from expression import Expression
from polynome import Polynome

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
        highest_degree: bool = len(deriver_exp1.expression) >= len(deriver_exp2.expression)
        #Égaliser les deux derivée
        if highest_degree:
            for i in range(0, len(deriver_exp1.expression), 1):
                if i in range(0, len(deriver_exp2.expression),1):
                    pass
                else:
                    deriver_exp2.expression.append(0)
        else:
            for i in range(0, len(deriver_exp2.expression), 1):
                if i in range(0, len(deriver_exp1.expression),1):
                    pass
                else:
                    deriver_exp1.expression.append(0)
        #On additionne les termes du même degrée
        for i in range(0, len(deriver_exp1.expression), 1):
            deriver_exp1.expression[i] = deriver_exp1.expression[i] + deriver_exp2.expression[i]
        
        return Polynome(deriver_exp1.expression)
    
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
        

    def __str__(self):
        return f"{list(self.exp1.expression)} * {list(self.exp2.expression)}"
    

exp1 = Polynome([2,1,3])
exp2 = Polynome([1,6,1,9])

print(Addition(exp1, exp2))
