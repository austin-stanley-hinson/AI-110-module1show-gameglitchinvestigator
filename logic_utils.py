import random


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIXME: Initial investigation showed the hint logic was reversed for guesses above/below the secret number.
    # FIX: I used AI to trace the comparison branches, then I flipped the hint text to match each outcome.
    # AI REVIEW: One AI idea involved mixed-type comparisons, so I kept this strictly numeric and re-checked manually.
    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def build_new_game_state(low: int, high: int, difficulty: str, rng_func=None):
    """
    Return a clean game-state payload for starting a new game.

    rng_func is injectable for deterministic tests.
    """
    if rng_func is None:
        rng_func = random.randint

    # FIX: New game now starts from a clean state so prior score/history/input do not leak into the next round.
    # VERIFIED: Covered by pytest in test_game_logic.py and re-tested in the live Streamlit app.
    return {
        "attempts": 1,
        "secret": rng_func(low, high),
        "score": 0,
        "status": "playing",
        "history": [],
        f"guess_input_{difficulty}": "",
    }
