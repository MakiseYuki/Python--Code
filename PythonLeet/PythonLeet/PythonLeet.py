class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

    def addString(self, num1: str, num2: str) -> str:
        sum = int(num1)+int(num2)
        return(str(sum))

    def climbStairs(self, n: int) -> int:
        f1 = 1; f2 = 2
        if n == 1:
            return f1
        elif n==2:
            return f2
        else:
            for i in range(n-2):
                ans = f1 + f2
                f1 = f2
                f2 = ans
            return ans

    def twoSum(self, nums: List[int], target: int)-> List[int]
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums.__contains__(diff) and nums.index(diff) != i:
                return [i, nums.index(diff)]

    def firstUniqChar(self, s: str) -> int:
        min_index = len(s) + 1
        
        for char in set(s):
            if s.count(char) == 1:
                min_index = min(s.index(char),min_index)
        if min_index == len(s) + 1:
            min_index = -1
        return min_index


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = [[-1 for y in range(101)] for x in range(10001)]
        
        return
    

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        secondary, primary= divmod(key, 10000)
        self.hashmap[primary][secondary] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        secondary, primary= divmod(key, 10000)
        return self.hashmap[primary][secondary]
        
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        secondary, primary= divmod(key, 10000)
        self.hashmap[primary][secondary] = -1

if __name__ == "__main__":
    alg = Solution()
    ans = alg.climbStairs(5)
    print(str(ans))