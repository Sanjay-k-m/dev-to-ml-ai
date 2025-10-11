# from numbers import Number


# class Solution(object):
#     def addStrings(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         result = str(int(num1) + int(num2))
#         return result
    
# s = Solution()
# s.addStrings(num1='11',num2='22')



# from ast import Break
# from operator import index


# class Solution(object):
#     def wordPattern(self, pattern, s):
#         """
#         :type pattern: str
#         :type s: str
#         :rtype: bool
#         """
#         word = s.split(' ')
#         if(len(pattern) != len(word)):
#             return False
        
#         char_to_word = {}
#         word_to_char = {}

#         for c,w in zip(pattern,word):
#             if c in char_to_word and char_to_word[c] != w:
#                 return False
#             if w in word_to_char and word_to_char[w] != c:
#                 return False
#             char_to_word[c] = w
#             word_to_char[w] = c
#         return True




          
# s = Solution()
# print(s.wordPattern(pattern='abba',s="Hey hello hello Hey"))



# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         filteredString = ''
#         for i in s:
#                 if i.isalpha():
#                      filteredString+=i.lower()
#         for i in range(len(filteredString)):
#              if  filteredString[i] != filteredString[(len(filteredString)-1)-i]:
#                   return False
             
#         return True
        

# s = Solution()

# print(s.isPalindrome(s = "0P"))


# from tempfile import tempdir


# class Solution(object):
#     def reverseString(self, s):
#         """
#         :type s: List[str]
#         :rtype: None Do not return anything, modify s in-place instead.
#         """

#         left =0
#         right = len(s)-1
#         for _ in range(len(s)//2):
#             temp =  s[left] 
#             s[left] = s[right]
#             s[right] = temp
#             left += 1 
#             right -= 1

#         return s 
# s= Solution()
# print(s.reverseString(list("Hellod")))


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s_store = {}
        t_store ={}

        for ch in s:
            s_store[ch] = s_store.get(ch,0)+ 1
        for ch in t:
            t_store[ch] = t_store.get(ch,0)+1
       
        return s_store == t_store

s= Solution()
print(s.isAnagram(s="aacc",t="ccaa"))