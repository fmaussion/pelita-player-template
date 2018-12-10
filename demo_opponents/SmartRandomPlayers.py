from pelita.datamodel import stop
from pelita.player import AbstractPlayer, SimpleTeam


class SmartRandomPlayer(AbstractPlayer):
    """A player that will move randomly but not stupidly."""

    def get_move(self):

        # Note that these might be noisy positions, but if one of them
        # is near us it will guaranteed not noisy
        dangerous_enemy_pos = [bot.current_pos
                               for bot in self.enemy_bots if bot.is_destroyer]
        killable_enemy_pos = [bot.current_pos
                              for bot in self.enemy_bots if bot.is_harvester]

        smart_moves = []
        for move, new_pos in list(self.legal_moves.items()):
            if move == stop or new_pos in dangerous_enemy_pos:
                # bad idea to go into an enemy who can eat us
                continue
            elif (new_pos in killable_enemy_pos or
                  new_pos in self.enemy_food):
                # get it!
                return move
            else:
                smart_moves.append(move)

        # OK select one of these smart ones
        if smart_moves:
            return self.rnd.choice(smart_moves)
        else:
            # we ran out of smart moves
            return stop


def team():
    return SimpleTeam('The Smart Random Players',
                      SmartRandomPlayer(), SmartRandomPlayer())
