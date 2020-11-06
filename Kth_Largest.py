import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #since heapq maintains min heap by default we make it as maxHeap by multiplying with -1
        nums=[-1*n for n in nums]
        heapq.heapify(nums)
        
        #remove k elements to retrun kth largest
        while k:
            res=-heapq.heappop(nums)
            k-=1
        
        return res
#TC:- O(nlogn) n-> to build the heap structure and logn to heapify
#SC:- O(n) extra space
'''
import heapq
ls=[1,2,7,3,9,5,8]

heapq.heapify(ls) #to heapify or to maintain the heap order
print(ls)

heapq.heappush(ls,0) # to push the element in the heap and maintains the heap structure
print(ls)

heapq.heappop(ls) # to pop the element and maintains the heap structure
print(ls)

print(heapq.nsmallest(4,ls)) #to print first 4 smallest elements from the heap
print(heapq.nlargest(3,ls)) # prints first 3 largest elements
'''
