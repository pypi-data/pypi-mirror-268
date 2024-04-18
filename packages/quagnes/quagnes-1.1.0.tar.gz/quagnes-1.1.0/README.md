# Summary
This package solves Agnes (Agnes Sorel) solitaire card games. It can
be used to solve games having the rules implemented in the GNOME AisleRiot
package and the rules attributed to Dalton in 1909 (with a minor variant
in the table layout) and Parlett in 1979 among others [1–3] and to
calculate win rates.

# Example
```
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

    # rc==1 are games that were won, but probably best to only print a
    # limited number for debugging or for rule variants when
    # win rate is low

    #if rc==1:
    #    f = open(f'winners/win{rep}.txt', 'w', encoding='utf-8')
    #    fwrite(new_game.print_history())
    #    f.close()
```

# Release Notes
## Version 1.1.0
### Fixes Affecting Simultation Results
- No longer forbid splitting of runs between same-suit cards when the stock
has two cards left, even when neither the source nor target pile can be
covered by a future deal. This optimization is incorrect, ie, it could
force some winning games to be reported as losses.
- Previously, splitting runs between cards of the same suit was not allowed
when the stock was empty when runs are moved by suit. Add the condition that
`Card(rank=last_card.rank - 1, suit=last_card.same_color_suit)` must also be
in the foundation or meet the criteria for being forced to the foundation
when it appears (for such splits to be forbidden), where `last_card` is the
last card in the run moved. The additional condition is because placing the
same-color suit at the bottom of the pile makes the pile unmovable, and so
it would matter whether or not the split was performed. So we only forbid
splits when this cannot be the case.

### Fixes Improving Run-Time
- When checking whether a card is the last in the pile (which is used to
determine whether a tableau move should be forced), we previously failed to
consider the card that would become last in a pile after the move. These
cards are now considered.
- Add optimization to force the last deal if the two dealt cards will
immediately be forced to the foundation if `Card(rank - 2, same_color_suit)`
is already in the foundation. Attributes were added to the `_AgnesState`
class to store the last and second to last card, whether they are of the
same suit in-sequence, and whether they are the same color, but not the
same suit.
- Add optimization to sort the tableau piles that can no longer be covered
by a deal before storing in or checking against the losing states set. The
piles are sorted by their top card.

### Other Changes
- Add `in_foundation` function to `_AgnesState` class.

# External Documentation
A C++ implementation written by this package author also exists in a git
repository.  Detailed information on the background, game rules, program
methodology, and analysis of win rates are available [there](https://github.com/ghrgriner/quagnes-cpp/wiki/Rules,-Methodology,-and-Analysis-of-Win-Rates).

# Using the Package
Games are simulated by creating an `Agnes` object with the appropriate
parameters, running `Agnes.play()`, and then using the return code and
extracting desired statistics from `Agnes` class attributes.

## Input Parameters
The following are the parameters used to construct `Agnes` objects:

|Parameter | Type | Description |
|:-------- | :----- | :---------  |
|`deck_filename` | `str` | Read deck from text file. If empty, a random deck will be used by calling `random.shuffle` and reversing the results. The text file should consist of 52 lines with each line formatted as `(rank, suit)`, where rank is in {0, 1, ..., 12} and suit is in {0, 1, 2, 3}. Suits are the same color if their value is equal modulus 2. The first card dealt is the base card.|
|`move_to_empty_pile`| `str` | Rule for what can be moved to empty tableau piles. See following table for valid values.|
|`move_same_suit`| `boolean` | If True, move runs by suit. If False (default), move runs by color.|
|`split_runs` | `boolean` | If True, movable runs must be moved in their entirety. If False (default), a movable run can be split for a move).|
|`face_up`| `boolean` |  If True, deal all cards face-up in the tableau. If False (default), only the last card in each column. |
|`track_threshold`| `int` | If the number of cards left in the stock is greater than or equal to this value (default = 0), track losing states in a single set for the whole game. This set can consume a lot of memory if some of the other options are chosen that allow a large number of moves (eg, `move_to_empty_pile != 'none'`).|
| `print_states` | `boolean` | Print detailed information about each state as moves are performed and undone. |
| `maximize_score` | `boolean` | Maximize score. Disable optimization that inspects the layout of highest-ranked cards in the tableau to determine if game is unwinnable. |
| `max_states` | `int` | Terminate game with return code 3 when number of states examined exceeds this threshold. 0 (default) means no threshold is used.|

### Rule for Moving to Empty Piles
|Value of `move_to_empty_pile` | Description |
|:-------- | :---------  |
|`'none'` | Empty piles can only be filled when dealing from stock (default). |
|`'any run'` | Empty piles can be filled by any movable card or movable run. |
|`'high run'` | Empty piles can be filled by any movable highest-rank card or movable run starting with a highest-rank card. |
|`'any 1'` | Empty piles can be filled by any movable single card, but not by a movable run of more than one card. |
|`'high 1'` | Empty piles can be filled by a single movable highest-rank card, but not by a movable run of more than one card. |

## Output
### `Agnes.play()` Return Code and `Agnes` Attributes
The return code of the `Agnes.play()` function indicates whether the game is
winnable (return code = 1), not winnable (return code = 2), or the
simulation was terminated due to reaching the maximum number of states
specified by the `max_states` parameter (return code = 3). The `Agnes`
object has attributes with the same name and type as the input parameters
that store the values of the parameters used during object construction.
In addition, the following attributes of `Agnes` are updated when
`Agnes.play()` is executed:

| Attribute | Description |
| :------------   | :---------  |
| `n_states_checked` | Count number of states checked (including repeats). |
| `n_deal` | Count number of deals performed (including those undone). |
| `n_foundation` | Count number of moves to foundation performed (including those undone). |
| `n_move_card_in_tableau` | Count number of moves in tableau performed (including those undone). |
| `max_score` | Maximum score found during play. (If moving to empty piles is not allowed, this will not be the true maximum, unless `-z` was specified to disable the optimization that tries to detect unwinnable games from the location of the highest-rank cards in the tableau.) |
| `max_depth` | Maximum depth of the search tree of moves. |
| `current_depth` | Depth of the search tree when the game was terminated. This value is always 0 for losing games. |

### Detailed Program Output
When `print_states=True` for the `Agnes` object, `Agnes.play()` will print
to standard output each state as moves are performed or undone.

```
Move: Move 2 card(s) from pile 1 to pile 3

piles:16#9-8-7##49-19-44##28-51-15-31##3-33-14-5-30-29##45-23-35##43-34-42-0-13-48-47-50##20-21-41-2-37#
depth:11, n_stock_left:16, valid_moves:[DealMove(), TablMove(from_=3, n_cards=2, to_=2, expose=False, tabltype=2)]
Foundations:[-1, -1, 1, 1]
T0:[] | [(9, 0), (8, 0), (7, 0)]
T1:[] | [(10, 3), (6, 1), (5, 3)]
T2:[] | [(2, 2), (12, 3), (2, 1), (5, 2)]
T3:[] | [(3, 0), (7, 2), (1, 1), (5, 0), (4, 2), (3, 2)]
T4:[] | [(6, 3), (10, 1), (9, 2)]
T5:[] | [(4, 3), (8, 2), (3, 3), (0, 0), (0, 1), (9, 3), (8, 3), (11, 3)]
T6:[] | [(7, 1), (8, 1), (2, 3), (2, 0), (11, 2)]
in_suit_seq:0011 0011 0000 0010 0010 0000 0000 1000 1001 0000 0000 0000 0000
last_in_pile:0011 0011 0000 0010 0000 0011 0000 1000 0000 0010 0000 0011 0000

Last move info:[10-2-T-T, 11-2-F-T, 0-0-F-T, 11-2-T-T, 10-2-F-T, 0-0-F-T, 9-1-F-T]
```

A line-by-line explanation of this output is provided in [the git repository of the C++ implementation](https://github.com/ghrgriner/quagnes-cpp/wiki/Program-Input-and-Output#explanation-of-detailed-output).
However, note that this Python package does not write any messages to
standard error.

# References
[1] Agnes (card game). Wikipedia.
    https://en.wikipedia.org/wiki/Agnes_(card_game). Retrieved
    March 15, 2024.

[2] Dalton W (1909). "My favourite Patiences" in The Strand Magazine,
    Vol 38.

[3] Parlett D (1979). The Penguin Book of Patience. London: Penguin.

# Disclosures
We are not affiliated with any of the books, websites, or applications
discussed in this documentation, except for this Python package and
previously-mentioned C++ implementation which we wrote.
