class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ['+','-','*','/']:
                second_num, first_num = stack.pop(), stack.pop()
                if i == '+':
                    stack.append(first_num + second_num)
                elif i == '-':
                    stack.append(first_num - second_num)
                elif i == '*':
                    stack.append(first_num * second_num)
                elif i== '/':
                    stack.append(int(first_num/second_num))
            else:
                stack.append(int(i))
        return stack.pop()