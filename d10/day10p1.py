import math 

file = open("d10/day10input.txt", "r")
content = file.read()
input_values = content.split('\n')

def flipper(value, switches):
    return ''.join([('.' if letter == '#' else '#') if index in switches else value[index] for index, letter in enumerate(value)])

def getMinPath(dest, transformations):
    origin = '.' * (len(dest)) # trim brackets
    queue = [(origin, [origin])]
    

    valid_paths = []
    min_seen = math.inf
    seen = set()
    while queue:
        curr, path = queue.pop(0)

        if path[-1] == dest:                            
            min_seen = min(min_seen, len(path))
            valid_paths.append(path)
            return valid_paths

        for trans in transformations:
            possible_child = flipper(curr, trans)
            
            if possible_child not in path and len(path) < min_seen and possible_child not in seen:
                new_path = path + [possible_child]
                queue.append((possible_child, new_path))
            seen.add(possible_child)

    return valid_paths

summed_up = 0

for val in input_values:
    row = val.split(" ")    
    transformations = [tuple([int(curr_val) for curr_val in value.split(',')]) for value in [row[index][1:-1] for index in range(1, len(row) - 1)]]
    print(transformations)

    result = sorted(getMinPath(row[0][1:-1], transformations), key=lambda x: len(x))[0][1:]
    
    print("Min path: ")
    summed_up += len(result)
    
    print("=====")
    print("Min transformations required: " + str(len(result)))

print(summed_up)