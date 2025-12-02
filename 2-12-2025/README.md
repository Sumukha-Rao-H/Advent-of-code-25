# 🎁 Day 2: Gift Shop ID Validator

> **Finding Invalid Product IDs in the North Pole Gift Shop**

---

## 🎯 The Challenge

You've arrived at the gift shop elevator. After exploring the surprisingly extensive selection, one of the clerks asks for your help. A young Elf was playing on a gift shop computer and accidentally added a whole bunch of **invalid product IDs** to their database!

Your task: identify all invalid product IDs across given ranges.

---

## 📋 Part One: The Pattern

An ID is **invalid** if it is made only of some sequence of digits **repeated exactly twice**.

**Examples:**
- `55` (5 repeated 2 times) ❌ Invalid
- `6464` (64 repeated 2 times) ❌ Invalid  
- `123123` (123 repeated 2 times) ❌ Invalid
- `12321` ✅ Valid (not a simple repetition)
- `101` ✅ Valid (no leading zeros)

**Important:** No leading zeros allowed! `0101` isn't an ID at all.

### Example Breakdown

Given ranges:
```
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
```

**Results:**

| Range | Invalid IDs | Count |
|-------|------------|-------|
| 11-22 | 11, 22 | 2 |
| 95-115 | 99 | 1 |
| 998-1012 | 1010 | 1 |
| 1188511880-1188511890 | 1188511885 | 1 |
| 222220-222224 | 222222 | 1 |
| 1698522-1698528 | _(none)_ | 0 |
| 446443-446449 | 446446 | 1 |
| 38593856-38593862 | 38593859 | 1 |
| 565653-565659 | _(none)_ | 0 |
| 824824821-824824827 | _(none)_ | 0 |
| 2121212118-2121212124 | _(none)_ | 0 |

**Sum of invalid IDs:** `1227775554`

---

## 🔄 Part Two: The Twist

The clerk discovers more invalid patterns! An ID is now **invalid** if made of some sequence of digits **repeated at least twice**.

**Examples:**
- `12341234` (1234 repeated 2 times) ❌ Invalid
- `123123123` (123 repeated 3 times) ❌ Invalid
- `1212121212` (12 repeated 5 times) ❌ Invalid
- `1111111` (1 repeated 7 times) ❌ Invalid

### Updated Results

| Range | Invalid IDs | Count |
|-------|------------|-------|
| 11-22 | 11, 22 | 2 |
| 95-115 | 99, 111 | 2 |
| 998-1012 | 999, 1010 | 2 |
| 1188511880-1188511890 | 1188511885 | 1 |
| 222220-222224 | 222222 | 1 |
| 1698522-1698528 | _(none)_ | 0 |
| 446443-446449 | 446446 | 1 |
| 38593856-38593862 | 38593859 | 1 |
| 565653-565659 | 565656 | 1 |
| 824824821-824824827 | 824824824 | 1 |
| 2121212118-2121212124 | 2121212121 | 1 |

**Sum of invalid IDs:** `4174379265`

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
- **Part One:** Sum of all invalid IDs (repeated pattern exactly twice)
- **Part Two:** Sum of all invalid IDs (repeated pattern at least twice)

---

## 📁 Project Files

```
2-12-2025/
├── 📄 README.md          ← You are here
├── 🐍 main.py            ← Your solution code
├── 📥 input.txt          ← Your puzzle input
└── 🧪 sample-input.txt   ← Example from problem
```

---

## 💡 Hints

- Parse comma-separated ranges with dash-separated start and end
- For Part One: Check if ID = first_half + first_half (where len(ID) is even)
- For Part Two: Check if ID can be formed by repeating a pattern multiple times
- The pattern length must divide the ID length evenly

---

## 📊 Answers

| Part | Answer |
|------|--------|
| Part 1 | 19605500130 |
| Part 2 | _(pending)_ |

---

## 🔗 Resources

- 🌐 [Advent of Code 2025 - Day 2](https://adventofcode.com/2025/day/2)
- 💬 [AoC Community](https://www.reddit.com/r/adventofcode/)

---

**Status:** 🔄 In Progress | **Language:** 🐍 Python | **Difficulty:** ⭐⭐ Intermediate

