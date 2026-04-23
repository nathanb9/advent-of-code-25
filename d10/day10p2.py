import math
import re

from z3 import *

file = open("d10/day10p2.txt", "r")
content = file.read()
input_values = content.split("\n")
answer = 0


for val in input_values:
    row = val.split(" ")
    transformations = [
        [int(curr_val) for curr_val in value.split(",")]
        for value in [row[index][1:-1] for index in range(1, len(row) - 1)]
    ]

    bs = [z3.Int(f"b{i}") for i in range(len(transformations))]
    optimizer = z3.Optimize()
    rhs = row[len(row) - 1]
    rhs = [int(strval) for strval in re.split("{|,|}", rhs)[1:-1]]
    print(transformations)

    optimizer.add(
        [
            z3.Sum(bs[b] for b, button in enumerate(transformations) if j in button)
            == joltage
            for (j, joltage) in enumerate(rhs)
        ]
    )

    optimizer.add([b >= 0 for b in bs])
    optimizer.minimize(z3.Sum(bs))
    if optimizer.check() != z3.sat:
        print("check failed ")
    else:
        print("didnt fail ")
        model = optimizer.model()
        answer += sum(model[b].as_long() for b in bs)
print(f"Part 2 {answer}")
