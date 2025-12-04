# ⚡ Day 3: Lobby Battery Challenge

> **Getting the Escalator Running with Emergency Power**

---

## 🎯 The Challenge

You've descended into the vast lobby, only to find that all the elevators are offline due to an electrical surge. The escalator could help, but it needs power. Fortunately, there are batteries nearby that can provide emergency power!

Your mission: **arrange batteries to produce maximum joltage**.

---

## 📦 Part One: Two-Battery Banks

### The Setup

You have banks of batteries, each labeled with joltage ratings (1-9). Within each bank, you must turn on **exactly two batteries**. The joltage output is the number formed by the digits of the batteries you've turned on.

**Key Rules:**
- Select exactly 2 batteries per bank
- Cannot rearrange batteries—must use their positions
- Joltage = digits of selected batteries (e.g., selecting positions with 2 and 4 = 24 jolts)
- Find the maximum joltage for each bank
- Sum all maximum joltages

### Example Walkthrough

Given banks:
```
987654321111111
811111111111119
234234234234278
818181911112111
```

**Maximum joltage per bank:**

| Bank | Strategy | Result | Joltage |
|------|----------|--------|---------|
| 987654321111111 | Turn on first two batteries (9 and 8) | 98 | ✅ Maximum |
| 811111111111119 | Turn on batteries labeled 8 and 9 | 89 | ✅ Maximum |
| 234234234234278 | Turn on last two batteries (7 and 8) | 78 | ✅ Maximum |
| 818181911112111 | Turn on to produce 92 | 92 | ✅ Maximum |

**Total Output:** 98 + 89 + 78 + 92 = **357 jolts**

---

## 🔋 Part Two: Twelve-Battery Banks

The escalator requires more power! Now you need to turn on **exactly twelve batteries** within each bank to produce the largest possible joltage.

**Key Changes:**
- Select exactly 12 batteries per bank (instead of 2)
- Still cannot rearrange—must use positions
- Joltage output will be 12 digits long

### Updated Example

Same banks, but now selecting 12 batteries:
```
987654321111111
811111111111119
234234234234278
818181911112111
```

**Maximum joltage per bank:**

| Bank | Strategy | Result | Joltage |
|------|----------|--------|---------|
| 987654321111111 | Turn on everything except some 1s at end | 987654321111 | ✅ Maximum |
| 811111111111119 | Turn on everything except some 1s | 811111111119 | ✅ Maximum |
| 234234234234278 | Turn on everything except specific batteries | 434234234278 | ✅ Maximum |
| 818181911112111 | Turn on everything except some 1s at front | 888911112111 | ✅ Maximum |

**Total Output:** 987654321111 + 811111111119 + 434234234278 + 888911112111 = **3121910778619 jolts**

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
- **Part One:** Total output joltage for 2-battery selections
- **Part Two:** Total output joltage for 12-battery selections

---

## 📁 Project Files

```
3-12-2025/
├── 📄 README.md          ← You are here
├── 🐍 main.py            ← Your solution code
├── 📥 input.txt          ← Your puzzle input
└── 🧪 sample-input.txt   ← Example from problem
```

---

## 💡 Algorithm Tips

- **For Part One:** Iterate through all pairs of positions (i, j) where i < j, concatenate digits, convert to integer, track maximum
- **For Part Two:** Iterate through all combinations of 12 positions, concatenate digits, convert to integer, track maximum
- Use Python's `itertools.combinations()` for efficient selection
- Convert string concatenation to integer for joltage value
- Keep track of per-bank maximum, then sum all maximums

---

## 📊 Answers

| Part | Answer |
|------|--------|
| Part 1 | 17445 |
| Part 2 | _(to be filled)_ |

---

## 🔗 Resources

- 🌐 [Advent of Code 2025 - Day 3](https://adventofcode.com/2025/day/3)
- 💬 [AoC Community](https://www.reddit.com/r/adventofcode/)

---

**Status:** ✅ Complete | **Language:** 🐍 Python | **Difficulty:** ⭐⭐ Intermediate

