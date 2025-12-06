# 🍽️ Day 5: Cafeteria Inventory Management

> **Determining Fresh vs. Spoiled Ingredients in the New System**

---

## 🎯 The Challenge

You've broken through to the cafeteria! But there's a problem: the Elves switched to a new inventory management system right before Christmas, and now they can't figure out which ingredients are fresh and which are spoiled.

Your mission: **help them identify fresh ingredients using their database**.

---

## 📊 Part One: Which Available Ingredients Are Fresh?

### Understanding the Database Format

The database has two sections (separated by a blank line):

1. **Fresh Ingredient ID Ranges** - Inclusive ranges of fresh ingredient IDs
2. **Available Ingredient IDs** - IDs to check

**Key Rules:**
- Each range is inclusive (e.g., `3-5` means IDs 3, 4, and 5 are fresh)
- Ranges can overlap
- An ID is fresh if it appears in **any** range
- Determine which available IDs are fresh

### Example

**Database:**
```
3-5
10-14
16-20
12-18

1
5
8
11
17
32
```

**Fresh Ranges:** 3-5, 10-14, 16-20, 12-18

**Analysis:**

| ID | In Range? | Status |
|----|-----------|----|
| 1 | ❌ Not in any range | 🔴 Spoiled |
| 5 | ✅ In range 3-5 | 🟢 Fresh |
| 8 | ❌ Not in any range | 🔴 Spoiled |
| 11 | ✅ In range 10-14 | 🟢 Fresh |
| 17 | ✅ In ranges 16-20, 12-18 | 🟢 Fresh |
| 32 | ❌ Not in any range | 🔴 Spoiled |

**Result:** 3 fresh ingredients (IDs: 5, 11, 17)

---

## 🔄 Part Two: Total Fresh Ingredient IDs

Now ignore the available ingredients section. Instead, find **all ingredient IDs** that the fresh ranges consider to be fresh.

### Key Difference

- Part One: Check which **available** IDs are fresh
- Part Two: Find **all possible** IDs that ranges cover

### Example

**Fresh Ranges:**
```
3-5
10-14
16-20
12-18
```

**All Fresh IDs According to Ranges:**

| Range | IDs Covered |
|-------|------------|
| 3-5 | 3, 4, 5 |
| 10-14 | 10, 11, 12, 13, 14 |
| 16-20 | 16, 17, 18, 19, 20 |
| 12-18 | 12, 13, 14, 15, 16, 17, 18 |

**Combined Unique IDs:** 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

**Result:** 14 total ingredient IDs considered fresh

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
- **Part One:** Number of available ingredient IDs that are fresh
- **Part Two:** Total count of all IDs covered by fresh ranges

---

## 📁 Project Files

```
5-12-2025/
├── 📄 README.md          ← You are here
├── 🐍 main.py            ← Your solution code
├── 📥 input.txt          ← Your puzzle input
└── 🧪 sample-input.txt   ← Example from problem
```

---

## 💡 Algorithm Tips

**Part One:**
- Parse the database: separate ranges from available IDs
- For each available ID, check if it falls within any range
- Count how many are fresh
- Handle overlapping ranges properly

**Part Two:**
- Parse only the ranges section
- Find all unique IDs covered by all ranges combined
- Approach 1: Create a set of all IDs in all ranges (fast for small ranges)
- Approach 2: Merge overlapping ranges, then sum coverage (fast for large ranges)
- Return the total count

**Implementation Hints:**
```python
# Check if ID is in any range
def is_fresh(id, ranges):
    return any(start <= id <= end for start, end in ranges)

# Count total coverage (Part Two)
def count_fresh_ids(ranges):
    fresh_ids = set()
    for start, end in ranges:
        fresh_ids.update(range(start, end + 1))
    return len(fresh_ids)

# More efficient for large ranges: merge overlapping ranges
def merge_ranges(ranges):
    sorted_ranges = sorted(ranges)
    merged = []
    for start, end in sorted_ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged
```

---

## 📊 Answers

| Part | Answer |
|------|--------|
| Part 1 | 664 |
| Part 2 | 350780324308385 |

---

## 🔗 Resources

- 🌐 [Advent of Code 2025 - Day 5](https://adventofcode.com/2025/day/5)
- 💬 [AoC Community](https://www.reddit.com/r/adventofcode/)

---

**Status:** ✅ Complete | **Language:** 🐍 Python | **Difficulty:** ⭐⭐ Intermediate

