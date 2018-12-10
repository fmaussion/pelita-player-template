# Pelita demo players

A template player and team package for the  [Pelita](https://github.com/ASPP/pelita) game, 
used for the final projects of the ACINN 
[scientific programming](https://fabienmaussion.info/scientific_programming) 
lecture.

## Notes on writing

* Please use Python 3
* Please use relative imports inside your package
* All `pelita` commands should be run from the root of the repository 
  (or outside of it), never from inside the `team/` folder, for example
* Simple testing can be done with a `pytest` command from the root folder

## Files

### `myteam/`

The main package which contains all your team’s code. Please use relative 
imports (`from .utils import bla`) from inside the package.

### `myteam/__init__.py`

The packages’s `__init__.py` is required to contain a function 
`team` which is supposed to return the main players for the 
tournament, for example:

    def team():
        return SimpleTeam("Local marsupials", KangarooPlayer(), KoalaPlayer())

### `team/demo_player.py`

Contains the code for a simple demo player. This player can then be 
imported in the `__init__.py` file.

### `team/utils.py`

This could be a good place for global utility functions (but feel free to 
add more files for this, if needed)

### `test/test_demo_player.py`

Simple unittest for your player. You can run 
tests using `pytest`, which automatically executes all tests in 
the `test/` directory.

    $ pytest
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.025s

    OK

### `demo_opponents/`

Some player for you to play against and get inspiration from. You goal should
be to be a bit better than them!

## Notes on gaming

You can start a game from anywhere else than the team folder. For example,
from the root folder:

    $ pelita myteam demo_opponents/PolitePlayers.py
    
Or:

    $ pelita demo_opponents/PolitePlayers.py myteam


## Licence

Code strongly inspired from the original Pelita players. The pelita license
is reproduced in COPYING.
