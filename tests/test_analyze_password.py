import pytest
from password_checker import analyze_password


@pytest.mark.parametrize(
    "password, expected_score, expected_label, expected_failed",
    [
        (".", 0, "Very weak", {"long enough", "has digits", "has uppercase", "has lowercase", "has symbol"}),
        ("abc", 1, "Very weak", {"long enough", "has digits", "has uppercase", "has symbol"}),
        ("ABC", 1, "Very weak", {"long enough", "has digits", "has lowercase", "has symbol"}),
        ("password", 2, "Weak", {"has digits", "has uppercase", "has symbol"}),
        ("PASSWORD", 2, "Weak", {"has digits", "has lowercase", "has symbol"}),
        ("password12", 3, "OK", {"has uppercase", "has symbol"}),
        ("PASSWORD94", 3, "OK", {"has lowercase", "has symbol"}),
        ("PASSword1245", 4, "Strong", {"has symbol"}),
        ("PasSWorD!@!", 4, "Strong", {"has digits"}),
        ("p@ssWorD!754", 5, "Very strong", set()),
        ("_PASSword765!_", 5, "Very strong", set()),
        ("Aa1-aaaaa", 5, "Very strong", set()),
        ("Aa1/aaaaa", 5, "Very strong", set()),
    ],
)
def test_analyze_password(password, expected_score, expected_label, expected_failed):
    score, label, failed = analyze_password(password)

    assert score == expected_score
    assert label == expected_label
    assert set(failed) == expected_failed
