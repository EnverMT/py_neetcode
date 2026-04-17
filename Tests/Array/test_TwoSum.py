from Leetcode.Array.TwoSum import Solution

solution = Solution()


def test_two_sum_returns_correct_indices() -> None:
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_returns_empty_list_when_no_solution() -> None:
    assert solution.twoSum([1, 2, 3], 7) == []


def test_two_sum_returns_correct_indices_with_duplicates() -> None:
    assert solution.twoSum([3, 3], 6) == [0, 1]


def test_two_sum_returns_correct_indices_with_negative_numbers() -> None:
    assert solution.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]


def test_two_sum_returns_correct_indices_with_zero() -> None:
    assert solution.twoSum([0, 4, 3, 0], 0) == [0, 3]


def test_two_sum_handles_two_element_input() -> None:
    assert solution.twoSum([9, 1], 10) == [0, 1]


def test_two_sum_finds_solution_at_the_end() -> None:
    assert solution.twoSum([1, 5, 3, 7], 10) == [2, 3]


def test_two_sum_handles_unsorted_values() -> None:
    assert solution.twoSum([8, 1, 6, 2], 10) == [0, 3]


def test_two_sum_handles_large_numbers() -> None:
    assert solution.twoSum([1_000_000, 500_000, -500_000, 3], 0) == [1, 2]


def test_two_sum_handles_repeated_values_before_match() -> None:
    assert solution.twoSum([1, 1, 1, 2, 8], 10) == [3, 4]


def test_two_sum_handles_same_number_used_twice_from_different_indices() -> None:
    assert solution.twoSum([5, 1, 5], 10) == [0, 2]


def test_two_sum_handles_zero_with_negative_and_positive_pair() -> None:
    assert solution.twoSum([0, -3, 1, 3], 0) == [1, 3]


def test_two_sum_finds_solution_in_the_middle() -> None:
    assert solution.twoSum([11, 2, 7, 15], 9) == [1, 2]


def test_two_sum_returns_smaller_index_first() -> None:
    assert solution.twoSum([4, 1, 2, 4], 8) == [0, 3]
