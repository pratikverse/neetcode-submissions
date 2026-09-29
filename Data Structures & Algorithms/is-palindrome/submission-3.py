class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = "".join(char for char in s if char.isalnum()).lower()
      
        left = 0
        right = len(newStr)-1

        while(left<right):
            if newStr[left] != newStr[right]:
                return False
            else:
                left+=1
                right-=1
        return True
