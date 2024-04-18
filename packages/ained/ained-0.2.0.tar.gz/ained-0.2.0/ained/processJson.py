import json
import os

from jsonschema import validate

from .board import Board
from .calculator import calc_all_probs
from .dipole import State
from .generator import IGenerator
from .historymanager import HistoryManager


def load_and_validate_json(filename):
    base_dir = os.path.dirname(__file__)
    rel_path = "Data"
    schema_file_path = os.path.join(base_dir, rel_path, "jasonSchema.json")

    with open(schema_file_path) as schema_file:
        schema = json.load(schema_file)

    with open(filename, 'r') as data_file:
        data = json.load(data_file)

    validate(instance=data, schema=schema)

    return data


def process_board_data(data, output, random_generator: IGenerator):
    board_properties = data["boardProperties"]
    rows = board_properties["rows"]
    columns = board_properties["columns"]
    prob = board_properties["probability"]
    initial_states = board_properties["initialState"]
    timesteps = data["timesteps"]

    # Build board
    history_manager = HistoryManager()
    board = Board(size_x=rows, size_y=columns, flip_probability=prob, generator=random_generator,
                  initial_states=initial_states)

    # Apply changes for each timestep
    for timestep in timesteps:
        print(f"Time: {timestep['time']}, Changes: {timestep['changes']}")
        for change in timestep['changes']:
            x = change['x']
            y = change['y']
            proposed = change['state']
            current = board.get_dipole(x, y).current_state.value

            if proposed == current:
                # Reinforce operation
                board.get_dipole(x, y).reinforce()
            else:
                # Dirty operation (proposed state is different from current state)
                board.get_dipole(x, y).stage_flip(State(proposed))

        # Then calculate probabilities of flipping other dipoles
        calc_all_probs(board)
        board.commit_and_propagate_staged_writes()

    board.history_manager.export_to_file(output)
