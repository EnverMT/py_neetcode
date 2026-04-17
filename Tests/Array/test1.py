from Leetcode.Array.ContainsDuplicate import Solution


def test_has_duplicate_returns_true_when_duplicate_exists() -> None:
    assert Solution().hasDuplicate([1, 2, 3, 1]) is True


def test_has_duplicate_returns_false_when_values_are_unique() -> None:
    assert Solution().hasDuplicate([1, 2, 3, 4]) is False
