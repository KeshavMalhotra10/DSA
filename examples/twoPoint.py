# Adds a pointer at another position
# can be used with two nested for-loops
# takes o(n^2) time complexity
# in code below i & j are two pointers used to compare every two elements in an array
"""
nums = [1, 2, 3, 4, 5]
n = len(nums)
for i in range(n):
    for j in range(i + 1, n):
        print(nums[i], nums[j])

"""

# two pointers usually only take 0(n) time
# we eliminate need for nested for-loops

# use two pointer algorithms when dealing with linear data structures
# ex: array, linked list, or predictable dynamic


# Two sum 2:
"""
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

"""

# solution
# --------
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # ensuring pointers start at first index, to last index
        left, right = 0, len(numbers) - 1
        while left < right:  # if left pointer crosses right pointer, no sum can be made
            sum = numbers[left] + numbers[right]

            # numbers is a sorted list [1,2,3,4,5]
            # if 1+5 = 6 is too big, move right pointer to left
            # if 1+5 = 6 is too small, move left pointer to right

            if sum < target:
                left += 1

            elif sum > target:
                right -= 1

            else:
                return [left + 1, right + 1]  # add 1 because question asks for it
        return []
'''

# time complexity of sulution is O(n), as the pointer would change n times at worse
# space complexity is 0(1) as only variables were used


# triplet sum:
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""

# since a + b + c = 0, let us fix one term a
# such that b + c = - a
# this looks awfully similar to the 2 sum solution
# however we must first sort it
# now just do 2 sum solution but iterate it through
# i terms

# solution
# ---------
"""
def triplet_sums(nums):
    triplets = []
    nums.sort()
    for i in range(len(nums)):
        # optimizations: triplets consisting
        # of only + numbers never sum to 0
        if nums[i] > 0:
            break
        # to avoid duplicate triplets, skip 'a'
        # if it's same as prev number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # find all pairs that some to target of '-a'
        pairs = pair_sum_sorted_all_pairs(nums, i + 1, -nums[i])
        for pair in pairs:
            triplets.append([str(nums[i]) + str(pair)])
    return triplets


def pair_sum_sorted_all_pairs(nums, start, target):
    pairs = []
    left, right = start, len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            # to avoid duplicate '[b,c]' pairs, skipe 'b' if it's same as prev number
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif sum < target:
            left += 1
        else:
            right -= 1
    return pairs


print(triplet_sums([0, -1, 2, -3, 1]))
"""


# is palindrome valid
# a palindrome is valid if when reversed it reads the same
# we can do this using two-pointers, checking if
# first and last, characters are same
# then moving inward till left == right
# take edge case 'abba', left !== right ever
# therefore when left passes right exit

# solution
# ---------
"""
def is_palindrome_valid(string):
    left, right = 0, len(string) - 1
    while left < right:
        # skip non-alphanumeric characters from left
        while left < right and not string[left].isalnum():
            left += 1
        # skip non-alphanumeric characters from right
        while left < right and not string[right].isalnum():
            right -= 1
        # if characters at left & right don't match,
        # it is not a palindrone
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome_valid("12.02.2021"))
"""


# largest container
# find largest container between lines of height n
# area depends on width and height
# width is between indices i and j
# height is simply the shorter of the two lines

# brute force approach


def large_contain_brute_force(heights):
    n = len(heights)
    max_water = 0

    # find max amt waeter stored between all pairs
    # of lines


"""
    for i in range(n):
        for j in range(i + 1, n):
            water = min(heights[i], heights[j]) * (j - i)
            max_water = max(max_water, water)
    return max_water
"""

# optimized solution for max water container
# start with maximum width
# then go inwards
# if left's height < right's height, left +=1
# if left's height > right's height, right-=1
# if left's height == right's height, left +=1, right -=1
# if left == right break
# if left > right break


def largest_container(height):
    n = len(height)
    max_water = 0

    left, right = 0, n - 1

    while left < right:
        water = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, water)
        if height[left] < height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1
        elif height[left] == height[right]:
            left += 1
            right -= 1
    return max_water
