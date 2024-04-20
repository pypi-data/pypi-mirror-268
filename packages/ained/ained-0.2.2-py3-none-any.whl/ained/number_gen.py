import os
import random


def generate_random_numbers(count: int, filepath: str):
    directory = os.path.dirname(filepath)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(filepath, 'w') as file:
        for i in range(count):
            file.write(str(random.randint(0, 100)) + '\n')
