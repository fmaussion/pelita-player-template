from pelita import datamodel
from pelita.player import AbstractPlayer, SimpleTeam


class RandomExplorerPlayer(AbstractPlayer):
    """Will prefer moving to a position it’s never seen before."""

    def set_initial(self):
        """This method is called only once at the begining of the game."""
        self.visited = set()

    def get_move(self):

        # Add current position to the visited locations
        self.visited.add(self.current_pos)

        # From all possible moves pick the one which isn't visited yet
        not_visited = []
        for move, pos in self.legal_moves.items():
            if pos not in self.visited:
                not_visited.append(move)

        if len(not_visited) == 0:
            # OK pick one random
            return self.rnd.choice(list(self.legal_moves.keys()))

        # more than one move left
        return self.rnd.choice(not_visited)


def team():
    return SimpleTeam("Random Explorer Players",
                      RandomExplorerPlayer(), RandomExplorerPlayer())
