# 🎄 Day 1: Safe Combination Solver

> **The North Pole's Greatest Security Challenge**

---

## 🔐 The Challenge

You've arrived at the North Pole base entrance, ready to decorate—but the security protocols have changed! The password is locked away in an ancient **circular dial safe**, and you must crack the code by analyzing a sequence of rotations.

---

## 🎯 How It Works

### The Dial System

```
        ┌─────────────────────┐
        │   Circular Dial     │
        │      (0-99)         │
        │      ↓ Arrow        │
        │  Starts at: 50      │
        └─────────────────────┘
```

**Mechanics:**

- 📍 **Start Position**: Dial points at `50`
- 🔄 **Rotation Format**: `L` or `R` + distance (e.g., `L68`, `R48`)
  - `L` = rotate left (toward lower numbers)
  - `R` = rotate right (toward higher numbers)
- �� **Wrapping**: The dial is circular (0 wraps to 99 and vice versa)
- 🎯 **Goal**: Count how many times the dial lands on `0`

---

## 📋 Example Walkthrough

**Input Rotations:**

```
L68  →  L30  →  R48  →  L5  →  R60  →  L55  →  L1  →  L99  →  R14  →  L82
```

**Dial Journey:**

| # | Rotation | Position | Hits 0? |
|---|:--------:|:--------:|:-------:|
| 🔄 Start | — | **50** | — |
| 1️⃣ | L68 | 82 | ❌ |
| 2️⃣ | L30 | 52 | ❌ |
| 3️⃣ | R48 | **0** | ✅ |
| 4️⃣ | L5 | 95 | ❌ |
| 5️⃣ | R60 | 55 | ❌ |
| 6️⃣ | L55 | **0** | ✅ |
| 7️⃣ | L1 | 99 | ❌ |
| 8️⃣ | L99 | **0** | ✅ |
| 9️⃣ | R14 | 14 | ❌ |
| 🔟 | L82 | 32 | ❌ |

**Result:** The dial hits 0 **3 times** 🎉

```
→ Password: 3
```

---

## 🚀 Quick Start

### Run Your Solution

```bash
# With your puzzle input
python main.py < input.txt

# Test with sample input
python main.py < sample-input.txt
```

### What You'll See

Your program should output the password—the number of times the dial lands on 0.

---

## 📁 Project Files

```
1-12-2025/
├── 📄 README.md          ← You are here
├── 🐍 main.py            ← Your solution code
├── 📥 input.txt          ← Your puzzle input
└── 🧪 sample-input.txt   ← Example from problem
```

---

## 💡 Tips

- Remember: The dial wraps around! Left from 0 → 99, Right from 99 → 0
- Parse the direction (`L`/`R`) and distance separately
- Use modulo (`%`) arithmetic to handle the circular wrapping
- Count zeros throughout the entire rotation sequence

---

## 🔗 Resources

- 🌐 [Advent of Code 2025 - Day 1](https://adventofcode.com/2025/day/1)
- 💬 [AoC Community](https://www.reddit.com/r/adventofcode/)

---

**Status:** ✅ Complete | **Language:** 🐍 Python | **Difficulty:** ⭐ Warm-up

