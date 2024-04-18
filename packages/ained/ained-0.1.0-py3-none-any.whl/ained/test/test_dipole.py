from dipole import Dipole, State

def test_set_dipole_state():
    dipole = Dipole(0, 0)
    assert dipole.current_state == State.UNKNOWN
    dipole.set_current_state(State.ON)
    assert dipole.current_state == State.ON

def test_stage_flip():
    dipole = Dipole(0, 0)
    assert dipole.current_state == State.UNKNOWN
    dipole.cycle_states()
    assert dipole.current_state == State.UNKNOWN
    assert dipole.proposed_state == State.OFF
    assert dipole.dirty

def test_commit_flip():
    dipole = Dipole(0, 0)
    assert dipole.current_state == State.UNKNOWN
    dipole.cycle_states()
    dipole.commit_flip()
    assert dipole.current_state == State.OFF
    assert dipole.proposed_state == State.OFF
    assert not dipole.dirty