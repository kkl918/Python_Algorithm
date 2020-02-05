# 完美平方
# 給定正整數n，找到若干個ˊ完全平方數(1, 4, 9...)，使他們的和等於n，完全平方數的各數最少。
# EX:
# 12=4+4+4, 返回3
# 13=4+9  , 返回2

class Solution:
	def numSquares(self, n):
		while n % 4 == 0:
			n//= 4
		if n % 8 == 7:
			return 4
		for i in range(n+1):
			temp = i * i
			if temp <= n:
				if int((n - temp) ** 0.5)** 2 + temp == n:
					return 1+ (0 if temp == 0 else 1)
			else:
				break
		return 3

if __name__ == '__main__':
	n = int(input('Input a value : '))
	print('Value : ', n)
	sol = Solution()
	print('Result : ', sol.numSquares(n))

