from logic_utils import build_new_game_state, check_guess


def test_hint_direction_for_too_low_guess():
    # VERIFIED: This regression test confirms the reversed-hint bug stays fixed ("Too Low" => "Go HIGHER").
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_hint_direction_for_too_high_guess():
    # VERIFIED: This is the opposite branch check so both hint directions are locked down.
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_new_game_state_resets_score():
    # AI COLLAB: Cursor suggested isolating reset state into build_new_game_state for easier unit testing.
    state = build_new_game_state(1, 100, "Normal", rng_func=lambda low, high: 42)
    assert state["score"] == 0


def test_new_game_state_clears_input_and_history():
    # VERIFIED: Confirms new game wipes both typed input and guess history from the previous round.
    state = build_new_game_state(1, 100, "Hard", rng_func=lambda low, high: 17)
    assert state["history"] == []
    assert state["guess_input_Hard"] == ""
