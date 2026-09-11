import tkinter as tk
from observers.observer import Observateur


class AffichageTemps(Observateur):

    def __init__(self, parent):
        self._label = tk.Label(parent, text="25:00", font=("Arial", 48, "bold"))
        self._label.pack(pady=10)

def actualiser(self, sujet) -> None:
    donnees = sujet.get_donnees()
    temps_restant = donnees["temps_restant"]

    minutes = temps_restant // 60
    secondes = temps_restant % 60

    self._label.config(
        text=f"{minutes:02d}:{secondes:02d}"
    )

