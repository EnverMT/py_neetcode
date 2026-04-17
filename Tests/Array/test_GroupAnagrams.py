from Leetcode.Array.GroupAnagrams import Solution

solution = Solution()


def normalize_grouped_anagrams(groups: list[list[str]]) -> list[list[str]]:
    return sorted((sorted(group) for group in groups), key=lambda group: (len(group), group))


def test_group_anagrams_returns_anagrams_grouped_together() -> None:
    assert normalize_grouped_anagrams(
        solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
    ) == normalize_grouped_anagrams(
        [
            ["hat"],
            ["act", "cat"],
            ["stop", "pots", "tops"],
        ]
    )


def test_group_anagrams_returns_empty_list_when_input_is_empty() -> None:
    assert normalize_grouped_anagrams(solution.groupAnagrams([])) == []


def test_group_anagrams_returns_single_group_when_all_strings_are_anagrams() -> None:
    assert normalize_grouped_anagrams(
        solution.groupAnagrams(["listen", "silent", "enlist"])
    ) == normalize_grouped_anagrams([["listen", "silent", "enlist"]])


def test_group_anagrams_returns_multiple_groups_when_no_anagrams_exist() -> None:
    assert normalize_grouped_anagrams(solution.groupAnagrams(["abc", "def", "ghi"])) == normalize_grouped_anagrams(
        [["abc"], ["def"], ["ghi"]]
    )


def test_group_anagrams_returns_correct_groups_with_empty_strings() -> None:
    assert normalize_grouped_anagrams(solution.groupAnagrams(["", "", ""])) == normalize_grouped_anagrams(
        [["", "", ""]]
    )


def test_group_anagrams_returns_correct_groups_with_single_character_strings() -> None:
    assert normalize_grouped_anagrams(solution.groupAnagrams(["a", "b", "c", "a"])) == normalize_grouped_anagrams(
        [["a", "a"], ["b"], ["c"]]
    )


def test_group_anagrams_returns_correct_groups_with_mixed_length_strings() -> None:
    assert normalize_grouped_anagrams(
        solution.groupAnagrams(["a", "ab", "ba", "abc", "cba"])
    ) == normalize_grouped_anagrams(
        [
            ["a"],
            ["ab", "ba"],
            ["abc", "cba"],
        ]
    )


def test_group_anagrams_returns_correct_groups_with_repeated_strings() -> None:
    assert normalize_grouped_anagrams(
        solution.groupAnagrams(["abc", "bca", "cab", "abc"])
    ) == normalize_grouped_anagrams([["abc", "bca", "cab", "abc"]])
