from expression import Expression
from fonctions import Exp, Sin
from operations import Multiplication
from polynome import Polynome
import matplotlib.pyplot as plt

def afficher_resultat(nom: str, expr: Expression, x_test: float = 2.0) -> None:
	derivee = expr.deriver()
	print(f"\n--- {nom} ---")
	print(f"f(x)   = {expr}")
	print(f"f'(x)  = {derivee}")
	print(f"f({x_test:g})  = {expr.evaluer(x_test):.6f}")
	print(f"f'({x_test:g}) = {derivee.evaluer(x_test):.6f}")


def tracer_comparaison(expr: Expression, a: float, b: float, n: int = 300) -> None:
	
	derivee = expr.deriver()
	pas = (b - a) / (n - 1)
	xs = [a + i * pas for i in range(n)]
	ys_expr = [expr.evaluer(x) for x in xs]
	ys_derivee = [derivee.evaluer(x) for x in xs]

	plt.figure(figsize=(10, 5))
	plt.plot(xs, ys_expr, label=f"f(x) = {expr}")
	plt.plot(xs, ys_derivee, label=f"f'(x) = {derivee}")
	plt.title("Comparaison entre une expression et sa dérivée")
	plt.xlabel("x")
	plt.ylabel("y")
	plt.grid(True, alpha=0.3)
	plt.legend()
	plt.tight_layout()
	plt.show()


def main() -> None:
	# Variable symbolique x representee par le polynome x.
	x = Polynome([0, 1])

	f = Polynome([1, 2, 3])  # 3x^2 + 2x + 1
	g = Sin(x)  # sin(x)
	h = Exp(Polynome([1, 2]))  # exp(2x + 1)
	p = Multiplication(Polynome([1, 0, 1]), Sin(x))  # (x^2 + 1) * sin(x)

	afficher_resultat("Polynome f", f, x_test=2.0)
	afficher_resultat("Sinus g", g, x_test=0.0)
	afficher_resultat("Exponentielle h", h, x_test=1.0)
	afficher_resultat("Produit p", p, x_test=1.0)

	print("\nGraphique pour p(x) et p'(x)...")
	tracer_comparaison(p, -5, 5)


if __name__ == "__main__":
	main()
