'''
 * Solution to Sort-Color at LeetCode in Python
 *
 * author: deepakr-28
 * ref: https://leetcode.com/problems/sort-colors/
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sore()
        zero = 0  #to store count of zeros in list
        one = 0   #to store count of ones in list
        two = 0   #to store count of twos in list
        for i in nums:  #loop thru the list to count the number of 0 1 and 2
            if(i==0):
                zero+=1 
            elif(i==1):
                one+=1
            else:
                two+=1
        for i in range(zero):  #making changes to original list by changing values
          nums[i] = 0
        for j in range(zero,one+zero):
          nums[j] = 1
        for k in range(one+zero,len(nums)):
          nums[k] = 2
