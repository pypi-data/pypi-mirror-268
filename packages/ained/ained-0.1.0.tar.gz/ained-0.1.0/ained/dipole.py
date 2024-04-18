from enum import Enum

from fxpmath import Fxp

from .fixedpoint_config import DTYPE


class State(Enum):
    UNKNOWN = 0
    OFF = 1
    ON = 2


class Dipole:
    def __init__(self, x, y, initial_state=0):
        self.x = x
        self.y = y
        self.current_state = State(initial_state)
        self.proposed_state = State(initial_state)

        # The dirty flag is set if the proposed state is different from the current state
        self.dirty = False
        # The reinforced flag is set if we want to write a state to the dipole that is the same as the current state
        # and "reinforce" it.
        self.reinforced = False

        self.prob_on = Fxp(0, False, dtype=DTYPE)
        self.prob_off = Fxp(0, False, dtype=DTYPE)
        self.prob_unchanged = Fxp(0, False, dtype=DTYPE)

    def clear_probs(self):
        self.prob_on.equal(0)
        self.prob_off.equal(0)

    def cycle_states(self):
        self.proposed_state = State((self.proposed_state.value + 1) % len(State))
        self.determine_if_dirty()

    # If calling from command line, make_dirty is set to false so that if we are actually changing the state
    # then dirty is true, and if we are just reinforcing by writing the same state we still set dirty to true. 
    # It's a bit hacky and I don't like it - but it works for now
    def stage_flip(self, state: State):
        self.proposed_state = state
        self.determine_if_dirty()

    def reinforce(self):
        self.reinforced = True

    def toggle_reinforce(self):
        if self.reinforced:
            self.reinforced = False
        else:
            self.reinforced = True

    def determine_if_dirty(self):
        if (self.proposed_state != self.current_state):
            self.dirty = True
        else:
            self.dirty = False

    def set_current_state(self, state):
        self.current_state = state
        self.proposed_state = self.current_state

    def commit_flip(self):
        self.current_state = self.proposed_state
        self.dirty = False
        self.reinforced = False

    def propagate(self, x: int) -> None:
        if x <= self.prob_off:
            self.set_current_state(State.OFF)
        elif self.prob_off < x <= self.prob_off + self.prob_on:
            self.set_current_state(State.ON)
