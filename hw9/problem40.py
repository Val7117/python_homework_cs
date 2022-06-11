#!/usr/bin/env python3

import math

# Recreate a fractional part

fractional_part = "".join(["{}".format(i) for i in range(1000000+1)])

# Choosing the needed digits on the specified positions

digits = [int(fractional_part[i]) for i in [1, 10, 100, 1000, 10000, 100000, 1000000]]

# Print the result

print("The value of the expresssion is", math.prod(digits))

