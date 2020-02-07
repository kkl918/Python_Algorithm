# 檢測正整數n是否為2的冪次
# n=4 -> True, n=5 -> False

class Solution:
	def checkPowerOf2(self, n):
		ans = 1
		for i in range(31):
			if ans == n:
				return True
			ans = ans << 1
		return False

if __name__ == '__main__':
	sol   = Solution()
	nums1 = 16
	nums2 = 17
	print('Input  : ' + str(nums1))
	print('Result : ' + str(sol.checkPowerOf2(nums1)))
	print('Input  : ' + str(nums2))
	print('Result : ' + str(sol.checkPowerOf2(nums2)))



