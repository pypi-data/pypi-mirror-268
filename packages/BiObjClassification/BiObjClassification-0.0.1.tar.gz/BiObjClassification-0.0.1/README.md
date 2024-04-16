#boRanking

Alpha version with most useful functions implemented.

Developed by


## Overview

The project implements a bi-objective lexicographic ranking approach. The classification is done based on two input files, one containing the results of each algorithm, and the other containing the execution times for each scenario.

## Installation

Make sure you have Python 3 installed. Then, you can install the package using the following command:


import boRanking


## Usage

After installing the package.

from boRanking import biobjective_lexicographic

# Function biobjective_lexicographic:

matrix_ranking = biobjective_lexicographic('results.csv', 'time.csv')
'Replace 'results.csv' and 'time.csv' with your file names'



## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.