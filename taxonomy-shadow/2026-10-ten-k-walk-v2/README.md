# Shadow tree v2 (seeding + split authority)
Base = v1 (../2026-10-ten-k-walk, intact). v2 layers: seeds2.txt (new leaves, N lines), splits2.txt (extra splits), results2.txt (re-walk of held rows into seeds/leaves), render2.py -> shadow-tree.txt (full text render).
Rule used for seeds: parent must be lvl4 or deeper (no touching lvl<=3 branches).
