# Shadow tree v3 (full per-work walk of the held rows)
v1 and v2 folders are untouched. v3 layer = results2.txt (all C/+C lines, v3 lines tagged `v3`), holds3.txt (named hold reasons), decided.txt (rows with a decision).
Per-book analysis lives in `book-analysis/books-NNNN.yaml` (250 queue ids per file, block YAML, greppable). Keys: id title author form has_magic is_real_earth setting genre tags confidence source decision note.
Values: has_magic true/false/?; is_real_earth true/false/?; setting earth_now|earth_past|earth_future|invented_world|space|other_planet|multiverse; source = knowledge|ol|web|title_form|title_guess. `rec.py attrs.txt` upserts records. The walk resumes from these records; do not re-research a record whose source is not title_guess.
