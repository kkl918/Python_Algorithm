# 判斷平方數
# 給定正整數num，判斷是否為完全平方數，要求當num維完全平方數時返回Ture，否則返回False
# 16 -> True, 17 -> False 

class Solution:
    def isPerfectSquare(self, num):
        l = 0
        r = num
        while(r - l > 1):
            mid = (l + r) / 2
            if(mid * mid <= num):
                l = mid
            else:
                r = mid
        ans = l
        if(l * l < num):
            ans = r
        return ans * ans == num

if __name__ == '__main__':
    num = 16
    print('初始值: ', num)
    sol = Solution()
    print('結果:', sol.isPerfectSquare(num))