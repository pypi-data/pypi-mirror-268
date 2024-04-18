import typer
from typing_extensions import Annotated

from .board import Board
from .display import Display
from .generator import TausworthePRNG
from .number_gen import generate_random_numbers
from .processJson import process_board_data, load_and_validate_json

# Information on Typer which is used to build the CLI:
# Documentation: https://typer.tiangolo.com
# Source Code: https://github.com/tiangolo/typer

app = typer.Typer()


@app.command()
def process_file(
        input_file: Annotated[str, typer.Argument(help="File path to JSON file to process.")],
        output_file: Annotated[str, typer.Argument(help="File path to save results to.")]):
    """
    Read in a json file (input_file) with board properties and a series of writes. Perform each write operation
    and propagate the results to neighboring bits. Save the entire history of writes and board states to (output_file)
    """
    rng = TausworthePRNG()
    data = load_and_validate_json(input_file)
    process_board_data(data, output_file, rng)


@app.command()
def generate_numbers(
        count: Annotated[int, typer.Argument(help="Number of random numbers to generate.")],
        filepath: Annotated[str, typer.Argument(help="File to save the random numbers to.")]):
    """
    Generate a file with random numbers from 0 to 100. Used for reproducible results.
    """
    generate_random_numbers(count, filepath)


@app.command()
def gui(
        rows: Annotated[int, typer.Argument(help="Number of rows of the dipole grid.")],
        columns: Annotated[int, typer.Argument(help="Number of columns of the dipole grid.")],
        probability: Annotated[float, typer.Option(help="Strength of co-varying effect")] = 0.7):
    """
    Create a visual representation of the dipole grid that you can interact with via a GUI.
    """
    number_generator = TausworthePRNG()
    board = Board(size_x=rows, size_y=columns, flip_probability=probability, generator=number_generator)
    Display(board)


if __name__ == "__main__":
    app()
