# EXECUTED 2026-10-28 15:05 (commit cd904064) - Modern Albion myth scope split
Served by main 2026-10-28 14:47 with main's names: Modern Albion epics / Modern Albion folklore (re-served 14:50 after "Too many words").
Axis: scale of the mythic conflict's stake in present-day life - the modern world is the prize vs
folklore encountered within ordinary modern life. Mapping 3/7 (same as final call):
- EPICS (3): the-dark-is-rising-sequence, prosperos-children, the-weirdstone-trilogy
  (Boneland bk3 quieter late-coda departure - disclose in yaml placement_history + serve text)
- FOLKLORE (7): king-rat, the-green-man-series, the-owl-service, lanny, greenmantle,
  a-midwinters-tail, the-albion-triptych

## Execution shape (split-with-umbrella rule, SPLITTING.md)
- modern-albion-myth STAYS as umbrella, works:[] (keep the key - verify_local requires it),
  status umbrella, def updated to say it is partitioned by stake-scale; children: the two new leaves.
- New leaf ids: modern-albion-epics / modern-albion-folklore (dirs under
  taxonomy/speculative-fiction/fantasy/real-earth-fantasy/contemporary-fantasy/
  contemporary-mythic-fantasy/modern-european-myth/modern-celtic-myth/modern-albion-myth/)
- Each leaf: genre.yaml (label, definition WITH Not-line vs sibling, works list, ruling citing
  approval message id, history), portrait (2 variants each, next free portrait number 838+;
  portrait rules: no people preferred, no franchise refs, no bows/arrows, 2:3, no text),
  works/<id>.yaml mirror files MOVED from parent works/ (git mv) with placement_history entries
  recording the re-walk root-down into the new leaf.
- index.html nodes list: edit parent's works->[], add two child dicts (parent:
  modern-albion-myth), portraits once generated. FLAT LIST dicts on the const nodes= line;
  json.JSONDecoder().raw_decode edit pattern.
- Def drafts (to be finalized at serve/approval):
  EPIC: "Modern Albion myth in which the old powers' struggle has the present-day world as its
  prize: the Dark rises to cover the earth, a returned witch-queen would rule modern Britain, and
  the world's sleeping defenders wake. Not Modern Albion folklore (the stakes are particular
  lives, homes and communities, not the world's fate)."
  LOCAL: "Modern Albion myth in which the old powers are met within ordinary present-day life:
  a valley's pattern that must be re-enacted, a green presence in the village wood, animal courts
  under London, a summoned mystery in the family forest, folklore kept alive on an island, a giant
  walking England's modern history. The stakes are particular lives and communities, however
  dangerous the powers. Not Modern Albion epics (there the modern world itself is the prize)."
- Checklist after approval: verify_local.sh | grep '^OK'; commit (instinct-bot identity); push;
  poll gh run green; live QA cache-busted (#modern-albion-epics, #modern-albion-folklore,
  #modern-albion-myth); screenshot each; browser_guidance record; release lease; report with
  user-usable URLs (split reports MUST include exact membership AND URLs).
- Drive portrait folder: 0ANZA2OU2lCCCUk9PVA.
