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
