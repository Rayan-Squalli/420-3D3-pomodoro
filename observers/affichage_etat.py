import tkinter as tk
from observers.observer import Observateur


class AffichageEtat(Observateur):

    def __init__(self, parent):
        self._label = tk.Label(parent, text="Travail", font=("Arial", 16, "bold"))
        self._label.pack(pady=5)

def actualiser(self, sujet) -> None:
    donnees = sujet.get_donnees()
    etat = donnees["etat"]

    couleur = "black" if etat == "Travail" else "blue"

    self._label.config(
        text=etat,
        fg=couleur
    )
