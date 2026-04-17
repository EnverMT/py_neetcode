from Leetcode.Array.ValidAnagram import Solution

def test_is_anagram_returns_true_for_anagrams() -> None:
    assert Solution().isAnagram("listen", "silent") is True

def test_is_anagram_returns_false_for_non_anagrams() -> None:
    assert Solution().isAnagram("hello", "world") is False