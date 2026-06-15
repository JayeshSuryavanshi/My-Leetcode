# My-Leetcode

My personal collection of [LeetCode](https://leetcode.com/) solutions, gathered as I
work through problems to sharpen my problem-solving skills and prepare for technical
interviews. Most solutions are synced automatically from LeetCode using
[LeetHub](https://github.com/QasimWani/LeetHub).

Feel free to browse, learn from, or compare approaches. Whether you are building a
strong foundation in data structures and algorithms or just want a reference for a
specific problem, I hope these help.

## Overview

- **~290 problems solved**, organized one folder per problem.
- Solutions are written primarily in **Python**, with a single **SQL** and a single
  **C++** solution.

| Difficulty | Solved |
| ---------- | -----: |
| Easy       |    117 |
| Medium     |    138 |
| Hard       |     31 |
| **Total**  | **286** |

> Counts are approximate and reflect the problems present in this repository at the
> time of writing.

## Repository structure

Each problem lives in its own top-level directory, named after the problem's LeetCode
number and slug:

```
<number>-<problem-slug>/
├── <number>-<problem-slug>.py   # my solution (usually Python; sometimes .sql / .cpp)
├── README.md                    # the original LeetCode problem statement
└── NOTES.md                     # space for personal notes (often empty)
```

For example:

```
0001-two-sum/
├── 0001-two-sum.py
├── README.md
└── NOTES.md
```

### A note on folder names

Because the repo grew over time and the sync tooling changed, two naming conventions
coexist:

- **Zero-padded** (newer): `0001-two-sum`, `0146-lru-cache`
- **Non-padded** (older): `1-two-sum`, `146-lru-cache`, and a few bare slugs like
  `two-sum`

Some problems therefore appear under more than one folder. When looking for a problem,
search by its slug (e.g. `two-sum`) rather than relying on a fixed number format.

## How to navigate

- **Find a problem by number or name:** browse the directory list, or use your
  editor / GitHub's file finder to search for the slug.
- **Read the problem:** open the `README.md` inside a problem folder — it contains the
  original LeetCode problem statement (rendered HTML).
- **Read the solution:** open the `.py` (or `.sql` / `.cpp`) file in the same folder.

## Languages used

| Language | Files |
| -------- | ----: |
| Python   |  ~288 |
| SQL      |     1 |
| C++      |     1 |

## Conventions

- Python solutions follow LeetCode's standard `class Solution:` template with the
  method signature provided by the problem.
- Per-problem `README.md` files are the original LeetCode problem statements and are
  reproduced for reference and convenience.
- `NOTES.md` files are reserved for personal notes and are frequently empty.

## Disclaimer

Problem statements belong to LeetCode and are included only as a convenient reference
alongside each solution. All solution code is my own work.

## Happy coding!
