# 🏭 Day 4: Printing Department Paper Rolls

> **Optimizing Forklift Operations to Break Through the Wall**

---

## 🎯 The Challenge

You've reached the printing department! The Elves need help optimizing forklift operations. If they can figure out how to efficiently access and remove paper rolls, they'll have time to break through the wall to the cafeteria—letting you continue deeper into the North Pole base.

**Mission:** Help the forklifts access and remove as many paper rolls as possible!

---

## 📦 Part One: Accessible Rolls

### The Setup

Paper rolls are arranged on a grid where `@` represents a paper roll and `.` represents empty space.

**Key Rule:**
- A forklift can only access a paper roll if there are **fewer than 4 rolls** in the 8 adjacent positions

### Understanding Adjacent Positions

```
X X X
X @ X
X X X
```

Count the `@` symbols in all 8 surrounding positions. If count < 4, the roll is accessible.

### Example

```
Initial Grid (10×10):
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

**Accessible rolls (marked with x):**
```
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
```

**Result:** 13 rolls of paper can be accessed

---

## 🔄 Part Two: Iterative Removal

### The Process

Once a roll can be accessed, the forklift removes it. This might make OTHER rolls accessible! Keep repeating until no more rolls can be removed.

### Removal Sequence Example

**Initial:** 13 accessible rolls
```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

**After Remove #1 (13 rolls):**
```
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
```

**After Remove #2 (12 rolls):**
```
.......x..
.@@.x.x.@x
x@@@@...@@
x.@@@@..x.
.@.@@@@.x.
.x@@@@@@.x
.x.@.@.@@@
..@@@.@@@@
.x@@@@@@@.
....@@@...
```

**After Remove #3 (7 rolls):**
```
..........
.x@.....x.
.@@@@...xx
..@@@@....
.x.@@@@...
..@@@@@@..
...@.@.@@x
..@@@.@@@@
..x@@@@@@.
....@@@...
```

**After Remove #4 (5 rolls):**
```
..........
..x.......
.x@@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@@.
....@@@...
```

**After Remove #5 (2 rolls):**
```
..........
..........
..x@@.....
..@@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@x.
....@@@...
```

**After Remove #6-9 (1 roll each):**
```
[Final state after 4 more removals]
```

**Result:** 13 + 12 + 7 + 5 + 2 + 1 + 1 + 1 + 1 = **43 total rolls removed**

---

## 🚀 Quick Start

### Run Your Solution

```bash
# With your puzzle input
python main.py < input.txt

# Test with sample input
python main.py < sample-input.txt
```

### Expected Output

Your program should output:
- **Part One:** Number of rolls accessible in initial state
- **Part Two:** Total number of rolls removed through iterative process

---

## 📁 Project Files

```
4-12-2025/
├── 📄 README.md          ← You are here
├── 🐍 main.py            ← Your solution code
├── 📥 input.txt          ← Your puzzle input
└── 🧪 sample-input.txt   ← Example from problem
```

---

## 💡 Algorithm Tips

**Part One:**
- Parse the grid into a 2D array
- For each `@` position, count neighbors (8-connected)
- If neighbor_count < 4, mark as accessible
- Return total accessible count

**Part Two:**
- Repeat Part One logic in a loop:
  - Find all currently accessible rolls
  - Remove them (mark as `.`)
  - Increment removal counter
  - Continue until no new rolls are accessible

**Implementation Hints:**
- Use nested loops to check 8-connected neighbors
- Handle boundary conditions (edge rows/columns)
- Use a copy of grid for each iteration to track changes
- Consider using BFS or iterative approach for efficiency

---

## 📊 Answers

| Part | Answer |
|------|--------|
| Part 1 | 1495 |
| Part 2 | 8768 |

---

## 🔗 Resources

- 🌐 [Advent of Code 2025 - Day 4](https://adventofcode.com/2025/day/4)
- 💬 [AoC Community](https://www.reddit.com/r/adventofcode/)

---

**Status:** ✅ Complete | **Language:** 🐍 Python | **Difficulty:** ⭐⭐ Intermediate

