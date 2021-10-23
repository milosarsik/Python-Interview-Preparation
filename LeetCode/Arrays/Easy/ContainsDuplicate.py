"""
One line solution that uses a set. Set's do not contain duplicates. Length's should be the same if there are no duplicates!

Time complexity: O(n).
Space complexity: O(n).
"""
def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
