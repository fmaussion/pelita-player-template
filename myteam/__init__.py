from pelita.player import SimpleTeam
from .demo_player import KangarooPlayer
# (please use relative imports inside your package)


# The default myteam factory function, which this package must export.
# It must return an instance of `SimpleTeam`  containing
# the name of the myteam and the respective instances for
# the first and second player.
def team():
    return SimpleTeam("Kangaroo Team", KangarooPlayer(), KangarooPlayer())

# For testing purposes, one may use alternate factory functions::
#
#     def alternate_team():
#          return SimpleTeam("Our alternate Team",
#                            AlternatePlayer(), AlternatePlayer())
#
# To be used as follows::
#
#     $ pelita path_to/groupN/:alternate_team
