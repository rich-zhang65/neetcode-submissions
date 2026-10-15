class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr1, ptr2 = 0, len(s) - 1

        while ptr1 < ptr2:
            while ptr1 < len(s) and not s[ptr1].isalnum():
                ptr1 += 1
            while ptr2 >= 0 and not s[ptr2].isalnum():
                ptr2 -= 1
            
            if ptr1 >= len(s) or ptr2 < 0:
                return True

            if s[ptr1].lower() != s[ptr2].lower():
                return False

            ptr1 += 1
            ptr2 -= 1
        
        return True
