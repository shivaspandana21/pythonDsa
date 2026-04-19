"""The two-pointer technique is a problem-solving approach where we use two variables (pointers) to traverse a data structure (usually an array or string) from different directions or at different speeds to solve problems efficiently."""
#leetcode 283 move zeroes
def moveZeroes( nums): 
    """
        Do not return anything, modify nums in-place instead.
        """
    i,j=0,0
    n=len(nums)
    while i<n:
        if nums[i]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1
        i+=1

#leecode 167 two sum II input array is sorted

    def twoSum( nums, target):
        n=len(nums)
        i=0
        j=len(nums)-1
        while i<j:
            sum=nums[i]+nums[j]
            if sum==target:
                return [i+1,j+1]
            elif sum>target:
                j-=1
            else:
                i+=1
            
        
        
#leetcode 75 sort colors
def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
                
                
#leetcode 11 container with most water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        max_area=0
        while i<j:
            area=min(height[i],height[j])*(j-i)
            max_area=max(max_area,area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area
    
#leetcode 1855 maximum distance beyween a pair of values
def maxDistance( nums1, nums2):
    i,j=0,0
    ans=0
    n1=len(nums1)
    n2=len(nums2)
    while i<n1 and j<n2:
        if nums1[i]<nums2[j]:
            ans=max(ans,j-i)
            j+=1
        else:
            i+=1
    return ans

#42 trapping rain water
class Solution:
    def trap(self, height):

        start = 0
        end = len(height) - 1

        leftMax = 0
        rightMax = 0
        totalWater = 0

        while start < end:

            leftMax = max(leftMax, height[start])
            rightMax = max(rightMax, height[end])

            if leftMax < rightMax:
                totalWater += leftMax - height[start]
                start += 1
            else:
                totalWater += rightMax - height[end]
                end -= 1

        return totalWater
    
#15 3 sum
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicate second elements
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return res