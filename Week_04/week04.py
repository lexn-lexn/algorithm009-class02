# 问题1 机器人移动
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx = [0,1,0,-1]
        dy = [1,0,-1,0] # dx,dy 组合起来在象限中看，正好是转一圈 控制方向和前进的技巧
        obstacles_set = set(map(tuple,obstacles)) #利用字典方法判断下一步是否是障碍点
        x = y = di = 0
        ans = 0
        
        for cmd in commands:
            if cmd == -2: #left
                di = (di - 1) % 4
            elif cmd == -1: #right
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacles_set:
                        x += dx[di] # 不在障碍点则更新坐标
                        y += dy[di]
                        ans = max(ans,x*x+y*y) #贪心算法只记录最好的结果，而动态规划记录过程
        return ans
		
# 问题2 分发饼干
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort() #孩子数组
        s.sort() #饼干数组
        child = 0 #孩子 i
        cookie = 0 #饼干 j
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]: #能够满足一个孩子的胃口
                child += 1 #孩子饱了
            cookie += 1 #饼干吃了
        return child #返回被满足的孩子数