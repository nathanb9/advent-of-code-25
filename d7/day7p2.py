file = open("d7p2input.txt", "r")
content = file.read()
grid = content.split('\n')

# beam entry point aka `S`
prev_beam_paths = [0 if grid[0][i] != 'S' else 1 for i in range(len(grid[0]))]

for beam_row_index in range(1, len(grid) - 1):
    beam_row = grid[beam_row_index]

    # update beam from prev_beam_location
    for space_index in range(0, len(beam_row) - 1):
        if beam_row[space_index] == '^':            
            prev_beam_paths[space_index - 1] += prev_beam_paths[space_index]
            prev_beam_paths[space_index + 1] += prev_beam_paths[space_index]    

            prev_beam_paths[space_index] = 0 
            


print(sum(prev_beam_paths))
file.close()
