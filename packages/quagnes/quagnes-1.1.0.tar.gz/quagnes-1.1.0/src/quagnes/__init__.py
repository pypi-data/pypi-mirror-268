#   quagnes: a package for solving Agnes solitaire
#   Copyright (C) 2019, 2024 Ray Griner (rgriner_fwd@outlook.com)
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#------------------------------------------------------------------------------

"""A package for solving Agnes solitaire.

SUMMARY
-------
This package solves Agnes (Agnes Sorel) solitaire card games. It can be
used to solve games having the rules implemented in the GNOME AisleRiot
package and the rules attributed to Dalton in 1909 and Parlett in 1979
among others [1–3] and to calculate win rates.

EXAMPLE
-------
import random
import quagnes

random.seed(12345)
n_reps = 1000

attributes = ['n_states_checked', 'n_deal', 'n_move_to_foundation',
    'n_move_card_in_tableau','n_no_move_possible','max_score','max_depth',
    'current_depth']

# header for the output file
print('rc,' + ','.join(attributes))

for rep in range(0, n_reps):
    new_game=quagnes.Agnes()
    rc = new_game.play()

    # Write the return code and selected attributes from the game
    out_str = (str(rc) + ',' +
        ','.join([ str(getattr(new_game, attr)) for attr in attributes ]))
    print(out_str, flush=True)

    # rc==1 are games that were won
    if rc==1:
        f = open(f'winners/win{rep}.txt', 'w', encoding='utf-8')
        f.write(new_game.print_history())
        f.close()

BACKGROUND
----------
Agnes is a difficult solitaire card game under some rule variants. This
package solves the game automatically.

Users can simulate random games and calculate win rates under various
permutations of rules, including moving sequences (runs) by same-suit or
same-color, allowing or not same-suit runs to be split in the middle of the
run for a move, dealing all tableau cards face-up at the start versus
dealing only the final tableau card face-up, and whether and how empty
columns can be filled in between deals (never, a single card of any rank, a
single card of the highest rank, a run starting with a single card of any
rank, or a run starting with a card of the highest rank). The package
provides additional options for debugging and tuning of the search algorithm
to be more memory-efficient at the expense of speed.

In 1979 Parlett named the two main variants of Agnes as Agnes Sorel (the
variant / set of variants described here) and Agnes Bernauer (a variant/set
of variants that uses a reserve) [3]. This package only considers Agnes
Sorel.

REFERENCES
----------
[1] Agnes (card game). Wikipedia.
   https://en.wikipedia.org/wiki/Agnes_(card_game). Retrieved
   March 15, 2024.

[2] Dalton W (1909). "My favourite Patiences" in The Strand Magazine,
    Vol 38.

[3] Parlett D (1979). The Penguin Book of Patience. London: Penguin.
"""

#------------------------------------------------------------------------------
# File:    __init__.py
# Date:    2024-03-14
# Author:  Ray Griner
# Changes:
#------------------------------------------------------------------------------
__author__ = 'Ray Griner'
__version__ = '1.1.0'
__all__ = ['Agnes']

from .agnes import Agnes
