# Shadow tree v3 (full per-work walk of the held rows)
v1 and v2 folders are untouched. v3 layer = results2.txt (all C/+C lines, v3 lines tagged `v3`), holds3.txt (named hold reasons), decided.txt (rows with a decision).
Per-book analysis lives in `book-analysis/books-NNNN.yaml` (250 queue ids per file, block YAML, greppable). Keys: id title author form has_magic is_real_earth setting genre tags confidence source decision note.
Values: has_magic true/false/?; is_real_earth true/false/?; setting earth_now|earth_past|earth_future|invented_world|space|other_planet|multiverse; source = knowledge|ol|web|title_form|title_guess. `rec.py attrs.txt` upserts records. The walk resumes from these records; do not re-research a record whose source is not title_guess.

## Re-home pass needed
`rehome-todo.txt` lists cards that I placed on an umbrella id (a node already split into children) and that the autofix script routed to the child with the fewest cards. That is a count-based placement, not a thematic one. Each of those cards needs to be moved to the child (or a new child) that fits its theme. Later batches should name real leaf ids.

Re-home status (4:48 PM): the 22 dragons-and-courts cards and 12 other clear misfits from batches c029 and later are re-homed by theme (new leaves courts-and-succession-wars, dragon-champions-and-dragoneers, shadow-and-folk-realms, big-city-underworlds, private-eyes-and-cryptids and others). The rest of the c029 and later list and the c001 to c028 entries are still to be reviewed one by one against their current leaf.
