#!/usr/bin/env/python3
from numpy.random import random
import argparse

__author__ = 'sumansourav'

parser = argparse.ArgumentParser(description='Enter the sample size')
parser.add_argument('sample_sizes', type=int, nargs='+',
                    help='a list of increasing sample sizes. '
                         'Ex: python <filename.py> 10 100 1000 5000 10000 20000 30000')
args = parser.parse_args()

for arg in args.sample_sizes:
    number_of_vals_in_range = 0
    expected_val = 0.682

    for num in random(arg):
        if num < expected_val:
            number_of_vals_in_range += 1
    # Notice increasing nearness to expected value as sample size increases
    print("% of numbers within -1,1 for sample size ", arg, ": ", number_of_vals_in_range/arg*100, "%")

# TODO: Plot a graph with matplotlib or excel to visually show nearness to E(x) as sample size increases
