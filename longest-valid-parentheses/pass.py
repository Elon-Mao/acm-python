class Solution:
    def longestValidParentheses(self, s: str) -> int:

        def append_len(add_len):
            nonlocal max_len
            if stack[-1] != '(' and stack[-1] != ')':
                new_len = stack.pop() + add_len
            else:
                new_len = add_len
            stack.append(new_len)
            max_len = max(new_len, max_len)

        stack = [')']
        max_len = 0
        for char in s:
            if char == '(' or stack[-1] == ')':
                stack.append(char)
            elif stack[-1] == '(':
                stack.pop()
                append_len(2)
            elif stack[-2] == '(':
                pop_len = stack.pop() + 2
                stack.pop()
                append_len(pop_len)
            else:
                stack.append(char)
        return max_len

solution = Solution()
print(solution.longestValidParentheses(')()())'))