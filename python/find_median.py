ptr1 = 0
        ptr2 = 0
        
        count = 0
        
        combined_arr = []
        
        if nums1[len(nums1) - 1] < nums2[ptr0]:
            for i in nums2:
                nums1.append(i)
            count = len(nums1)
            if count % 2 != 0:
                median_num = nums1[count//2]
                return median_num
        elif nums2[len(nums2) - 1] < nums1[ptr0]:
            for i in nums1:
                nums2.append(i)
            count = len(nums2)
            if count % 2 != 0:
                median_num = nums2[count//2]
                return median_num
            
        else:
            while ptr1 < len(nums1) and ptr2 < len(nums2):
                if nums1[ptr1] < nums2[ptr2]:
                    combined_arr.append(nums1[ptr1])
                    ptr1 += 1