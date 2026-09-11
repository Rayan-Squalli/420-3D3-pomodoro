import tkinter as tk
from observers.observer import Observateur


class BarreProgression(Observateur):

    def __init__(self, parent):
        self._canvas = tk.Canvas(parent, width=300, height=20, bg="white")
        self._canvas.pack(pady=10)

def actualiser(self, sujet) -> None:
    donnees = sujet.get_donnees()

    temps_restant = donnees["temps_restant"]
    duree_totale = donnees["duree_totale"]

    largeur = int(300 * temps_restant / duree_totale)

    self._canvas.delete("all")

    self._canvas.create_rectangle(
        0,
        0,
        largeur,
        20,
        fill="green",
        outline=""
    )
