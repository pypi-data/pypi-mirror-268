import numpy as np
from fxpmath import Fxp

from .dipole import Dipole, State
from .fixedpoint_config import DTYPE


def manhatten_distance(first: Dipole, second: Dipole):
    x_delta = abs(first.x - second.x)
    y_delta = abs(first.y - second.y)
    return x_delta + y_delta


def calc_prob(source: Dipole, sink: Dipole, prob: Fxp):
    # Ensure inputs are fixed point
    assert prob.dtype == DTYPE

    distance = manhatten_distance(source, sink)
    power = Fxp(None, False, dtype=DTYPE)
    power.equal(prob ** Fxp(distance))

    # Ensure output is fixed point
    assert power.dtype == DTYPE

    return power


def calc_terms(dirty_dipoles: set, sink: Dipole, prob, pos_term=True):
    terms = []
    coefficients = []

    initial = Fxp(1, False, dtype=DTYPE)

    coefficients.append(initial)

    for index, dipole in enumerate(dirty_dipoles):
        prob_on = calc_prob(dipole, sink, prob)
        one = Fxp(1, False, dtype=DTYPE)
        coefficients.append((one - prob_on) * coefficients[index])
        prob_on *= coefficients[index]
        terms.append(prob_on)

    sum = Fxp(None, False, dtype=DTYPE)
    sum.equal(np.sum(terms))

    assert sum.dtype == DTYPE
    return sum


def calc_all_probs(board) -> None:
    # Calculate states of static dipoles based on dynamic dipoles and distance

    # Using the dirty bits, calculate if the static bits should change
    for i in range(board.size_x):
        for j in range(board.size_y):
            if not board.grid[i, j].dirty:
                changed_dipoles = board.get_changed_dipoles()

                positive_dipoles = set([dipole for dipole in changed_dipoles if dipole.proposed_state == State.ON])
                negative_dipoles = set([dipole for dipole in changed_dipoles if dipole.proposed_state == State.OFF])

                board.grid[i, j].clear_probs()

                one = Fxp(1, False, dtype=DTYPE)

                # Only positive changed dipoles
                if len(positive_dipoles) > 0 and len(negative_dipoles) == 0:
                    prob_pos = calc_terms(positive_dipoles, board.grid[i, j], board.flip_probability)
                    board.grid[i, j].prob_on = prob_pos

                    prob_unchanged = Fxp(None, False, dtype=DTYPE)
                    prob_unchanged.equal(one - prob_pos)
                    board.grid[i, j].prob_unchanged = prob_unchanged

                # Only negative changed dipoles
                elif len(positive_dipoles) == 0 and len(negative_dipoles) > 0:
                    prob_neg = calc_terms(negative_dipoles, board.grid[i, j], board.flip_probability)
                    board.grid[i, j].prob_off = prob_neg

                    prob_unchanged = Fxp(None, False, dtype=DTYPE)
                    prob_unchanged.equal(one - prob_neg)
                    board.grid[i, j].prob_unchanged = prob_unchanged

                # Negative and positive changed dipoles
                else:
                    pos_term = calc_terms(positive_dipoles, board.grid[i, j], board.flip_probability)
                    neg_term = calc_terms(negative_dipoles, board.grid[i, j], board.flip_probability)

                    prob_pos = Fxp(None, False, dtype=DTYPE)
                    prob_pos.equal(pos_term * (one - neg_term))

                    prob_neg = Fxp(None, False, dtype=DTYPE)
                    prob_neg.equal(neg_term * (one - pos_term))

                    board.grid[i, j].prob_on = prob_pos
                    board.grid[i, j].prob_off = prob_neg

                    prob_unchanged = Fxp(None, False, dtype=DTYPE)
                    prob_unchanged.equal(one - prob_pos - prob_neg)
                    assert prob_unchanged.dtype == DTYPE

                    board.grid[i, j].prob_unchanged = prob_unchanged
