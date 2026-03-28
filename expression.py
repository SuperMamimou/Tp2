from abc import ABC, abstractmethod


class Expression(ABC):
    """Base commune pour toutes les expressions symboliques."""

    @abstractmethod
    def evaluer(self, x: float) -> float:
        """Retourne la valeur numerique de l'expression pour x."""

    @abstractmethod
    def deriver(self) -> "Expression":
        """Retourne l'expression symbolique de la derivee."""

    @abstractmethod
    def __str__(self) -> str:
        """Retourne une representation lisible de l'expression."""
