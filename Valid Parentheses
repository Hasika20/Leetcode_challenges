class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {"(":")", "{":"}", "[":"]"}
        stack = []
        for i in s:
            if i in dict.keys():
                stack.append(i)
            elif i in dict.values():
                if not stack or dict[stack.pop()] != i:
                    return False
        return not stack