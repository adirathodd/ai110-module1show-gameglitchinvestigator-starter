# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
  - **Purpose:** A number guessing game where the player tries to guess a secret number within a specified range based on difficulty. The player receives hints ("Go Higher" or "Go Lower") and earns points based on how quickly they win. The game was intentionally broken to teach debugging and AI collaboration.

- [x] Detail which bugs you found.
  - **Bug 1:** Hints were backwards due to type mismatch. When the secret was converted to a string on even attempts, string comparison (`"50" > "10"` = True) replaced numeric comparison, reversing the logic.
  - **Bug 2:** New Game button didn't fully reset state. It only reset attempts and secret, leaving score, status, and history unchanged, preventing proper game restarts.
  - **Bug 3:** Attempts counter started at 1 instead of 0, giving players one fewer attempt than allowed.
  - **Bug 4:** String conversion on even attempts was creating the root cause of the hint bug.

- [x] Explain what fixes you applied.
  - **Fix 1:** Refactored `check_guess()` into `logic_utils.py` and ensured both guess and secret are converted to integers before comparison, eliminating type mismatches and ensuring numeric comparison.
  - **Fix 2:** Updated the New Game button to reset all session state: `attempts`, `secret`, `score`, `status`, and `history`.
  - **Fix 3:** Changed attempts initialization from `1` to `0`.
  - **Fix 4:** Removed the problematic string conversion logic that attempted `secret = str(st.session_state.secret)` on even attempts.

## 📸 Demo

✅ **Fixed Game Screenshot:** The game now runs correctly with proper hints and state management.

**Test Results:** All 4 pytest tests pass:
```
tests/test_game_logic.py::test_winning_guess PASSED                      [ 25%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 50%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 75%]
tests/test_game_logic.py::test_string_secret_comparison PASSED           [100%]

============================== 4 passed in 0.01s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
