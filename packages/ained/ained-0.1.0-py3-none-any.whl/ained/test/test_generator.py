from ained.generator import FileRandomGenerator
from number_gen import generate_random_numbers
from ained.generator import TausworthePRNG
import os

def test_file_random_generator():
    test_data ="./Test_Data/random_nums.txt"
    number_count = 10
    generate_random_numbers(number_count, test_data)
    generator = FileRandomGenerator(test_data)

    first_num = generator.get_random()

    num = 0
    for i in range(number_count):
        num = generator.get_random()

    assert num == first_num

def test_tausworthePRNG():
    '''
    Test to ensure the output of the TausworthePRNG is always 16 bits
    :return:
    '''
    rng = TausworthePRNG()
    for i in range(100):
        value = rng.get_random().bin()
        assert len(value) == 16

