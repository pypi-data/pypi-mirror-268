#   A module for solving Agnes solitaire
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

#------------------------------------------------------------------------------
# File:    agnes.py
# Date:    2019-03-19
# Author:  Ray Griner
# Purpose: AgnesState class definition
# Changes:
# [20240314RG]: (1) Add type hints. (2) Change attribute name _AgnesState.exp
#   to _AgnesState.exposed. (3) Make moves and _AgnesState.exposed tuples
#   instead of lists. (4) Minor bug fix when validating suits in deck passed
#   as input. (5) previous version assumed all piles in tableau were exposed,
#   now this is controlled via an input parameter. (6) Change
#   '_AgnesState.found' attribute to 'foundation' (7) Removed
#   `move_from_same_suit` parameter until I can confirm exactly what the game
#    variant rules are.
# [20240316RG]: (1) Improve documentation. (2) Add `no_print` parameter
#    to _undo_move that is set to True when called from Agnes.print_history.
#    (3) Reimplement `move_from_same_suit` parameter functionality (except now
#    renamed to `split_same_suit_runs`. To facilitate, calc_n_movable changed
#    to return list of integers with the number of cards that can be moved
#    instead of the maximum number that can be moved from a pile.
#    (4) Change `move_to_empty_pile` parameter to be 'none', 'any', 'highest'
#    instead of True (now 'any') or False (now 'none').
#    (5) Change `expose_all` parameter name to `face_up`.
# [20240322RG]: (1) Bug fix, add `Agnes._check_for_loops` that is true when
#    `split_same_suit_runs` is true or `move_to_empty_pile != "none"`.
#     Previously we were just checking for loops when the first half of
#     this was true, giving infinite loops in the second case.
#  (2) If there is more than one empty target pile that cannot be covered by
#     a future deal, all such piles are equivalent and it is only permitted
#     to move to the first.
#  (3) Do not permit moving entire pile to a different empty pile if both
#     the source and target column cannot be covered by a future deal.
#  (4) Refactor: make AgnesPile a namedtuple class to reduce the amount of
#     code that needs an explicit index.
#  (5) Refactor: Add n_movable attribute to _AgnesState and rename
#     calc_n_movable to set_n_movable. Call this function on a pile whenever
#     a pile is updated, instead of calling it for every pile.
#  (6) Add uncompressed printing of table state to make it each to search for
#     prior state when print_states=`True`. When printing compressed string
#     to store in the set, change to use '#' and '-' since the character code
#     for these are not in the range of codes that will be used by cards (which
#     start at ASCII code 48).
#  (7) Do not allow splitting of any run (same-suit or otherwise) once the
#     stock is empty, unless EmptyRule is 'any 1' or 'high 1'.
# [20240403RG] (1) Change `split_same_suit_runs` constructor parameter and
#  `Agnes` attribute to `split_runs` and use the same logic to decide
#  whether run must be moved in its entirety when `move_same_suit=false`.
#  (2) Add new class attributes needed for run-time optimizations
#  (2a) Create `_all_lmi` attribute on `Agnes` that stores a stack of
#     newly defined LastMoveInfo objects.
#  (2b) Add `tabltype` attribute to Move objects and enum for this to store
#     whether a tableau move joined or split a same-suit sequence (considering
#     only the top card of the pile). Similarly used for moves to foundation.
#  (2c) Added `last_in_pile` and `in_suit_seq` attributes to `_AgnesState`
#     objects to store whether a card is the final card in a tableau pile
#     (or in the foundation) or in an exposed pile under a same-suit card that
#     has one higher rank, respectively. These are both implemented as 13x4
#     arrays and are updated / undone for each move using the new attribute
#     from change (2b).
#  (2d) Added _dont_deal_last function
#  (3) Optimzations:
#  (3a) When stock is 0 and empty_rule not in 'any 1' or 'high 1'... then
#    never split a run between the same suit, regardless of whether moving
#    by suit or color.
#  (3b) When stock is 0 and empty_rule not in 'any 1' or 'high 1'... then
#    force joins by suit sequence if the same-color top card of the pile being
#    moved is (i) already in the foundation or (ii) `move_same_suit=false` and
#    already under the next-highest card of the same suit (`in_suit_seq`) or
#    (iii) `move_same_suit=false` and the card from the same-color suit is
#    also available to be played on (`last_in_pile`).
#  (3c) Do not move a card to the foundation unless one of the following is
#    true:
#     - track_threshold <= n_stock_left (ie, we are still using the
#       losing_states set)
#     - last_move_info[from_pile].depth == 0, ie, last operation on the pile
#       wasn't a move within tableau to or from this pile
#     - last_move_info[from_pile].can_move_to_found = true, ie, if the last
#       operation was a move to this pile, we set can_move_to_found = true if
#       it was NOT possible to perform the move to foundation when the tableau
#       move was done.
# (3d) If track_threshold > n_stock_left, do not allow reversing a move
#   between two piles if no other operations have been done on those piles.
#   Reversing a move means moving the same number of cards back that were
#   originally moved.
# (3e) When track_threshold is > 2, do not deal last deal if there there are
#   two columns that will not be covered by the final deal where we just moved
#   from one to the other with no other operations. (This restriction forces us
#   to only consider the case when such moves are done after the last deal.)
# (3f) Additional restriction on splitting same suit besides those implied by
#   `split_runs` (which were implemented in set_n_movable). Only allow splits
#   of same suit if source or target will be covered by future deal, or
#   `split_empty_stock=True` or Card(src_card.rank, same_color_suit(src_card))
#   is not in the foundation, where src_card is the highest-rank card in the
#   part of the pile that is being moved.
# 20240413:
# Fixes to Optimization (8). These were causing wins to be reported as losses
# for a small number of games.
# (1) No longer forbid splitting of runs between same-suit cards when the stock
#   has two cards left, even when neither the source nor target pile can be
#   covered by a future deal. This optimization was incorrect, it causes a
#   small umber of wins to be reported as losses.
# (2) Previously splitting of same-suit runs was not allowed when the stock was
#   empty when runs are moved by suit. Add the condition that
#   Card(rank=last_card.rank - 1, suit=same_color_suit) must also be in the
#   foundation (for such splits to be forbidden) or forcable to the foundation
#   where last_card is the last card in the run moved. The additional condition
#   is because placing the same color suit at the bottom of the pile makes the
#   pile unmovable, and so it would matter whether or not the split was
#   performed. So we only forbid splits when this cannot be the case.
#
# New Optimizations to improve run time:
# (3) When checking whether a card is the last in the pile (which is used to
#   determine whether a tableau move should be forced), we previously failed to
#   consider the cards that will newly last in a pile after a move. These cards
#   are now considered.
# (4) Add Optimization (9) to force the last deal if the two dealt cards will
#   immediately be forced to the foundation according to the first part of
#   Optimization (8d) (but not considering whether the 1-lower same-color card
#   is in suit-sequence. Attributes were added to the `AgnesState` class to
#   store the last and second to last card, whether they are of the same suit
#   in sequence, and whether they are the same color, but not the same suit.
# (5) Add Optimization (10) to sort the tableau piles that can no longer be
#   covered by a deal before storing in or checking against the losing states
#   set. The piles are sorted by their top card. New attributes `sort_order`
#   and `pile_sort_info` in AgnesState.
#------------------------------------------------------------------------------
"""A module for solving Agnes solitaire. """

import random
import copy
from typing import Set, Optional, Union, NamedTuple
from dataclasses import dataclass
from enum import Enum

__all__ = ['Agnes']
__author__ = 'Ray Griner'

# Each card is a tuple with two members. Use these to access.
#_RANK = 0
#_SUIT = 1

#------------------------------------------------------------------------------
# Type aliases
#------------------------------------------------------------------------------
CardRank = int
CardSuit = int
#Card = tuple[CardRank, CardSuit]
#Card = collections.namedtuple('Card', 'rank suit')
#
#class Card(NamedTuple):
#    rank: CardRank
#    suit: CardSuit

@dataclass(frozen=True, slots=True)
class LastMoveInfo:
    """Information about the last tableau move performed on a pile.

    Attributes
    ----------
    depth : int
        Depth at which the last tableau move to or from this pile was
        performed. Set to 0 if no prior such move or when a move to
        foundation or deal on the pile occurs.
    n_moved : int
        Number of cards moved during the last tableau move to or from
        this pile. Set to 0 if depth is set to 0.
    moved_to : bool
        True if depth is not 0 and this was the pile moved to.
    can_move_to_found : bool
        Set to false if depth is not 0 and the bottom card in the run
        being moved could have been put into the foundation before the
        move. This is set on the pile that was moved to. Otherwise, true.
    """
    depth: int = 0
    n_moved: int = 0
    moved_to: bool = False
    can_move_to_found: bool = True

#@dataclass(frozen=True)
class SetNMovableOpts(NamedTuple):
    """Options to pass to the `set_n_movable` function.
    """
    move_same_suit: bool
    split_runs: bool
    split_empty_stock: bool

@dataclass(frozen=True, slots=True)
class Card:
    """Dataclass representing a card in the deck.

    Attributes
    ----------
    rank : CardRank
        Rank of the card
    suit : CardSuit
        Suit of the card. Suits that are equal modulus 2 are the same color.
    """
    rank: CardRank
    suit: CardSuit

    def __repr__(self) -> str:
        return f'({self.rank}, {self.suit})'

    # Represent a card as a single byte string
    def strcompr(self) -> str:
        """A compressed single character representation.

           Used when writing the state to the cache.
        """
        return str(chr(48+13*self.suit+self.rank))

    # Represent a card as a readable string
    def struncomp(self) -> str:
        """An uncompressed representation.

           Used when printing the state for humans to read.
        """
        return str(13*self.suit+self.rank)

    def twochar(self) -> str:
        """Return a two character string representing the card, eg, '3♦'."""
        if self.rank==0:
            rank_str = 'A'
        elif self.rank==12:
            rank_str = 'K'
        elif self.rank==11:
            rank_str = 'Q'
        elif self.rank==10:
            rank_str = 'J'
        else:
            rank_str = str(self.rank)

        if self.suit==0:
            suit_str='♣'
        elif self.suit==1:
            suit_str='♦'
        elif self.suit==2:
            suit_str='♠'
        elif self.suit==3:
            suit_str='♥'

        return rank_str+suit_str

class AgnesPile(NamedTuple):
    """Represents a tableau pile.

    Attributes
    ----------
    n_movable : list[int]
        List of ints representing the number of cards that can be moved from
        the tableau column (without considering whether there is a
        destination that columns can be moved to). For example, if the
        bottom cards in a column are 3S, 4S, 5H, the value is 2, even if
        there is no 5C or 5S exposed.
    exposed : list[Card]
        List of exposed cards in the pile. Highest index indicates cards
        at the bottom of the column in the tableau.
    hidden: list[Card]
        List of hidden cards in the pile. Highest index indicates cards
        at the bottom of the column in the tableau.
    """
    n_movable: list[int]
    hidden: list[Card]
    exposed: list[Card]

@dataclass
class PileSortInfo():
    n_stock_left: int
    pile_index: int
    pile: AgnesPile

@dataclass(frozen=True)
class DealMove:
    """Dataclass representing a deal from the stock."""
    def __str__(self) -> str:
        return 'Deal'

class TablType(Enum):
    """Indicates if a tableau move splits or joins a same-suit sequence.

    Also used for moves to foundation (NONE and SPLIT only).
    """
    NONE = 0
    SPLIT = 1
    JOIN = 2

@dataclass(frozen=True, slots=True)
class MoveToFound:
    """Dataclass representing a move of one card to the foundation.

    Attributes
    ----------
    from_ : int
        Pile from which the card was taken.
    suit : CardSuit
        Suit of the card being moved.
    expose : bool
        Indicates whether a hidden card was exposed after the move.
    tabltype : TablType
        Indicates whether the card being moved was in sequence under
        a card of the same suit (TablType.SPLIT) or not (TablType.NONE).
    """
    from_: int
    suit: CardSuit
    expose: bool
    tabltype: TablType

    def __str__(self) -> str:
        str2 = ''
        str1 = (f'Move bottom card from pile {self.from_} to foundation '
                f'{self.suit}')
        if self.expose:
            str2 = ' (exposes a card)'
        return str1 + str2

    def __repr__(self) -> str:
        retlist: list[str] =['MoveToFound(from_=', str(self.from_),
            ', suit=', str(self.suit)]
        if self.expose:
            retlist.append(', expose=True')
        else:
            retlist.append(', expose=False')
        retlist.append(', tabltype=')
        retlist.append(str(self.tabltype.value))
        retlist.append(')')
        return ''.join(retlist)

@dataclass(frozen=True, slots=True)
class TablMove:
    """Dataclass representing a move in the tableau.

    Attributes
    ----------
    from_ : int
        Pile from which the run was moved.
    n_cards : int
        Number of cards in the run that was moved.
    to_ : int
        Pile to which the run was moved.
    expose : bool
        Indicates whether a hidden card was exposed after the move.
    tabltype : TablType
        Indicates whether the highest-rank card in the run being moved was
        in sequence under a card of the same suit (TablType.SPLIT) or
        will be in such sequence after the move (TablType.JOIN) or neither
        (TablType.NONE).
    """
    from_: int
    n_cards: int
    to_: int
    expose: bool
    tabltype: TablType

    def __str__(self) -> str:
        str2 = ''
        str1 = (f'Move {self.n_cards} card(s) from pile {self.from_} to pile '
               f'{self.to_}')
        if self.expose:
            str2 = ' (exposes a card)'
        return str1 + str2

    def __repr__(self) -> str:
        retlist: list[str] =['TablMove(from_=', str(self.from_),
            ', n_cards=', str(self.n_cards), ', to_=', str(self.to_)]
        if self.expose:
            retlist.append(', expose=True')
        else:
            retlist.append(', expose=False')
        retlist.append(', tabltype=')
        retlist.append(str(self.tabltype.value))
        retlist.append(')')
        return ''.join(retlist)

class EmptyRule(Enum):
    """Rule for what can be moved to an empty tableau pile.
    """
    NONE = 0
    ANY1 = 1
    ANYRUN = 2
    HIGH1 = 3
    HIGHRUN = 4

AgnesGraph = dict[CardSuit, set[CardSuit]]
ExpHidd = tuple[list[Card], list[Card], list[Card], list[Card], list[Card],
    list[Card], list[Card]]
NMovable = tuple[list[int], list[int], list[int], list[int], list[int],
    list[int], list[int]]
#AgnesMove = tuple[int, ...]
AgnesMove = Optional[Union[MoveToFound, TablMove, DealMove]]

#------------------------------------------------------------------------------
# Static functions
#------------------------------------------------------------------------------
# describe_move: Change a list that represents a move into text description for
#   printing
#------------------------------------------------------------------------------
def _describe_move(move: Optional[AgnesMove]) -> str:
    if move is None:
        return 'Initial layout'
    else:
        return str(move)

def _empty_rule_str_to_enum(emptyrule_str: str) -> EmptyRule:
    return {
        'none': EmptyRule.NONE,
        'any 1': EmptyRule.ANY1,
        'any run': EmptyRule.ANYRUN,
        'high 1': EmptyRule.HIGH1,
        'high run': EmptyRule.HIGHRUN,
           }[emptyrule_str]

def _empty_rule_to_split_empty_stock(emptyrule_str: str) -> bool:
    return {
        'none': False,
        'any 1': True,
        'any run': False,
        'high 1': True,
        'high run': False,
           }[emptyrule_str]

def _dont_deal_last(last_move_info: list[LastMoveInfo]) -> bool:
    anydup: set[int] = set()
    for pile_index in range(2, 7):
        if last_move_info[pile_index].depth > 0:
            if last_move_info[pile_index].depth in anydup:
                return True
            else:
                anydup.add(last_move_info[pile_index].depth)
    return False

#------------------------------------------------------------------------------
# The largest trees hit a memory limit when writing to the losing_states set
# so here we do some simple compression for the string representation rather
# than using the form generated by __repr__ (which we keep for use in debugging
# output).
#------------------------------------------------------------------------------

# Each tableau pile is a string of ASCII codes representing the cards,
#  starting with '+'.
def _strpilecomp(pile: list[Card]) -> str:
    return '#' + ''.join([tpl.strcompr() for tpl in pile])

def _strpileuncomp(pile: list[Card]) -> str:
    return '#' + '-'.join([tpl.struncomp() for tpl in pile])

#------------------------------------------------------------------------------
# Depth-first search to detect if a king or a set of kings is blocking cards
#  in such a way that the game is unwinnable.
#------------------------------------------------------------------------------
def _cyclic(g: AgnesGraph) -> bool:
    current_path: set[CardSuit] = set()
    visited: set[CardSuit] = set()

    def visit(vertex: CardSuit) -> bool:
        if vertex in visited: return False
        visited.add(vertex)
        current_path.add(vertex)
        for neighbor in g.get(vertex, ()):
            if neighbor in current_path or visit(neighbor): return True
        current_path.remove(vertex)
        return False

    return any(visit(v) for v in g)

class Agnes:
    """
    A class used to represent a game of Agnes solitaire

    Attributes
    ----------
    n_states_checked : int
        Number of states examined
    n_deal : int
        Number of deals performed
    n_move_card_in_tableau : int
        Number of moves of card(s) between piles in tableau
    n_move_to_foundation : int
        Number of times a card was moved to foundation
    n_no_move_possible : int
        Number of states created where no move was possible
    max_depth : int
        Maximum depth of the search tree
    current_depth : int
        Current depth of the search tree
    max_score : int
        Maximum score obtained (i.e., maximum number of cards moved
        to the foundations). For the default input parameters, the
        program backtracks as soon as it detects a state cannot be
        won. A higher maximum score may be possible if the game were
        played in full.
    maximize_score : boolean
        Stores value of input parameter with the same name
    move_to_empty_pile : str
        Stores value of input parameter with the same name
    move_same_suit : boolean
        Stores value of input parameter with the same name
    split_runs : boolean
        Stores value of input parameter with the same name
    face_up : boolean
        Stores value of input parameter with the same name
    maximize_score : boolean
        Stores value of input parameter with the same name
    track_threshold : boolean
        Stores value of input parameter with the same name
    print_states : bool
        Stores value of input parameter with the same name
    test_deck : bool
        Stores value of input parameter with the same name
    deck_filename : bool
        Stores value of input parameter with the same name
    max_states : boolean
        Stores value of input parameter with the same name
    """

    def __init__(self,
                 move_to_empty_pile: str = 'none',
                 move_same_suit: bool = False,
                 split_runs: bool = True,
                 face_up: bool = False,
                 maximize_score: bool = False,
                 track_threshold: int = 0,
                 print_states: bool = False,
                 test_deck: int = 0,
                 deck_filename: Optional[str] = None,
                 max_states: int = 0):
        """
        Parameters
        ----------
        move_to_empty_pile : {'none', 'high 1', 'any 1', 'high run', 'any run'}
            Optional parameter, default is 'none'. Describes which single
            cards or runs can be moved to an empty pile.
            'none': (default), no card can be moved from the tableau. Empty
                piles are only filled when dealing from stock.
            'any 1': Any single card can be moved.
            'high 1': Any single card of highest rank can be moved. For
                example, if the base card is a 3, then a 2 can be moved.
            'any run': Any movable run can be moved.
            'high run': Any movable run that is built down from a card of
                highest rank.
        move_same_suit : boolean, optional (default = False)
            If True, only permit moving sequences of cards in the tableau
            that are the same suit. Otherwise, permit moving sequences of
            cards that are the same color.
        split_runs: boolean, optional (default = True)
            If True, allow a movable run to be split during a move. If
            false, movable runs must be moved in their entirety.
        face_up : boolean, optional (default = False)
            Deal all cards face up in the tableau.
        track_threshold : int, optional (default = 0)
            If the number of cards left in the stock is greater than or
            equal to this value, track losing states in a single set for
            the whole game. This set can consume a lot of memory if some of
            the other options are chosen that allow a large number of moves
            (eg, `move_to_empty_pile != 'none'`).
        print_states : boolean, optional (default = False)
            Print game states as moves are made. See `Agnes.print_history`
            for output format.
        maximize_score : boolean, optional (default = False)
            Determine the maximum score. Disables the algorithm used when
            `move_to_empty_pile == 'none'` that stops playing the game
            when it detects a game is unwinnable.
        test_deck : {0, 1}, optional (default = 0)
            If 0, a random deck is generated. If 1, a fixed test deck that
            wins is used.
        deck_filename : string, optional
            Read deck from text file, If empty, a random deck will be
            used by calling random.shuffle and reversing the results.
            The text file should consist of 52 lines with each line is
            formatted as "(rank, suit)", where rank is in 0..12 and
            suit is in 0..3. Note the first card dealt is the base card.
        max_states : int, optional
            Terminate game with return code 3 when number of states
            examined exceeds this threshold.  0 (default) means no
            threshold is used.
        """
        if print_states: print('Start Agnes()')

        # Initial deck, before standardizing so the base card has rank 0
        self._initial_deck: list[Card] = []
        # Deck after standardizing the base card
        self._deck: list[Card] = []
        # List to track the valid moves remaining for each state in the stack
        self._all_valid_moves: list[list[AgnesMove]] = []
        self._all_lmi: list[list[LastMoveInfo]] = []
        # List of states we have been since the last deal or move-to-foundation
        # This is to check that we don't enter an infinite loop of moving
        # cards in the tableau.
        self._check_loops: set[str] = set()
        # Moves performed to reach each state.
        self._moves: list[AgnesMove] = []
        self._curr_state: _AgnesState = _AgnesState()
        # States (as str) that we have already identified as losing
        self._losing_states: Set[str] = set()
        self.test_deck = test_deck
        self.n_states_checked = 1
        self.n_deal = 1
        self.n_move_card_in_tableau = 0
        self.n_move_to_foundation = 0
        self.n_no_move_possible = 0
        self._max_states = max_states
        self.deck_filename = deck_filename
        self.move_to_empty_pile = move_to_empty_pile
        self.move_same_suit = move_same_suit
        self.print_states = print_states
        self.track_threshold = track_threshold
        self.split_runs = split_runs
        self.max_depth = 0   # maximum depth of the search tree
        # Current depth of the search tree (i.e., number moves played to reach
        # the current state. Does not count moves played where search had to
        # backtrack.
        self.current_depth = 0
        self.face_up = face_up
        self._check_for_loops = (split_runs
             or move_to_empty_pile != 'none')
        #self._face_up = True
        self.maximize_score = maximize_score
        self.max_score = 1   # maximum score found
        #self.move_from_same_suit = move_from_same_suit
        #move_from_same_suit : boolean, optional
        #    Allow moving a pile off of the same suit. For example,
        #    when True (default), will allow moving the three of clubs
        #    from under the four of clubs to under the four of spades in
        #    the tableau.
        self._enum_to_empty_pile = _empty_rule_str_to_enum(
            self.move_to_empty_pile)
        self.split_empty_stock=_empty_rule_to_split_empty_stock(
            self.move_to_empty_pile)

        if self.test_deck == 0:
            if not self.deck_filename:
                self._initialize_deck()
            else:
                self._initialize_deck_from_file(self.deck_filename)
        else:
            self._initialize_test_deck(self.test_deck)

    def __repr__(self) -> str:
        return (f'move_same_suit:{self.move_same_suit}\n'
               f'Deck:{self._deck}\nStates:\n{self._curr_state}')

    def print_history(self) -> str:
        """Print history for a won or stopped game.

        Return a string that contains the history of the game through
        the current state. Because there is currently no way to play the
        game one move at a time, the only games where the state after
        `Agnes.play` is executed that will show moves are winning games
        or games that were stopped due to `Agnes.max_states` being exceeded.

        A -1 in the foundation indicates no card has yet been played in the
        column. Tableau piles are presented horizontally instead of
        vertically as 'T0' - 'T6', where cards on the right side of the
        line can be played, and a '|' separates hidden cards and exposed
        cards in each tableau pile.

        Cards are represented as in input decks as '(rank, suit)', where
        rank is 0–12 and suit is 0–3, where suits 0 and 2 are the same
        color, as are suits 1 and 3. The normalized cards are printed, ie,
        all cards have a number subtracted from their rank so that the base
        card has rank 0.

        Returns
        -------
        A string as described above.

        Notes
        -----
        Because the `Agnes` object has to construct the states by undoing
        moves, a deepcopy of the object is made before starting. This also
        (unnecessarily) copies the perhaps quite large `_losing_states`
        attribute. Therefore, it is probably best to use this only for
        debugging rather than printing the history for all winners.
        """
        states: list[_AgnesState] = []
        # inefficient, since losing_states set may be quite large, but we
        # expect to only do once for each winning game
        # a copy is needed because making/undoing moves changes the
        # current state stored in the `Agnes` object.
        copyself: Agnes = copy.deepcopy(self)
        # do not iterate over enumerate(...) since _moves is being modified
        for move_index in range(0, len(copyself._moves)): # pylint: disable=protected-access
            states.append(copy.deepcopy(copyself._curr_state)) #pylint: disable=protected-access
            copyself._undo_move(no_print=True)                 #pylint: disable=protected-access
            copyself._curr_state.set_valid_moves(self._enum_to_empty_pile, #pylint: disable=protected-access
                self.move_same_suit, self.split_empty_stock,
                self.track_threshold, self._all_lmi[-(move_index+1)])

        # Get the initial state also
        states.append(copy.deepcopy(copyself._curr_state)) # pylint: disable=protected-access
        return str(list(reversed(states)))

    # Print the deck used in a simple text format
    def export_deck(self, filename: str) -> None:
        """Export the deck to a text file.

        Write one card per line as (rank, suit) where suit is 0, 1, 2, or 3,
        and rank is 0, 1, ..., 12. Note this this is the deck as input
        using the `deck_filename` parameter or as randomly generated
        the deck is standardized to have a base card of 0 for internal
        used. The standardized cards are displayed in the
        `Agnes.print_history` or `print_states` functions.

        Arguments
        ---------
        filename: str
            Output filename

        Returns
        -------
        None
        """
        outstr=''
        #for card in self._initial_deck:
            #outstr += '({:2d}, {:d})\n'.format( card[_RANK], card[_SUIT])
        outstr = '\n'.join([ f'({card.rank:2d}, {card.suit:d})'
                             for card in self._initial_deck])
        f = open(filename, 'w', encoding='utf-8')
        f.write(outstr)
        f.write('\n')
        f.close()

    def _initialize_deck_from_file(self, filename: str) -> None:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self._initial_deck = []
        line_number = 0
        dupset=set()
        for line in lines:
            line_number += 1
            stripped = line.rstrip()
            hasparen = stripped.startswith('(') and stripped.endswith(')')
            noparen = stripped.strip('()')
            rank, suit = noparen.split(',')
            rank = rank.strip()
            suit = suit.strip()
            # [20240314RG]: bug fix, was using 'suit.isdigit' instead of
            # 'suit.isdigit()'
            if (not hasparen or not rank.isdigit() or not suit.isdigit()
                   or int(rank)>12 or int(suit)>3):
                raise ValueError('Lines in deck_filename should be of the '
                   "form '(rank, suit)' where rank is in 0..12 and suit is "
                   f'in 0..3. Found: {stripped} (line {line_number})')
            card = Card(rank=int(rank), suit=int(suit))
            if card in dupset:
                raise ValueError('Duplicate card in deck '
                                 f'found on line {line_number}')
            else:
                dupset.add(card)
            self._initial_deck.append(card)
        if line_number != 52:
            raise ValueError('52 lines in deck_filename '
                             f'expected. Found: {line_number}')

    # Set the maximum number of cards that can be moved in a given pile.
    def _initialize_deck(self) -> None:
        self._initial_deck = []
        for rank in range(0, 13):           # Ranks: 0-12
            for suit in range(0,4):                        # Suits: 0-3
                self._initial_deck.append(Card(rank=rank, suit=suit))
        random.shuffle(self._initial_deck)
        self._initial_deck.reverse()

    #  Winning
    def _initialize_test_deck(self, test_deck: int) -> None:
        if test_deck == 1:
            win_base = [(6, 2)]
            win_row1 = [(9, 1),(5, 1),(7, 3),(5, 3),(3, 3),(9, 0),(5, 0)]
            win_row2 =        [(12,2),(2, 1),(6, 0),(4, 2),(13,3),(2, 2)]
            win_row3 =               [(8, 1),(4, 3),(7, 0),(8, 2),(3, 2)]
            win_row4 =                      [(10,0),(1, 3),(11,1),(8, 0)]
            win_row5 =                             [(13,1),(9, 3),(4, 0)]
            win_row6 =                                    [(9, 2),(1, 1)]
            win_row7 =                                           [(7, 1)]
            win_stock1 = [(6, 3),(11,2),(5, 2),(3, 0),(2, 0),(11,0),(13,0)]
            win_stock2 = [(10,3),(3, 1),(8, 3),(1, 0),(10,1),(11,3),(7, 2)]
            win_stock3 = [(12,0),(10,2),(4, 1),(12,3),(12,1),(6, 1),(13,2)]
            win_stock4 = [(1, 2),(2, 3)]
        elif test_deck != 0:
            raise ValueError('test_deck takes values 0 (default: use random '
                'deck), 1 (wins)')

        # Make a list of lists representing the deck
        temp_deck = [win_base, win_row1, win_row2, win_row3, win_row4,
                     win_row5, win_row6, win_row7, win_stock1, win_stock2,
                     win_stock3, win_stock4]

        # Flatten the list of lists
        for x in temp_deck:
            for y in x:
                self._initial_deck.append(Card(rank=y[0], suit=y[1]))

    def play(self) -> int:
        """Play the game of Agnes and return integer status.

        Parameters
        ----------
        None

        Returns
        -------
        An integer with the following meanings:
            1: Won
            2: Lost
            3: Terminated because number of states created exceeds
               max_states
        """

        first_state = self._curr_state
        last_move_info: list[LastMoveInfo] = []
        for i in range(0, 7):
            last_move_info.append(LastMoveInfo())

        # Reset the indexing of all cards so base card has rank 0
        self._deck = []
        for i in range(0, 13*4):
            self._deck.append(Card(rank=(self._initial_deck[i].rank
                                - self._initial_deck[0].rank) % 13,
                                   suit=self._initial_deck[i].suit))
        first_state.set_last_cards(self._deck)
        # Deal base card to foundation
        first_state.play_base_card(self._deck[0])

        snm_opts: SetNMovableOpts = SetNMovableOpts(
            move_same_suit=self.move_same_suit, split_runs=self.split_runs,
            split_empty_stock=self.split_empty_stock)

        # Deal next cards to Tableau
        for i in range(0,7):
            for j in range(i,7):
                first_state.deal_onto_pile(pile_index=j, deck=self._deck,
                    face_up=bool(self.face_up or j == i))

        for i in range(0,7):
            first_state.set_n_movable(i, snm_opts)

        self._all_lmi.append(last_move_info)
        first_state.set_valid_moves(self._enum_to_empty_pile,
            self.move_same_suit, self.split_empty_stock,
            self.track_threshold, self._all_lmi[-1])

        #print(first_state)
        self._all_valid_moves = [first_state.valid_moves]
        done = 0
        if self.print_states:
            print(first_state)
            print(self._lmi_to_str())
        if (self._enum_to_empty_pile == EmptyRule.NONE
                and not self.maximize_score
                and first_state.any_pile_blocked()):
            return 2
        else:
            while done == 0:
                done = self._perform_move()
                if self.print_states:
                    print(self._curr_state)
                    print(self._lmi_to_str())
            self.current_depth = self._curr_state.depth
            return done

    def _undo_move(self, no_print: bool) -> None:
        """Undo last move (last item in `_moves` stack).

        The three-step process when executing a move is described in the
        docstring of `_perform_move`. This function reverses step (1)
        by manually resetting the attributes and step (3) (by popping the
        last items from the stack. Step (2) is not reversed as the counters
        that were updated were meant to be cumulative.

        Parameters
        ----------
        no_print : bool
            Do not print 'Undo move' to standard output, even if
            `self.print_states = True`. Without this parameter, the
            function `Agnes.print_history` would print 'Undo move' as it
            unwinds the game play to show the history of winning moves.

        Returns
        -------
        None
        """

        if self.print_states and not no_print: print('Undo move')
        new_state = self._curr_state
        curr_move = self._moves.pop()
        snm_opts: SetNMovableOpts = SetNMovableOpts(
            move_same_suit=self.move_same_suit, split_runs=self.split_runs,
            split_empty_stock=self.split_empty_stock)
        self._all_valid_moves.pop()
        self._all_lmi.pop()
        if self._check_for_loops and not no_print:
            if not new_state.is_loop:
                self._check_loops.remove(new_state.hash_str)
        new_state.depth = new_state.depth - 1

        new_state.is_loop = False
        new_state.is_loser = False

        if curr_move is None:
            raise ValueError('_undo_move: curr_move should not be None')
        elif isinstance(curr_move, MoveToFound):
            last_card: Card = Card(new_state.foundation[curr_move.suit],
                                   curr_move.suit)
            if curr_move.tabltype == TablType.NONE:
                new_state.in_suit_seq[last_card.rank][last_card.suit] = False
            if new_state.piles[curr_move.from_].exposed:
                card_to_hide: Card = new_state.piles[
                    curr_move.from_].exposed[-1]
                new_state.last_in_pile[card_to_hide.rank][
                    card_to_hide.suit] = False

            # if we exposed a card when we moved the card beneath it to the
            # foundation, turn it back over before moving the card back from
            # the foundation
            if curr_move.expose:
                new_state.piles[curr_move.from_].hidden.append(
                    new_state.piles[curr_move.from_].exposed.pop())
            # now move the card back from the foundation

            new_state.piles[curr_move.from_].exposed.append(
                Card(rank=new_state.foundation[curr_move.suit],
                     suit=curr_move.suit))
            new_state.foundation[curr_move.suit] -= 1
            new_state.set_n_movable(curr_move.from_, snm_opts)
            if len(new_state.piles[curr_move.from_].exposed) == 1:
                new_state.set_sort_order(self._enum_to_empty_pile)
        elif isinstance(curr_move, DealMove):
            # Deal from stock
            if new_state.n_stock_left == 0:
                # Put two cards back on deck and remove them from the tableau
                new_state.undo_deal_for_pile(0)
                new_state.undo_deal_for_pile(1)
                # set_n_movable depends on whether n_stock_left>0, so need
                # to call it for all piles, not just the first two
                for pile_index in range(0,7):
                    new_state.set_n_movable(pile_index, snm_opts)
            else:
                for pile_index, _ in enumerate(new_state.piles):
                    new_state.undo_deal_for_pile(pile_index)
                for i in range(0, 7):
                    new_state.set_n_movable(i, snm_opts)
            for i in range(0, 7):
                new_state.pile_sort_info[i].n_stock_left = (
                    new_state.n_stock_left)
            new_state.set_sort_order(self._enum_to_empty_pile)
        elif isinstance(curr_move, TablMove):
            # since we are undoing the move here, the curr_move.to_ pile
            #  is now the one we are moving the run from
            from_pile = new_state.piles[curr_move.to_].exposed
            to_pile = new_state.piles[curr_move.from_].exposed
            top_card = from_pile[-curr_move.n_cards]
            if curr_move.tabltype == TablType.JOIN:
                new_state.in_suit_seq[top_card.rank][top_card.suit] = False
            elif curr_move.tabltype == TablType.SPLIT:
                new_state.in_suit_seq[top_card.rank][top_card.suit] = True

            if len(from_pile) != curr_move.n_cards:
                prev_card = from_pile[-1*(curr_move.n_cards + 1)]
                new_state.last_in_pile[prev_card.rank][prev_card.suit] = True
            if to_pile:
                new_state.last_in_pile[to_pile[-1].rank][
                    to_pile[-1].suit] = False

            # if we exposed a card when we moved the pile, turn it back over
            # before moving the pile back
            pre_from_size = len(new_state.piles[curr_move.from_].exposed)
            if curr_move.expose:
                new_state.piles[curr_move.from_].hidden.append(
                    new_state.piles[curr_move.from_].exposed.pop())
            # now move the pile back
            for n_to_pop in range(-1*curr_move.n_cards,0):
                new_state.piles[curr_move.from_].exposed.append(
                    new_state.piles[curr_move.to_].exposed.pop(n_to_pop)
                    )
            new_state.set_n_movable(curr_move.from_, snm_opts)
            new_state.set_n_movable(curr_move.to_, snm_opts)
            if (not new_state.piles[curr_move.to_].exposed
                    or pre_from_size == 0):
                new_state.set_sort_order(self._enum_to_empty_pile)

        new_state.update_hash_str()

        if self._moves:
            new_state.curr_move = self._moves[-1]
        else:
            new_state.curr_move = None
        # [20240315RG] bug fix for printing
        new_state.valid_moves = self._all_valid_moves[-1]

    def _perform_move(self) -> int:
        """Perform a move. Call _undo_move if no possible move.

        To make a move, update:
            (1) the appropriate attributes of `self._curr_state`
                (`exposed`, `hidden`, `n_stock_left`, `foundation`,
                 `last_in_pile`, `in_suit_seq`)
            (2) any counters in `self` that count the various types of
                moves made (`n_move_to_foundation`,`n_deal`,
                `n_move_card_in_tableau`).
            (3) append to the stacks that track the evolution of the
                game:` _moves`, `_all_valid_moves`, `_check_loop_states`,
                `_all_lmi`.  While we could have used a single stack to
                manage these three items, we intentionally do not maintain
                a stack of _AgnesState objects. This would simplify the code
                (eg, `_undo_move` could be replaced with popping the last
                state) but increases the run-time.

        Arguments
        ---------
        None

        Returns
        -------
        Integer with the values:
           0 if there were no valid moves, but depth > 0 so _undo_move was
             called, OR there was a valid move so it was made, but it didn't
             result in a win.
           1 if game is won (there was a valid move, it was made, and the
             game was won)
           2 if game is lost (no valid moves, and depth == 0)
           3 if self.n_states_checked > self._max_states and
             self._max_states>0

        """
        self.n_states_checked += 1

        snm_opts: SetNMovableOpts = SetNMovableOpts(
            move_same_suit=self.move_same_suit, split_runs=self.split_runs,
            split_empty_stock=self.split_empty_stock)

        if self._curr_state.depth > self.max_depth:
            self.max_depth = self._curr_state.depth

        if self._max_states > 0 and self.n_states_checked>self._max_states:
            #print(f'Terminated at {self.n_states_checked} moves', flush=True)
            return 3

        # Check the score and whether it's greater than the max score
        valid_moves = self._all_valid_moves[-1]
        won_game = False
        any_pile_blocked = False

        # Lost the game!
        if (self._curr_state.depth == 0 and not valid_moves):
            self.n_no_move_possible += 1
            return 2
        elif not valid_moves:
            # keep track of states that we know are losers
            if (self._curr_state.n_stock_left >= self.track_threshold
                    and not self._curr_state.is_loser):
                self._losing_states.add(self._curr_state.hash_str)
            self.n_no_move_possible += 1
            self._undo_move(no_print=False)
            return 0
        else:
            # Make a move
            curr_move = valid_moves.pop()
            new_state = self._curr_state
            new_state.curr_move = curr_move
            self._all_lmi.append(copy.deepcopy(self._all_lmi[-1]))
            last_move_info = self._all_lmi[-1]
            new_state.depth += 1
            if isinstance(curr_move, MoveToFound):
                last_card = new_state.piles[curr_move.from_].exposed.pop()
                if curr_move.expose:
                    new_state.piles[curr_move.from_].exposed.append(
                        new_state.piles[curr_move.from_].hidden.pop())
                if new_state.piles[curr_move.from_].exposed:
                    new_last = new_state.piles[curr_move.from_].exposed[-1]
                    new_state.last_in_pile[new_last.rank][new_last.suit] = True
                new_state.foundation[last_card.suit] += 1
                self.n_move_to_foundation += 1
                # +4 here because -1 represents no card in pile
                score = sum(new_state.foundation)+4
                if score > self.max_score:
                    self.max_score = score
                if score == 52: won_game = True
                new_state.set_n_movable(curr_move.from_, snm_opts)
                last_move_info[curr_move.from_] = LastMoveInfo(depth = 0,
                    n_moved = 0, moved_to = False, can_move_to_found = True)
                if curr_move.tabltype == TablType.NONE:
                    new_state.in_suit_seq[last_card.rank][last_card.suit] = (
                        True)
                if not new_state.piles[curr_move.from_].exposed:
                    new_state.set_sort_order(self._enum_to_empty_pile)
            elif isinstance(curr_move, DealMove):
                # Deal from stock
                if new_state.n_stock_left == 2:
                    new_state.deal_onto_pile(0, self._deck, True)
                    new_state.deal_onto_pile(1, self._deck, True)
                    # set_n_movable depends on whether n_stock_left>0, so need
                    # to call it for all piles, not just the first two
                    for pile_index in range(0,7):
                        new_state.set_n_movable(pile_index, snm_opts)
                    last_move_info[0] = LastMoveInfo(depth = 0, n_moved = 0,
                        moved_to = False, can_move_to_found = True)
                    last_move_info[1] = LastMoveInfo(depth = 0, n_moved = 0,
                        moved_to = False, can_move_to_found = True)
                else:
                    for pile_index in range(0,7):
                        new_state.deal_onto_pile(pile_index, self._deck, True)
                    for pile_index in range(0,7):
                        new_state.set_n_movable(pile_index, snm_opts)
                        last_move_info[pile_index] = LastMoveInfo(depth = 0,
                            n_moved = 0, moved_to = False,
                            can_move_to_found = True)

                # If move_to_empty_pile == 'none', then our trick of speeding
                # up run-time by seeing if any lower cards are blocked by
                # the highest card won't work, because the highest card
                # could be moved to an empty pile
                if (self._enum_to_empty_pile == EmptyRule.NONE
                        and not self.maximize_score):
                    any_pile_blocked = new_state.any_pile_blocked()
                self.n_deal += 1
                # When undoing move, always update sort order, because it does
                # not seem worth it to check if any pile is being emptied
                for i in range(0, 7):
                    new_state.pile_sort_info[i].n_stock_left = (
                        new_state.n_stock_left)
                new_state.set_sort_order(self._enum_to_empty_pile)
            elif isinstance(curr_move, TablMove):
                self.n_move_card_in_tableau += 1
                from_pile = new_state.piles[curr_move.from_].exposed
                to_pile = new_state.piles[curr_move.to_].exposed
                if len(from_pile) != curr_move.n_cards:
                    last_card = from_pile[-1 *(curr_move.n_cards+1)]
                    new_state.last_in_pile[last_card.rank][last_card.suit] = (
                        True)
                if to_pile:
                    new_state.last_in_pile[to_pile[-1].rank][
                        to_pile[-1].suit] = False
                top_card = from_pile[-1*curr_move.n_cards]
                if curr_move.tabltype == TablType.JOIN:
                    new_state.in_suit_seq[top_card.rank][top_card.suit] = True
                elif curr_move.tabltype == TablType.SPLIT:
                    new_state.in_suit_seq[top_card.rank][top_card.suit] = False

                last_card = from_pile[-1]
                last_move_info[curr_move.from_] = LastMoveInfo(
                    depth = new_state.depth, n_moved = curr_move.n_cards,
                    moved_to = False,
                    can_move_to_found = True)
                last_move_info[curr_move.to_] = LastMoveInfo(
                    depth = new_state.depth, n_moved = curr_move.n_cards,
                    moved_to = True,
                    can_move_to_found = (
                       not (new_state.foundation[last_card.suit]
                            == (last_card.rank - 1))))

                size_tgt_pre = len(new_state.piles[curr_move.to_].exposed)
                for n_to_pop in range(-1*curr_move.n_cards,0):
                    new_state.piles[curr_move.to_].exposed.append(
                        new_state.piles[curr_move.from_].exposed.pop(n_to_pop)
                        )
                if curr_move.expose:
                    new_state.piles[curr_move.from_].exposed.append(
                        new_state.piles[curr_move.from_].hidden.pop())
                new_state.set_n_movable(curr_move.from_, snm_opts)
                new_state.set_n_movable(curr_move.to_, snm_opts)
                if (not new_state.piles[curr_move.from_].exposed
                        or size_tgt_pre == 0):
                    new_state.set_sort_order(self._enum_to_empty_pile)
            else:
                raise TypeError(f'curr_move is {curr_move}')

            new_state.update_hash_str()
            new_state.is_loop = False
            new_state.is_loser = False
            if self._check_for_loops:
                # Unlike other languages, Python doesn't give a return code
                # indicating whether item was already in the set, but we can
                # determine by getting the length before and after (O(1) time)
                len_before = len(self._check_loops)
                self._check_loops.add(new_state.hash_str)
                if len_before == len(self._check_loops):
                    new_state.is_loop = True

            #------------------------------------------------------------------
            # It's possible we've already evaluated that this state is losing.
            # Consider the case where there are two possible independent moves
            # (M1: Move 1 card from Pile 1 to 2, M2: move 1 card from pile 5
            # to 6). Once you check that M1->M2 doesn't win, no need to check
            # M2->M1
            #------------------------------------------------------------------
            if new_state.is_loop:
                if self.print_states:
                    print('New state is a loop, '
                          'so setting valid_moves to empty')
                new_state.valid_moves = []
            elif (self._curr_state.n_stock_left >= self.track_threshold
                and (new_state.hash_str in self._losing_states)):
                new_state.is_loser = True
                new_state.valid_moves = []
                if self.print_states:
                    print('Already checked the new state, '
                          'so setting valid_moves to empty')
            elif (self._enum_to_empty_pile == EmptyRule.NONE
                    and any_pile_blocked):
                if self.print_states:
                    print('New state is a block, '
                          'so setting valid_moves to empty')
                new_state.valid_moves = []
            else:
                new_state.set_valid_moves(self._enum_to_empty_pile,
                    self.move_same_suit, self.split_empty_stock,
                    self.track_threshold, self._all_lmi[-1])

            if won_game:
                self._moves.append(curr_move)
                self._all_valid_moves.append([])
                return 1
            elif not new_state.valid_moves:
                self._all_valid_moves.append([])
                self._moves.append(curr_move)
            else:
                self._all_valid_moves.append(new_state.valid_moves)
                self._moves.append(curr_move)

            return 0

    def _lmi_to_str(self) -> str:
        lmi_top: list[LastMoveInfo] = self._all_lmi[-1]
        retlist = []
        for item in lmi_top:
            if item.moved_to:
                mt = 'T'
            else:
                mt = 'F'
            if item.can_move_to_found:
                t_or_f = 'T'
            else:
                t_or_f = 'F'
            retlist.append(f'{item.depth}-{item.n_moved}-{mt}-{t_or_f}')
        return f"Last move info:[{', '.join(retlist)}]"


#------------------------------------------------------------------------------
# AgnesState class - represents a state in the game.
#------------------------------------------------------------------------------
class _AgnesState:
    """Represent a state in the game.

    Attributes:
    -----------
    depth : int
        The number of moves played to reach the state.
    n_stock_left : int
        Number of cards remaining in the stock.
    piles : tuple(AgnesPile) (7-tuple)
        7-tuple representing the 7 tableau piles
    found : list[int]
        List of size four representing the top card in each of the four
        foundations. A value of -1 indicates no card in the foundation.
    curr_move : list[int]
        Last move played to reach this state
    valid_moves : list[AgnesMove]
        List of valid moves for this state. It is initialized when the state
        is created and then moves are popped off as they are tried.
    force_move : Optional[AgnesMove]
        Move that will be forced. This will override the list of
        valid moves. For example, moving a card from the tableau to an
        empty foundation pile may be forced. See `set_valid_states`
        for details.
    in_suit_seq : list[list[bool]]
        True for a given card if the card is in an exposed pile in sequence
        under a card of the same suit or is in the foundation. Access
        as: in_suit_seq[card.rank][card.suit].
    last_in_pile : list[list[bool]]
        True for a given card if the card is the last card in an exposed
        pile (ie, first available for play) or is in the foundation.
        Access as: last_in_pile[card.rank][card.suit].
    hash_str : str
        Somewhat compressed representation of the cards left in the stock and
        and tableau cards. This will be stored in the sets that check for
        loops and previously losing states.
    lower_last : Card
        The lower-ranked of the two last cards in the deck.
    upper_last : Card
        The higher-ranked of the two last cards in the deck.
    last_same_suit_seq : bool
        True if lower_last and upper_last are the same suit and in order.
    last_same_color_not_suit : bool
        True if lower_last and upper_last are the same color and not the
        same suit.
    """
    # default constructor
    def __init__(self) -> None:
        self.depth = 0
        self.n_stock_left = 52
        # Exposed and hidden cards in tableau.
        self.piles: tuple[AgnesPile, ...] = (AgnesPile([], [], []),
            AgnesPile([], [], []), AgnesPile([], [], []),
            AgnesPile([], [], []), AgnesPile([], [], []),
            AgnesPile([], [], []), AgnesPile([], [], []))
        self.foundation = [-1, -1, -1, -1]
        self.curr_move: Optional[AgnesMove] = None
        self.valid_moves: list[Optional[AgnesMove]] = []
        #self.force_move: list[Optional[AgnesMove]] = []
        self.is_loop = False
        self.is_loser = False
        self.in_suit_seq: list[list[bool]] = []
        self.last_in_pile: list[list[bool]] = []
        self.hash_str: str = ''
        for _ in range(0, 13):
            self.in_suit_seq.append([False, False, False, False])
            self.last_in_pile.append([False, False, False, False])
        self.pile_sort_info: list[PileSortInfo] = []
        self.sort_order: list[int] = [0, 1, 2, 3, 4, 5, 6]
        self.lower_last: Card = Card(0, 0)
        self.upper_last: Card = Card(0, 0)
        self.last_same_suit_seq: bool = False
        self.last_same_color_not_suit: bool = False

        for pile_index in range(0, 7):
            self.pile_sort_info.append(PileSortInfo(pile_index = pile_index,
                pile = self.piles[pile_index], n_stock_left = 52))
            self.sort_order[pile_index] = pile_index

    # String representation of object (print() will use this)
    #def vertstr(self) -> str:
    #    str1 = (f'\nMove: {_describe_move(self.curr_move)}\n\n'
    #        f'depth:{self.depth}, n_stock_left:{self.n_stock_left}, '
    #        f'valid_moves:{self.valid_moves}\n')
    #
    #    foundlist=[]
    #    for i, value in self.foundation:
    #        if value == -1:
    #            foundlist.append('  ')
    #        else
    #            foundlist.append(Card(rank=value, suit=suit).twochar())
    #    str2 = 'Foundations:' + ' '.join(foundlist)

    def __repr__(self) -> str:
        return (f'\nMove: {_describe_move(self.curr_move)}\n\n'
            f'piles:{self.struncomp()}\n'
        ##    f'hash_str:{self.hash_str}\n'
        ##    f'sort_order:{self.sort_order}\n'
        ##    f'n_movable:{[item.n_movable for item in self.piles]}\n'
            f'depth:{self.depth}, n_stock_left:{self.n_stock_left}, '
            f'valid_moves:{self.valid_moves}\nFoundations:{self.foundation}\n'
            f'T0:{self.piles[0].hidden} | {self.piles[0].exposed}\n'
            f'T1:{self.piles[1].hidden} | {self.piles[1].exposed}\n'
            f'T2:{self.piles[2].hidden} | {self.piles[2].exposed}\n'
            f'T3:{self.piles[3].hidden} | {self.piles[3].exposed}\n'
            f'T4:{self.piles[4].hidden} | {self.piles[4].exposed}\n'
            f'T5:{self.piles[5].hidden} | {self.piles[5].exposed}\n'
            f'T6:{self.piles[6].hidden} | {self.piles[6].exposed}\n'
            f'in_suit_seq:{self._print_in_suit_seq()}\n'
            f'last_in_pile:{self._print_last_in_pile()}\n'
            )

    def _print_in_suit_seq(self) -> str:
        '''Print in_suit_seq bool attribute as 0s and 1s.

        Space is used to separate the nested lists.
        '''
        outlist = []
        for suit_list in self.in_suit_seq:
            suitlist = []
            for suit in suit_list:
                if suit:
                    suitlist.append('1')
                else:
                    suitlist.append('0')
            outlist.append(''.join(suitlist))
        return ' '.join(outlist)

    def _print_last_in_pile(self) -> str:
        '''Print last_in_pile bool attribute as 0s and 1s.

        Space is used to separate the nested lists.
        '''
        outlist = []
        for suit_list in self.last_in_pile:
            suitlist = []
            for suit in suit_list:
                if suit:
                    suitlist.append('1')
                else:
                    suitlist.append('0')
            outlist.append(''.join(suitlist))
        return ' '.join(outlist)

    def update_hash_str(self) -> None:
        """Compressed string representation of the state.
        """
        retlist = [str(chr(self.n_stock_left))]
        for pile_index in range(0, 7):
            pile = self.piles[self.sort_order[pile_index]]  # 20240413: add
            retlist.append(_strpilecomp(pile.exposed))
            retlist.append(_strpilecomp(pile.hidden))
        self.hash_str = '-'.join(retlist)

    def struncomp(self) -> str:
        """Uncompressed string representation of the state.
        """
        retlist = [str(self.n_stock_left)]
        for pile in self.piles:
            retlist.append(_strpileuncomp(pile.exposed))
            retlist.append(_strpileuncomp(pile.hidden))
        return ''.join(retlist)

    # Uncomment to print format similar to, but not identical to v0.6 (ie,
    # format of moves is different. For use when `Agnes.face_up` is True.
    #
    #def __repr__(self) -> str:
    #    return (f'\nMove: {_describe_move(self.curr_move)}\n\n'
    #        f'depth:{self.depth}, n_stock_left:{self.n_stock_left}, '
    #        f'valid_moves:{self.valid_moves}\nFoundations:{self.foundation}\n'
    #        f'T0:{self.exposed[0]}\nT1:{self.exposed[1]}\n'
    #        f'T2:{self.exposed[2]}\nT3:{self.exposed[3]}\n'
    #        f'T4:{self.exposed[4]}\nT5:{self.exposed[5]}\n'
    #        f'T6:{self.exposed[6]}\n')

    def set_n_movable(self, pile_index: int,
                      snm_opts: SetNMovableOpts) -> None:
        """Set self.piles[pile_index].n_movable.

        Note this just checks the number of cards from the bottom of the
        pile than can be moved according to the rules. It does not check
        whether there is somewhere the selected set of cards can be moved
        to. The latter is done in `set_valid_moves`.

        It sets the number cards from the bottom of the pile that can be
        moved according to the `move_same_suit` and `split_runs` parameter.

        While doing so, it also applies additional optimizations
        when the stock is empty and `split_empty_stock` is false about
        whether to allow splitting a run between two cards of the same
        suit (even when `split_runs` is True). Namely:
          (1) If runs are moved by color, such splits are never allowed.
          (2) If runs are moved by suit, such splits are not allowed
          if it is certain the last card in the pile being moved is not
          needed as a move target for the suit of the same color (ie,
          if Card(last_card.rank - 1, last_card.same_color_suit) is
          in the foundation or can be forced to the foundation, the split is
          not allowed. [However, this second condition is implemented in
          set_valid_moves rather than here, because this function is only
          called when piles are touched and it's possible an operation on a
          different pile activated or deactivated condition (2).

        Because the function checks whether `self.n_stock_left == 0`, it
        must be called for all piles when the stock is made empty (or such
        a move undone). The call must follow updating of all piles.

        Arguments
        ---------
        pile_index : int
            Index of the pile to check
        snm_opts : SetNMovableOpts
            Tuple holding `Agnes` parameter values `move_same_suit`,
            `split_runs`, and `split_empty_stock`.

        Returns
        -------
        List of integers with number of cards that can be moved from a
        pile.
        """
        pile = self.piles[pile_index].exposed
        self.piles[pile_index].n_movable.clear()
        #whole_suit_seq: bool = True
        if pile:
            for card_index, card in enumerate(reversed(pile)):
                try:
                    #above_card = pile[card_index + 1]
                    above_card = pile[-1 - card_index - 1]
                except IndexError:
                    above_card = None

                # the next two if statements verify that the card starts a
                # sequence of the same color
                if not card.rank - card_index == pile[-1].rank:
                    #whole_suit_seq = False
                    break

                if not card.suit == pile[-1].suit:
                    #whole_suit_seq = False
                    if (snm_opts.move_same_suit
                            or (card.suit % 2) != (pile[-1].suit % 2)):
                        break

                if above_card:
                    is_split_same_suit = (above_card.rank == card.rank + 1
                        and above_card.suit == card.suit)
                    is_split_same_color = (above_card.rank == card.rank + 1
                        and (above_card.suit - card.suit) % 2 == 0)
                else:
                    is_split_same_suit = False
                    is_split_same_color = False

                # Lastly, only add to n_movable if we are allowed to split
                # runs (conditional line 1) or the move is not splitting a run
                # (remaining lines of conditional).
                #--------------------------------------------------------------
                if (snm_opts.split_runs
                        or (snm_opts.move_same_suit
                            and not is_split_same_suit)
                        or (not snm_opts.move_same_suit
                            and not is_split_same_color)):
                    # 20240413 - add check in foundation when move_same_suit
                    #---------------------------------------------------------
                    # But... we should also never split between the same suit
                    # in sequence when the stock is 0 and split_empty_stock is
                    # false: (1) when we are moving by suit, we forbid the
                    # split as long as we can be sure we won't need to move
                    # the other suit onto the pile; (2) when moving by color,
                    # never need to split runs
                    #----------------------------------------------------------
                    if (self.n_stock_left == 0
                            and not snm_opts.split_empty_stock
                            and ((not snm_opts.move_same_suit
                                    and is_split_same_suit))):
                        continue
                    self.piles[pile_index].n_movable.append(card_index + 1)

    def undo_deal_for_pile(self, pile_index: int) -> None:
        """Undo deal of one card for pile identified by pile_index.

        Set `in_suit_seq` and `last_in_pile` = False for the card being
        undealt. If there is a card above this that will be now last,
        set `last_in_pile` to True for that card. Pop the last card
        from `piles[pile_index].exposed` and increase `n_stock_left` by 1.

        Unlike deal_onto_pile, we don't need to handle face-down deals
        because we never undo them.

        Attributes
        ----------
        pile_index : int
            Index of the pile for which the deal is undone
        """
        pile = self.piles[pile_index].exposed
        last_card = pile[-1]
        self.in_suit_seq[last_card.rank][last_card.suit] = False
        self.last_in_pile[last_card.rank][last_card.suit] = False
        pile.pop()
        if pile:
            new_last_card: Card = pile[-1]
            self.last_in_pile[new_last_card.rank][new_last_card.suit] = True
        self.n_stock_left += 1

  # Deal a single card from stock onto the pile identified by pile_index
    def deal_onto_pile(self, pile_index: int, deck: list[Card],
                       face_up: bool) -> None:
        """Deal a card from the stock onto the pile with index pile_index.

        Set `last_in_pile` = True for the card being dealt and set
        `last_in_pile` = False for the card now covered by the deal (if
        one exists). Set `in_suit_seq = True` for the dealt card if the card
        happened to be dealt in sequence under a card of the same suit
        in the exposed pile.  Card dealt is appended to the end of the
        `exposed` pile if `face_up = True` and the `hidden` pile otherwise.
        Decrease `n_stock_left` by 1.

        Attributes
        ----------
        pile_index : int
            Pile being dealt to.
        deck : list[Card]
            Deck from which we are dealing.
        face_up : bool
            Indicates whether card is dealt face-up (and put in the
            self.piles[pile_index].exposed pile) or face-down (and put
            in the .hidden pile).
        """
        card: Card = deck[52 - self.n_stock_left]
        if face_up:
            if self.piles[pile_index].exposed:
                last_card = self.piles[pile_index].exposed[-1]
                if (card.rank + 1 == last_card.rank
                        and card.suit == last_card.suit):
                    self.in_suit_seq[card.rank][card.suit] = True
                self.last_in_pile[last_card.rank][last_card.suit] = False
            self.piles[pile_index].exposed.append(card)
            self.last_in_pile[card.rank][card.suit] = True
        else:
            self.piles[pile_index].hidden.append(card)
        self.n_stock_left = self.n_stock_left - 1

    def any_pile_blocked(self) -> bool:
        """Check if game is unwinnable after a deal.

        This should only be called if `Agnes.move_to_empty_pile=='none'`.
        Otherwise, the game might be winnable even though suits are
        blocked because the 'kings' can be moved to an empty pile to
        unblock the cards beneath them. (Here we use 'king' to refer to
        the highest-rank card.)

        Creates a graph indicating whether a given 'king' is covering in
        a pile a lower rank card of the same suit or a 'king' of another
        suit. If the graph has a cycle, the game cannot be won.

        Returns
        -------
        bool that is True if any pile or combination of piles blocks a win.
        """
        graph: AgnesGraph = {0: set(), 1: set(), 2: set(), 3: set()}
        for pile in self.piles:
            pile_both = pile.hidden + pile.exposed
            if pile_both:
                # Check for blocks
                king_found = [False, False, False, False]
                for current_card in reversed(pile_both):
                    if current_card.rank == 12:
                        king_found[current_card.suit] = True
                    for k in range(0, 4):    # loop over suits
                        if (king_found[k]
                                    and (current_card.rank < 12
                                         or current_card.suit != k)):
                            graph[k].add(current_card.suit)
        return _cyclic(graph)

    # Set self.validmoves with the three types of moves
    def set_valid_moves(self, enum_to_empty_pile: EmptyRule,
                        move_same_suit: bool, split_empty_stock: bool,
                        track_threshold: int,
                        last_move_info: list[LastMoveInfo]) -> None:
        """Set self.valid_moves to the valid moves available.

        Three types: DealMove()
                     TablMove(from_=, to_=, n_cards=, expose=, tabltype=)
                     MoveToFound(from_=, suit=, expose=, tabltype=)

        This function creates a list of all valid moves that can be done
        by seeing if a deal is available, which cards can be moved to which
        target piles, and which cards can be moved to the foundation.

        Various optimizations reduce the moves available. Forcing a move
        means this is the only move that can be played. Forced moves are
        designed to reduce the space of moves that need to be searched
        without changing the final score of the game. If more than one
        move meets the criteria to be forced, the last move is chosen.

        (1) If there are multiple empty piles that won't be covered by
        a future deal, only allow moves to the first pile.

        (2) If we are not using the `losing_states` set (track_threshold >
        `n_stock_left`), do not reverse a move (ie, move the same number
        of cards from one pile to another).

        (3) Force joins by suit sequence when the stock is empty and
        `split_empty_stock is False` if the same-color top card of the
        pile being moved satisfies (i) next lowest card is already in
        the foundation or (ii) `move_same_suit = False` and already under
        the next-highest card of the same suit or (iii)
        `move_same_suit = False` and next-highest card will be available
        to be played on after the move (last_in_pile or will be the new
        last card after the move from the current pile). For example,
        suppose we have a run starting with 4C that we might put under 5C.
        This move is forced if (i) 3S in foundation, or
        (ii) `move_same_suit = False` and 4S already under 5S, or
        (iii) `move_same_suit = False` and 5S is last in pile or we are
        moving the 4C from under the 5S.

        (4) Force move to foundation if (a) Card(rank - 2, same_color_suit)
        is already in the foundation or (b) stock is empty and
        `split_empty_stock = False` and Card(rank - 1, same_color_suit)
        is already under Card(rank, same_color_suit).

        (5) Force the last deal if the two dealt cards can immediately be
        forced to the foundation.

        (6) There are additional restrictions when the stock is empty for
        when a run can be split between two cards of the same suit, even
        when `split_runs=True`. When `move_same_suit is False`, the split
        is never allowed (enforced in the `set_n_movable` function). Otherwise,
        the split is allowed only if the last card in the pile being moved
        will never need to have the same-color suit added, which means
        Card(rank - 1, same_color_suit) is in the foundation or can be forced
        to the foundation [Card(rank - 2, same_color_suit in foundation), and
        Card(rank - 3, suit) in foundation] (where all ranks and suits refer to
        the last card of the pile being moved).

        Parameters
        ----------
        enum_to_empty_pile : EmptyRule
            `Agnes.move_to_empty_pile` parameter converted to enum.
        move_same_suit : bool
            `Agnes.move_same_suit` parameter
        split_empty_stock : bool
            `Agnes.split_empty_stock` attribute
        track_threshold : int
            `Agnes.track_threshold` attribute
        last_move_info : list[LastMoveInfo]
            The LastMoveInfo information for this state

        Returns
        -------
        None
        """
        self.valid_moves = []
        force_move: Optional[AgnesMove] = None

        # Deal (DealMove dataclass)
        if (self.n_stock_left > 2
                or (self.n_stock_left == 2
                    and (track_threshold <= 2
                        or not _dont_deal_last(last_move_info)))):
            self.valid_moves.append(DealMove())
            if self.is_deal_forced():
                force_move = DealMove()

        for pile_index, pile in enumerate(self.piles):
            exp_pile = pile.exposed
            len_exp_pile = len(pile.exposed)
            if len_exp_pile == 0: continue
            last_card = exp_pile[-1]
            tabltype: TablType = TablType.NONE
            # Moves in tableau (TablMove dataclass)
            #
            # Get a list of the number of cards that are movable
            # according to the input parameters. This does not yet consider
            # if there is a location the cards can be moved to.
            #n_movable = self.set_n_movable(pile_index, move_same_suit,
            #                                split_same_suit_runs)

            for n_to_move in pile.n_movable:
                tabltype = TablType.NONE
                src_in_next_suit_seq = False   # 20240413: add
                # 'Source' card: the one we want to move
                src_card = exp_pile[-n_to_move]
                if n_to_move == len_exp_pile:
                    expose = bool(pile.hidden)
                else:
                    expose = False
                    card_above = exp_pile[-n_to_move - 1]
                    if (src_card.rank + 1 == card_above.rank
                            and src_card.suit == card_above.suit):
                        tabltype = TablType.SPLIT
                    if (src_card.rank + 1 == card_above.rank
                            and (src_card.suit + 2) % 4 == card_above.suit):
                        src_in_next_suit_seq = True   # 20240413: add

                # 'target' pile is the pile we are trying to move to
                found_empty_target = False
                for target_index in range(0,7):
                    if (target_index == pile_index
                        or (not self.piles[target_index].exposed
                            and found_empty_target)
                        or (track_threshold > self.n_stock_left
                            and (last_move_info[pile_index].depth ==
                                last_move_info[target_index].depth)
                            and (last_move_info[pile_index].n_moved ==
                                 n_to_move)
                            and last_move_info[pile_index].moved_to
                            and (last_move_info[pile_index].depth > 0))):
                        continue

                    if self.piles[target_index].exposed:
                        target_card = self.piles[target_index].exposed[-1]
                    elif target_index >= self.n_stock_left:
                        found_empty_target = True

                    if not self.piles[target_index].exposed:
                        if (( n_to_move != len_exp_pile
                            or (n_to_move == len_exp_pile
                                 and (target_index < self.n_stock_left
                                       or pile_index < self.n_stock_left)))
                            and
                               (((enum_to_empty_pile == EmptyRule.ANY1 or
                             (enum_to_empty_pile == EmptyRule.HIGH1
                              and src_card.rank == 12)) and n_to_move == 1) or
                             ((enum_to_empty_pile == EmptyRule.ANYRUN or
                             (enum_to_empty_pile == EmptyRule.HIGHRUN
                              and src_card.rank == 12))))):
                            if (self.n_stock_left > 0
                                or tabltype != TablType.SPLIT
                                or split_empty_stock
                                or not (self.in_foundation(last_card.rank - 1,
                                                 (last_card.suit + 2) % 4)
                                or (self.in_foundation(last_card.rank - 2,
                                                 (last_card.suit + 2) % 4)
                                    and self.in_foundation(last_card.rank - 3,
                                                  last_card.suit)))):
                                self.valid_moves.append(TablMove(
                                    from_=pile_index, n_cards=n_to_move,
                                    to_=target_index, expose=expose,
                                    tabltype=tabltype))
                    elif (self.piles[target_index].exposed
                            and src_card.rank == target_card.rank - 1
                            and (src_card.suit % 2 == target_card.suit % 2)):
                        if src_card.suit == target_card.suit:
                            tabltype = TablType.JOIN

                        if (self.n_stock_left > 0
                            or tabltype != TablType.SPLIT
                            or split_empty_stock
                            or not (self.in_foundation(last_card.rank - 1,
                                                 (last_card.suit + 2) % 4)
                            or (self.in_foundation(last_card.rank - 2,
                                                 (last_card.suit + 2) % 4)
                                and self.in_foundation(last_card.rank - 3,
                                                  last_card.suit)))):
                            self.valid_moves.append(TablMove(
                                from_=pile_index, n_cards=n_to_move,
                                to_=target_index, expose=expose,
                                tabltype=tabltype))

                        # 20240413: add src_in_next_suit_seq to condition
                        if (not self.n_stock_left
                            and not split_empty_stock
                            and target_card.suit == src_card.suit
                            and (self.in_foundation(src_card.rank,
                                                   (src_card.suit+2) % 4)
                                or (not move_same_suit
                                    and (self.in_suit_seq[src_card.rank][
      (src_card.suit + 2) % 4]
                                         or (src_card.rank < 12
                                             and (self.last_in_pile[
      src_card.rank+1][(src_card.suit + 2) % 4])
        or src_in_next_suit_seq))))):
                            force_move = TablMove(
                                from_=pile_index, n_cards=n_to_move,
                                to_=target_index, expose=expose,
                                tabltype=tabltype)

            # Move card to foundation (MoveToFound dataclass)
            expose = bool(len_exp_pile == 1 and pile.hidden)
            if (last_card.rank - 1 == self.foundation[last_card.suit]
                and (track_threshold <= self.n_stock_left
                    or not last_move_info[pile_index].depth
                    or last_move_info[pile_index].can_move_to_found)):
                if self.in_suit_seq[last_card.rank][last_card.suit]:
                    tabltype = TablType.SPLIT
                else:
                    tabltype = TablType.NONE
                self.valid_moves.append(MoveToFound(from_=pile_index,
                        suit=last_card.suit, expose = expose,
                        tabltype=tabltype))
                same_color_suit = (last_card.suit + 2) % 4

                # See discussion in docstring about forcing moves
                if (self.in_foundation(last_card.rank - 2, same_color_suit)
                    or (self.n_stock_left == 0 and not split_empty_stock
                        and self.in_suit_seq[last_card.rank - 1][
                            same_color_suit])):
                    force_move = MoveToFound(from_=pile_index,
                            suit=last_card.suit, expose=expose,
                            tabltype=tabltype)

        if force_move:
            self.valid_moves.clear()
            self.valid_moves.append(force_move)

    def play_base_card(self, base_card: Card) -> None:
        """Play the base card into the foundation.

        Arguments
        ---------
        base_card : Card

        Returns
        -------
        None
        """
        self.foundation[base_card.suit] = 0
        self.last_in_pile[0][base_card.suit] = True
        self.in_suit_seq[0][base_card.suit] = True
        self.n_stock_left = self.n_stock_left - 1

    # TODO: probably should be moved to constructor
    def set_last_cards(self, deck: list[Card]) -> None:
        """Set information about last cards in deck for use by is_deal_blocked.

        This isn't used to deal, so we don't store which card is actually the
        last, we only store their values and which is lower and two indicator
        variables.
        """
        if deck[-1].rank < deck[-2].rank:
            self.lower_last = deck[-1]
            self.upper_last = deck[-2]
        else:
            self.lower_last = deck[-2]
            self.upper_last = deck[-1]

        card1 = self.lower_last
        card2 = self.upper_last

        self.last_same_suit_seq = (card1.suit == card2.suit
             and card1.rank + 1 == card2.rank)
        self.last_same_color_not_suit = card1.suit ==(card2.suit + 2) % 4

    def is_deal_forced(self) -> bool:
        """Check if deal can be forced (if cards can be forced to foundation).

        Generally, a card can be forced to the foundation if (1) the card
        below it is already in the foundation, and
        (2a) Card(rank - 2, same_color_suit) is already in the foundation, or
        (2b) Card(rank - 1, same_color_suit) is in sequence under a card of
        the same suit and split_empty_stock is False.

        Here we consider only (1)+(2a), as the correctness is easier to
        discern and the effect of (1)+(2b) is negligible.

        This code also handles the case where the two last cards might be
        the same color but different suits (in which case putting the first
        card into the foundation will increase the threshold at which the
        second card would be forced into the foundation).

        Returns
        -------
        Boolean indicating whether the deal should be forced.
        """
        card1 = self.lower_last
        card2 = self.upper_last
        if self.n_stock_left != 2:
            return False
        else:
            can_put1 = False
            can_put2 = False
            if self.last_same_suit_seq:
                can_put1 = self.in_foundation(card1.rank - 1, card1.suit)
                can_put2 = can_put1
            else:
                can_put1 = self.in_foundation(card1.rank - 1, card1.suit)
                can_put2 = self.in_foundation(card2.rank - 1, card2.suit)

            card1_forcable = (can_put1
                and (self.in_foundation(card1.rank - 2, (card1.suit + 2) % 4)))
            card2_forcable = (can_put2
                and (self.in_foundation(card2.rank - 2, (card2.suit + 2) % 4)))

            # TODO: maybe can get rid of one of the if branches since
            # card1.rank <= card2.rank
            if card1_forcable and card2_forcable:
                return True
            elif (not self.last_same_color_not_suit
                    or (not card1_forcable and not card2_forcable)):
                return False
            elif (card1_forcable and can_put2
                    and self.in_foundation(card2.rank - 3, card1.suit)):
                return True
            elif (card2_forcable and can_put1
                    and self.in_foundation(card1.rank - 3, card2.suit)):
                return True
            else:
                return False

    def set_sort_order(self, move_to_empty_pile: EmptyRule) -> None:
        """Set sort_order.

        Update the sort_order using pile_sort_key as the key.
        """
        # TODO: could move this out to perform_move and undo_move
        for pile_index in range(0, 7):
            self.sort_order[pile_index] = pile_index

        if self.n_stock_left > 2:
            #print(self.sort_order)
            #print(self.hash_str)
            return
        elif move_to_empty_pile != EmptyRule.NONE:
            self.sort_order.sort(key = lambda x: pile_sort_key(
                    self.pile_sort_info[x]))
            #self.sort_order = sorted(self.sort_order,
            #    key=lambda x: pile_sort_key(self.pile_sort_info[x]))
        #print(self.sort_order)
        #print(self.hash_str)

    def in_foundation(self, rank: int, suit: int) -> bool:
        return self.foundation[suit] >= rank

def pile_sort_key(pile_sort_info: PileSortInfo) -> int:
    """Sort piles for losing states set.

    If n_stock_left = 2, the first two piles will be covered by the last deal,
    so they are not equivalent to each other or the other two and are always
    sorted first by their index. Otherwise, sort empty piles before non-empty
    and if non-empty, sort by card value.

    Returns
    -------
    Integer taking values:
       (0-1) if n_stock_left = 2 and pile_index <= 1,
       (2-9) calculated as pile_index+2 if the pile is empty
       (10-62) calculated as Card(value) + 10 otherwise, where the card is the
             top card in the pile (index=0)
    """
    if pile_sort_info.n_stock_left == 2 and pile_sort_info.pile_index <= 1:
        retval = pile_sort_info.pile_index
    elif pile_sort_info.pile.hidden:
        retval = (pile_sort_info.pile.hidden[0].rank*4
                 + pile_sort_info.pile.hidden[0].suit + 10)
    elif pile_sort_info.pile.exposed:
        retval = (pile_sort_info.pile.exposed[0].rank*4
                 + pile_sort_info.pile.exposed[0].suit + 10)
    else:
        retval = pile_sort_info.pile_index + 2
    return retval

