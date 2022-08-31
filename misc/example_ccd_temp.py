#!/usr/bin/env python3

# Example of an external temperature script for indi-allsky
# The first line to STDOUT should be a number
# Additional lines are ignored
# Any info sent to STDERR is also ignored

import sys


temp_c = -5.111

print('STDERR is ignored', file=sys.stderr)

# first line to STDOUT must contain a number with no additional details
# number is assumed to be celcius

print(f'{temp_c:0.2f}')  # formatting is not necessary, this is just an example

# This would also be valid
#print(temp_c)


print('Any additional lines are ignored')
