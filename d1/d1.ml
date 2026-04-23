
let process_file filename =
  let ic = open_in filename in
  let rec io_and_acculate (running_value) =
    try
      let line_input = input_line ic in
        (*Printf.printf "cur line: (%s)\n" line_input;*)

          let current_dail_movement line =
            if line.[0] = 'R'
            then (int_of_string (String.sub line 1 ((String.length line)-1)))
            else ((int_of_string (String.sub line 1 ((String.length line) - 1))) * -1)
          in
            Printf.printf "cur line: (%s)\n" line_input;
            Printf.printf "running total: (%i)\n" running_value;
            if running_value == 0 then
              1 + io_and_acculate((((running_value + (current_dail_movement line_input)) mod 100)))
            else
              io_and_acculate((((running_value + (current_dail_movement line_input)) mod 100)))

    with End_of_file ->
      close_in ic;
      0
  in
  Printf.printf "sol: %i\n" (io_and_acculate(50))

let () = process_file "d1/d1test.txt"
