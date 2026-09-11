import tkinter as tk
from models.minuteur import Minuteur
from observers.affichage_temps import AffichageTemps
from observers.affichage_etat import AffichageEtat
from observers.barre_progression import BarreProgression
from observers.compteur_sessions import CompteurSessions
from observers.logger_session import LoggerSession


class Dashboard(tk.Tk):

    INTERVALLE_MS = 1000

    def __init__(self, minuteur: Minuteur):
        super().__init__()
        self.title("Minuteur Pomodoro")
        self.resizable(False, False)
        self._minuteur = minuteur
        self._en_marche = False

        self._creer_observateurs()
        self._abonner_observateurs()
        self._creer_boutons()

    def _creer_observateurs(self) -> None:
        self._affichage_temps = AffichageTemps(self)
        self._affichage_etat = AffichageEtat(self)
        self._barre_progression = BarreProgression(self)
        self._compteur_sessions = CompteurSessions(self)
        self._logger_session = LoggerSession()

    def _abonner_observateurs(self) -> None:
        self._minuteur.abonner(self._affichage_temps)
        self._minuteur.abonner(self._affichage_etat)
        self._minuteur.abonner(self._barre_progression)
        self._minuteur.abonner(self._compteur_sessions)
        self._minuteur.abonner(self._logger_session)

    def _creer_boutons(self) -> None:
        frame = tk.Frame(self)
        frame.pack(pady=10)

        self._btn_start = tk.Button(
            frame,
            text="Démarrer",
            command=self._demarrer
        )
        self._btn_start.pack(side=tk.LEFT, padx=5)

        self._btn_pause = tk.Button(
            frame,
            text="Pause",
            command=self._pause,
            state=tk.DISABLED
        )
        self._btn_pause.pack(side=tk.LEFT, padx=5)

        self._btn_reset = tk.Button(
            frame,
            text="Réinitialiser",
            command=self._reset
        )
        self._btn_reset.pack(side=tk.LEFT, padx=5)

    def _demarrer(self) -> None:
        self._en_marche = True

        self._btn_start.config(state=tk.DISABLED)
        self._btn_pause.config(state=tk.NORMAL)

        self._tick()

    def _pause(self) -> None:
        self._minuteur.basculer_pause()

        donnees = self._minuteur.get_donnees()

        if donnees["en_pause"]:
            self._btn_pause.config(text="Reprendre")
        else:
            self._btn_pause.config(text="Pause")
            self._tick()

    def _reset(self) -> None:
        self._en_marche = False

        self._minuteur.reinitialiser()

        self._btn_start.config(state=tk.NORMAL)
        self._btn_pause.config(
            state=tk.DISABLED,
            text="Pause"
        )

    def _tick(self) -> None:
        donnees = self._minuteur.get_donnees()

        if self._en_marche and not donnees["en_pause"]:
            self._minuteur.tick()

        if self._en_marche:
            self.after(self.INTERVALLE_MS, self._tick)