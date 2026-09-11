from models.subject import Sujet


DUREE_TRAVAIL = 25 * 60
DUREE_PAUSE = 5 * 60


class Minuteur(Sujet):

    def __init__(self):
        super().__init__()
        self._temps_restant = DUREE_TRAVAIL
        self._en_pause = False
        self._etat = "Travail"
        self._sessions_completees = 0

    def tick(self) -> None:
        """Avance le minuteur d'une seconde et notifie les observateurs."""
        if self._en_pause:
            return

        if self._temps_restant > 0:
            self._temps_restant -= 1
        else:
            self._changer_etat()

        self.notifier()

    def _changer_etat(self) -> None:
        """Bascule entre travail et pause."""
        if self._etat == "Travail":
            self._sessions_completees += 1
            self._etat = "Pause"
            self._temps_restant = DUREE_PAUSE
        else:
            self._etat = "Travail"
            self._temps_restant = DUREE_TRAVAIL

    def basculer_pause(self) -> None:
        """Met en pause ou reprend le minuteur."""
        self._en_pause = not self._en_pause
        self.notifier()

    def reinitialiser(self) -> None:
        """Réinitialise le minuteur à l'état initial."""
        self._temps_restant = DUREE_TRAVAIL
        self._en_pause = False
        self._etat = "Travail"
        self._sessions_completees = 0

        self.notifier()

    def get_donnees(self) -> dict:
        return {
            "temps_restant": self._temps_restant,
            "etat": self._etat,
            "en_pause": self._en_pause,
            "sessions_completees": self._sessions_completees,
            "duree_totale": (
                DUREE_TRAVAIL
                if self._etat == "Travail"
                else DUREE_PAUSE
            )
        }