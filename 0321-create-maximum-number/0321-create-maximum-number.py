class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge(a1, a2):
            ans = []
            ln1 = len(a1)
            ln2 = len(a2)
            while len(ans) < ln1 + ln2:
                if a1 and a2 and a1>a2:
                    ans.append(a1[0])
                    a1.pop(0)
                elif a1 and a2 and a1<=a2:
                    ans.append(a2[0])
                    a2.pop(0)
                else:
                    if a1:
                        ans.extend(a1)
                    elif a2:
                        ans.extend(a2)
            return ans
        def getMaxSeq(nums, k):
            ans = []
            for i in range(len(nums)):
                while ans and len(ans) + len(nums)-i>k and ans[-1]< nums[i]:
                    ans.pop()
                if len(ans)<k:
                    ans.append(nums[i])
            return ans
        ln1 = len(nums1)
        ln2 = len(nums2)
        if k > ln1+ ln2:
            return []
        if ln1 + ln2 ==k:
            return merge(nums1, nums2)
        if ln1 + ln2 >k:
            sol = []
            for i in range(0, k+1):
                if i>ln1 or k-i > ln2:
                    continue
                else:
                    s1 = getMaxSeq(nums1, i)
                    print(s1, "----")
                    s2 = getMaxSeq(nums2, k-i)
                    print(s2, "''''")
                    ans = merge(s1, s2)
                    print(ans)
                    sol = max(sol, ans)
            return sol


        
        
