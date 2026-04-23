file = open("d11p1input.txt", "r")
content = file.read()
input_values = content.split('\n')

# acyclic btw
graph = {}

for relationships in input_values: 
    rel = relationships.split(' ')
    source = rel[0][0:len(rel[0]) - 1]
    routes = rel[1:len(rel)]
    graph[source] = set(routes)

if 'out' not in graph:
    graph['out'] = set()

queue = [('you', ['you'])]
valid_paths = []

while queue:     
    curr, path = queue.pop(-1)
    if curr == 'out': 
        valid_paths.append(path)
    for child in graph[curr]:

        if child not in path:
            new_path = path + [child]
            queue.append((child, new_path))
            
print(valid_paths)
print(len(valid_paths))
        

    




    