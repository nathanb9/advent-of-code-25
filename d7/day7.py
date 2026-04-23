file = open("day7input.txt", "r")
content = file.read()
grid = content.split('\n')

# beam entry point aka `S`
prev_beam_locations = ['0' if grid[0][i] != 'S' else '1' for i in range(len(grid[0]))]
beam_splits_freq = 0

for beam_row_index in range(1, len(grid) - 1):
    beam_row = grid[beam_row_index]
    # count beams from prev_beam_location that are on a splitter in current
    
    for space_index in range(0, len(beam_row) - 1):
        if beam_row[space_index] == '^' and prev_beam_locations[space_index] == '1':
            beam_splits_freq += 1

    # update beam from prev_beam_location

    for space_index in range(0, len(beam_row) - 1):
        if beam_row[space_index] == '^' and prev_beam_locations[space_index] == '1':                   
            prev_beam_locations[space_index - 1] = '1'
            prev_beam_locations[space_index + 1] = '1'

print(beam_splits_freq)

file.close()
