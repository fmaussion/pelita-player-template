from pelita import datamodel
from pelita.graph import Graph, NoPathException, diff_pos
from pelita.player import AbstractPlayer, SimpleTeam


class FoodEatingPlayer(AbstractPlayer):

    def set_initial(self):

        # At game initialisation, we make a graph of all reachable positions
        self.graph = Graph(self.current_uni.reachable([self.initial_pos]))
        self.next_food = None

    def goto_pos(self, pos):
        """A helper method to give us the right move towards the given pos"""
        return self.graph.a_star(self.current_pos, pos)[-1]

    def get_move(self):

        # check if food we wanted to pick is still present
        if self.next_food is None or self.next_food not in self.enemy_food:
            if not self.enemy_food:
                # all food has been eaten? ok, game is over and i’ll stop
                return datamodel.stop
            # Then make a choice and stick to it
            self.next_food = self.rnd.choice(self.enemy_food)

        try:
            next_pos = self.goto_pos(self.next_food)
            move = diff_pos(self.current_pos, next_pos)
            return move
        except NoPathException:
            # This is case something unexpected happens
            return datamodel.stop


def team():
    return SimpleTeam("The Food Eating Players",
                      FoodEatingPlayer(), FoodEatingPlayer())
