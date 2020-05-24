# 习题一：移动零
# 不能新建列表

# 测试代码
def fun_test(res, pre):
    if res == pre:
        return True
    return False

class Solution:
    def moveZeroes(self, nums):
        i = 0
        n_l = len(nums)
        for j in range(n_l):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

# 测试通过
s = Solution()
n = [1, 20, 0, 2, 0, 7]
s.moveZeroes(n)
print(fun_test(n, [1, 20, 2, 7,0,0]))


# 问题二：两数之和
# [1,3,7,9,0] target为12则索引为1,3
class Solution(object):
    def two_sum(self, tar, nums):
        hashmap = {}
        for i in range(len(nums)):
            if (tar-nums[i]) in hashmap:
                return [hashmap[tar-nums[i]], i]
                pass
            hashmap[nums[i]] = i
# 测试通过
ts = Solution()
res = ts.two_sum(10,[12,3,5,7,8,35,21,2,3,])
print(fun_test(res,[1,3]))
