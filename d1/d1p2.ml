

let process_file filename =
  let ic = open_in filename in
  let rec io_and_acculate (running_value) =
    try
      let line_input = input_line ic in
          let current_dail_movement line =
            if line.[0] = 'R'
              then (int_of_string (String.sub line 1 ((String.length line) - 1)))
            else ((int_of_string (String.sub line 1 ((String.length line) - 1))) * -1)
          in
            let dail_rotations_hit_zero = 
              (int_of_float ((abs_float ((float_of_int running_value) +. (float_of_int(current_dail_movement line_input)))) /. 100.0)) in
            Printf.printf "==========\n";
            Printf.printf "cur line: (%s)\n" line_input;
            Printf.printf "running total: (%i)\n" running_value;
            Printf.printf "dail rotations that hit 0: (%i)\n" dail_rotations_hit_zero;
            Printf.printf "==========\n";
            if dail_rotations_hit_zero >= 1 then
              dail_rotations_hit_zero + io_and_acculate((((abs (running_value + (current_dail_movement line_input))) mod 100)))
            else if running_value == 0 then 
              1 + io_and_acculate((((running_value + (current_dail_movement line_input)) mod 100)))
            else
              io_and_acculate((((running_value + (current_dail_movement line_input)) mod 100)))
      
    with End_of_file ->
      close_in ic;
      0
  in
  Printf.printf "sol: %i\n" (io_and_acculate(50))

let () = process_file "d1/d1test.txt"
