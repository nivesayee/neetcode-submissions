class Solution:
    def isValid(self, s: str) -> bool:
        open_close_mapper = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []
        for i in s:
            if i in open_close_mapper:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if open_close_mapper[stack.pop()] != i:
                    return False
        return len(stack)==0
            