# 🎄 Advent of Code 2025 - Day 1: The Safe Combination

## 📖 Problem Description

You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the password has changed, and a document on the wall explains that the password is locked in a safe below.

### The Safe Mechanism

The safe features a **circular dial** with numbers **0-99**. The dial has an arrow that starts pointing at **50**. As you turn the dial, it clicks at each number, and the goal is to analyze a sequence of rotations to find the password.

**Key Mechanics:**
- **Rotation Notation**: `L` (left/lower numbers) or `R` (right/higher numbers) followed by a distance
- **Circular Wrapping**: Left from 0 goes to 99; right from 99 goes to 0
- **Starting Position**: 50
- **Password**: Count how many times the dial points at 0 after any rotation

### Example Walkthrough

Given rotations:
```
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
```

The dial moves through:
| Step | Rotation | Current Position | At Zero? |
|------|----------|------------------|----------|
| Start | — | 50 | ✗ |
| 1 | L68 | 82 | ✗ |
| 2 | L30 | 52 | ✗ |
| 3 | R48 | **0** | ✓ |
| 4 | L5 | 95 | ✗ |
| 5 | R60 | 55 | ✗ |
| 6 | L55 | **0** | ✓ |
| 7 | L1 | 99 | ✗ |
| 8 | L99 | **0** | ✓ |
| 9 | R14 | 14 | ✗ |
| 10 | L82 | 32 | ✗ |

**Result**: The dial points at 0 three times → **Password = 3**

---

## 🎯 Your Challenge

Analyze the rotations in your puzzle input and determine the actual password to open the North Pole base entrance.

## 📂 Files

| File | Purpose |
|------|---------|
| `main.py` | Python solution for Day 1 |
| `input.txt` | Your personal puzzle input |
| `sample-input.txt` | Example input from the puzzle |

## ▶️ How to Run

```bash
python main.py < input.txt
```

Or test with the sample:
```bash
python main.py < sample-input.txt
```

---

**Advent of Code 2025** | [Day 1 Official](https://adventofcode.com/2025/day/1)
