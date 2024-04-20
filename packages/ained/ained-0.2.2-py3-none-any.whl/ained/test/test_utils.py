from ..calculator import manhatten_distance, calc_prob, calc_all_probs, calc_terms
from ..board import Board
from ..dipole import Dipole, State
from math import isclose
from ..historymanager import HistoryManager


def test_manhatten_dist_zero():
    history_manager = HistoryManager()
    board = Board(2, 2, 0.7, history_manager)
    dist = manhatten_distance(board.get_dipole(0, 0), board.get_dipole(0, 0))
    assert dist == 0


def test_manhatten_dist_one():
    history_manager = HistoryManager()
    board = Board(2, 2, 0.7, history_manager)
    dist = manhatten_distance(board.get_dipole(0, 0), board.get_dipole(0, 1))
    assert dist == 1


def test_manhatten_dist_two():
    history_manager = HistoryManager()
    board = Board(2, 2, 0.7, history_manager)
    dist = manhatten_distance(board.get_dipole(0, 0), board.get_dipole(1, 1))
    assert dist == 2


def test_calc_prob_dist_one():
    history_manager = HistoryManager()
    board = Board(2, 2, 0.7, history_manager)
    prob = calc_prob(board.get_dipole(0, 0), board.get_dipole(0, 1), board.flip_probability)
    assert isclose(prob, 0.7, rel_tol=0.05)


def test_calc_prob_dist_two():
    history_manager = HistoryManager()
    board = Board(2, 2, 0.7, history_manager)
    prob = calc_prob(board.get_dipole(0, 0), board.get_dipole(1, 1), board.flip_probability)
    assert isclose(prob, 0.49, rel_tol=0.05)

def test_prob_one_red_one_blue():
    history_manager = HistoryManager()
    board = Board(2, 2, 0.7, history_manager)
    board.get_dipole(0, 0).stage_flip(State.ON)
    board.get_dipole(1, 1).stage_flip(State.OFF)
    calc_all_probs(board)

    assert isclose(board.get_dipole(0, 1).prob_on, 0.21, rel_tol=0.05)
    assert isclose(board.get_dipole(0, 1).prob_off, 0.21, rel_tol=0.05)
    assert isclose(board.get_dipole(0, 1).prob_unchanged, 0.58, rel_tol=0.05)

    assert isclose(board.get_dipole(1, 0).prob_on, 0.21, rel_tol=0.05)
    assert isclose(board.get_dipole(1, 0).prob_off, 0.21, rel_tol=0.05)
    assert isclose(board.get_dipole(1, 0).prob_unchanged, 0.58, rel_tol=0.05)

def test_prob_two_blue():
    history_manager = HistoryManager()
    board = Board(2, 2, 0.7, history_manager)
    board.get_dipole(0, 0).stage_flip(State.ON)
    board.get_dipole(1, 1).stage_flip(State.ON)
    calc_all_probs(board)

    assert isclose(board.get_dipole(0, 1).prob_on, 0.91, rel_tol=0.05)
    assert isclose(board.get_dipole(0, 1).prob_off, 0, rel_tol=0.05)
    assert isclose(board.get_dipole(0, 1).prob_unchanged, 0.09, rel_tol=0.05)

    assert isclose(board.get_dipole(1, 0).prob_on, 0.91, rel_tol=0.05)
    assert isclose(board.get_dipole(1, 0).prob_off, 0, rel_tol=0.05)
    assert isclose(board.get_dipole(1, 0).prob_unchanged, 0.09, rel_tol=0.05)

def test_prob_two_blue_two_red():
    history_manager = HistoryManager()
    board = Board(5, 5, 0.7, history_manager)
    board.get_dipole(0, 0).stage_flip(State.ON)
    board.get_dipole(0, 4).stage_flip(State.ON)
    board.get_dipole(4, 0).stage_flip(State.OFF)
    board.get_dipole(4, 4).stage_flip(State.OFF)
    calc_all_probs(board)

    assert isclose(board.get_dipole(2, 2).prob_off, 0.24, rel_tol=0.05)
    assert isclose(board.get_dipole(2, 2).prob_on, 0.24, rel_tol=0.05)
    assert isclose(board.get_dipole(2, 2).prob_unchanged, 0.51, rel_tol=0.05)


