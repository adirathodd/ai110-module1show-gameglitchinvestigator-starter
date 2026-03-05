import sys
from pathlib import Path

# Add parent directory to path so we can import logic_utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_string_secret_comparison():
    """
    Test the bug fix: when secret is a string, ensure numeric comparison not lexicographic.
    This specifically targets the bug where "50" > "10" (lexicographic: True) 
    but 50 > 10 (numeric: True). The old code would use string comparison 
    which reversed hints for certain number combinations.
    """
    # Secret is 10 (as a string), guess is 50 (should be Too High numerically)
    outcome, message = check_guess(50, "10")
    assert outcome == "Too High", f"Expected 'Too High' but got '{outcome}'"
    
    # Secret is 100 (as a string), guess is 5 (should be Too Low numerically)
    outcome, message = check_guess(5, "100")
    assert outcome == "Too Low", f"Expected 'Too Low' but got '{outcome}'"
    
    # Secret is 42 (as a string), guess should match
    outcome, message = check_guess(42, "42")
    assert outcome == "Win", f"Expected 'Win' but got '{outcome}'"
