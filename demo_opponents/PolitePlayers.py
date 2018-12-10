from pelita import datamodel
from pelita.player import AbstractPlayer, SimpleTeam

POLITE_WORDS = ['Sorry', 'Ups', 'Excuse me']


class PolitePlayer(AbstractPlayer):
    """Speaks when stepping on a friendly bot."""

    def get_move(self):
        # There is just one other player
        other = self.other_team_bots[0]
        if self.current_pos == other.current_pos:
            self.say(self.rnd.choice(POLITE_WORDS))
        return self.rnd.choice(list(self.legal_moves.keys()))


def team():
    return SimpleTeam("The Polite Players",
                      PolitePlayer(), PolitePlayer())
