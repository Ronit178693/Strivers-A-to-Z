def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()
        
'''
TC = O(n) + O(m+n log (m+n)) 
SC = O(1)
'''

def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1
        j = (m+n) - 1
        k = n - 1
        while(i >= 0 and k >= 0):
            if(nums1[i] < nums2[k]):
                nums1[j] = nums2[k]
                k -= 1
                j -= 1
            else:
                nums1[j] = nums1[i]
                i -= 1
                j -= 1
        while(k>=0):
            nums1[j] = nums2[k]
            k -= 1
            j -= 1
        return nums1
    
'''
TC - O(m+n)+O(n)
SC - O(1)
'''


