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

- **Game purpose:** This project is a Streamlit number guessing game where the app picks a secret number and the player tries to guess it using higher/lower feedback.
- **Bugs found:** I found a reversed high/low hint bug, a session state reset issue on New Game, edge-case problems around invalid input flow, and game logic mixed directly into the UI file.
- **Fixes applied:** I corrected guess comparison/hint behavior, improved reset handling with `st.session_state`, moved core logic into helper functions in `logic_utils.py`, and verified fixes with `pytest` plus manual Streamlit testing.

## Demo Walkthrough

1. I start the app with `python -m streamlit run app.py` and leave difficulty on **Normal** (range 1-100, 8 attempts).
2. The game loads with score `0`, status `playing`, and a secret number (shown if I open **Developer Debug Info**).
3. I enter `20` and click **Submit Guess** while the secret is higher, so the app marks it as **Too Low** and shows **Go HIGHER!**.
4. The attempts count increases after submit, and the score updates for that valid guess.
5. Next I enter `80` (above the secret), and the app marks it as **Too High** with **Go LOWER!**.
6. I then try invalid input like `abc`; the app shows **That is not a number.** instead of crashing.
7. For invalid input, the submit still counts as an attempt, but score only changes on valid guesses.
8. I enter the correct number (for example, `50` if the debug panel shows `50`) and get the win message with final score.
9. After winning, the game stops further guessing until I click **New Game**.
10. Clicking **New Game** resets score/history/input and starts a fresh round with a new secret number.

## 🧪 Test Results

```
$ python3 -m pytest tests/test_game_logic.py
============================= test session starts ==============================
platform darwin -- Python 3.13.7, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/austinstanleyhinson/Desktop/AI-110/AI-110-module1show-gameglitchinvestigator
collected 4 items

tests/test_game_logic.py ....                                            [100%]

============================== 4 passed in 0.01s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
