import tkinter as tk
from observers.observer import Observateur


class CompteurSessions(Observateur):

    def __init__(self, parent):
        self._label = tk.Label(
            parent,
            text="Sessions complétées : 0",
            font=("Arial", 12)
        )
        self._label.pack(pady=5)

def actualiser(self, sujet) -> None:
    donnees = sujet.get_donnees()
    sessions = donnees["sessions_completees"]

    self._label.config(
        text=f"Sessions complétées : {sessions}"
    )
