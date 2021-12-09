"""
One line solution that uses a set. Set's do not contain duplicates. Length's should be the same if there are no duplicates!

Time complexity: O(n).
Space complexity: O(n).
"""
def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)

        return False
