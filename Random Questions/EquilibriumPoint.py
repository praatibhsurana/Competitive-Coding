"""
Question on GeeksforGeeks

Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

Example 1:

Input:
n = 1
A[] = {1}
Output: 1
Explanation:
Since its the only element hence
its the only equilibrium point. 

"""
def equilibriumPoint(arr, n)
    
    if n==1 : return 1
    
    prefixSum = [0] * n
    prefixSum[0] = arr[0]
    for i in range(1, n) :
        prefixSum[i] = prefixSum[i - 1] + arr[i]
 
    # Forming suffix sum array from n-1
    suffixSum = [0] * n
    suffixSum[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1) :
        suffixSum[i] = suffixSum[i + 1] + arr[i]
 
    # Find the point where prefix
    # and suffix sums are same.
    for i in range(1, n - 1, 1) :
        if prefixSum[i] == suffixSum[i] :
            return i+1
         
    return -1
  
# Don't use brute force 
