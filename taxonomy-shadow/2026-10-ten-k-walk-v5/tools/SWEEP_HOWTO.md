Re-sweep pipeline (rows MC00001-MC10069, WALK rows in verdicts-pass1.tsv):
1. python3 sweep_ol.py A B  -> Open Library author/year/subjects for WALK rows A..B
2. echo 'MC0000N|query' | python3 sweep_ws.py -> web_search snippets in parallel
3. rebuild /tmp/sw/auth.json (author -> cards in tree) from index.html, then python3 sweep_au.py <author part>
4. decide: skip-* / FOLD (tools/fold_books.py) / place (tools/live_place.py spec) / held-question (seed or split)
5. echo 'MC0000N|verdict|note' | python3 sweep_rec.py ; verify_local, commit, push, poll deploy
Progress: MC00001-73 mostly recorded; remaining WALK in that range: Dirge for Sabis, Albion, Arslan, Ballistic, Days of Future Past 2/3, Death's Head Legion, Death's Sweet Embrace, Deep State, Empire/Gateway of the Saviours, Exile's Return, Fire with Fire, Gallowglass, Geosynchron, Dark Brethren etc.
