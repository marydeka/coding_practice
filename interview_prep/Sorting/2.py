"""Leetcode 4. Median of Two Sorted Arrays
Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""

def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    
    both_arrays = sorted(nums1+nums2)
    arr_length = len(both_arrays)
    if arr_length %2 == 1:
        return both_arrays[arr_length//2]
    else :
        return (both_arrays[arr_length//2] + both_arrays[(arr_length//2)-1])/2

"""below is what looks like a better solution, but I can't understand the end of it


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        left=len(nums1)
        right=len(nums2)
        i,j=0,0
        res=[]
        while i<left and j<right:
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
                

    
        res.extend(nums1[i:])
        
        res.extend(nums2[j:])
        
        lent=len(res)-1
        return res[int(lent/2)] if len(res)%2!=0 else 0.5*(res[int(lent/2)] + res[int(lent/2)+1])

        """