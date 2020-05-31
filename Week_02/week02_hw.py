# 问题一最小的k个数
#    暴力方法和大顶堆方法
class Solution1(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        col_dict = {}
        for i in nums:
            if i not in col_dict:
                col_dict[i] = 0
            col_dict[i] += 1
        res_list = sorted(col_dict.items(), key=lambda x: x[1], reverse=True)
        print(res_list)
        # col = []
        # for i in range(k):
        #     col.append(res_list[i][0])
        # return
        # 用heap堆 大顶堆求最大值
        import heapq
        return heapq.nlargest(k, col_dict.keys(), key=col_dict.get)


s = Solution1()
r = s.topKFrequent([1, 2, 1, 1, 1, 2, 3], 2)
print(r)

# 问题二 滑动窗口最大值问题
#          暴力方法
class Solution2(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        col = []
        for i in range(len(nums) - k + 1):
            col.append(max(nums[i:i + k]))
        return col


s2 = Solution2()
r = s2.maxSlidingWindow([1, 2, 3, 56, 7, 8, 3, 21, 2], 3)
print(r)