class Solution:
    def isValid(self, s: str) -> bool:
        open_close_map = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        for i in s:
            if i in open_close_map:
                if len(stack) == 0:
                    return False
                if stack.pop()!=open_close_map[i]:
                    return False
            else:
                stack.append(i)
        return True if len(stack)==0 else False