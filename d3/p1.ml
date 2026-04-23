(*
  tldr: highest two digit value which is not necessarily contiguous but has to be consecutive.
*)

let process_file filename =
  let ic = open_in filename in
  let rec io_and_acculate =
    try
      let line_input = input_line ic in
        Printf.printf "cur line: (%s)\n" line_input;
        let rec _process_bnk remaining_digits max_val =
        let cur_dig = (int_of_char remaining_digits.[0]) in
          let d1 = (int_of_char max_val.[0]) in
          let d2 = (int_of_char max_val.[1]) in
          (* reached one digit - then get the max of the second digit and the last digit in the input*)
          if (String.length remaining_digits) == 1 then (int_of_string (String.cat (string_of_int d1) (string_of_int (max d2 cur_dig))))
          else
          if cur_dig > d1 then
            (_process_bnk (String.sub remaining_digits 1 ((String.length remaining_digits) - 1)) (String.cat (string_of_int d1) "0"))
          else
            (_process_bnk (String.sub remaining_digits 1 ((String.length remaining_digits) - 1)) (String.cat (string_of_int d1) (string_of_int (max d2 cur_dig))))
        in
        Printf.printf "process bank: %i" (_process_bnk line_input "00");
        0

    with End_of_file ->
      close_in ic;
      1

  in
  Printf.printf "\nsol: %i\n" io_and_acculate

let () = process_file "d3/sampleinput.txt"
