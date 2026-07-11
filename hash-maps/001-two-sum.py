class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
    
    # Example usage:
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]         

#Time complexity: O(n), where n is the number of elements in the input list nums. 
# We iterate through the list once, 
# and each lookup in the hash map takes O(1) time on average.
