import os


class HistoryManager:

    def __init__(self):
        self.board_history = []
        self.write_history = []

    def record_board(self, board_state):
        self.board_history.append(board_state)

    def record_writes(self, writes: list):
        simple_writes = []
        for dipole in writes:
            info = (dipole.x, dipole.y, dipole.current_state.value)
            simple_writes.append(info)
        self.write_history.append(simple_writes)

    def clear_history(self):
        self.board_history.clear()
        self.write_history.clear()

    def export_to_file(self, filepath):

        directory = os.path.dirname(filepath)
        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(filepath, 'w') as file:
            timestep = 1
            file.write(str(self.board_history[0]) + '\n')

            for item in self.write_history:
                file.write(f"Timestep: {str(timestep)}\n")
                file.write("Writes: " + str(item) + '\n')
                file.write(str(self.board_history[timestep]) + '\n')
                timestep += 1
