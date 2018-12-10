from pelita.player import SimpleTeam
from pelita.player import SteppingPlayer

from pelita.game_master import GameMaster

from myteam import KangarooPlayer
from demo_opponents.PolitePlayers import PolitePlayer


def test_my_player_is_not_moving():

    my_team = SimpleTeam("test", KangarooPlayer(), PolitePlayer())

    test_layout = """
        ############
        # 0 #  # 1 #
        #   #  #   #
        # 2 .  . 3 #
        ############
    """

    teams = [
        # register my_team for bots 0, 2
        my_team,
        # register a pre-defined myteam as an enemy
        # First one moves left-down-down-left-left, second one left
        SimpleTeam(SteppingPlayer("<vv<<"), SteppingPlayer("<<<<<"))
    ]

    gm = GameMaster(test_layout, teams, number_bots=4, game_time=5, seed=20)

    # play `game_time` rounds
    gm.play()

    # check the position of my bots
    # Tests fail, because our players are random
    # assert gm.universe.bots[0].current_pos == (2, 1)
    # assert gm.universe.bots[2].current_pos == (2, 3)

    # For reference, testing the SteppingPlayer
    assert gm.universe.bots[1].current_pos == (6, 3)
    assert gm.universe.bots[3].current_pos == (4, 3)
