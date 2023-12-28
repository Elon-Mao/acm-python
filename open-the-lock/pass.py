# https://leetcode.cn/problems/open-the-lock/

class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        end_set = set(deadends)
        if '0000' in end_set:
            return -1
        step0_set = {'0000'}
        step = 0
        while True:
            if target in step0_set:
                return step
            step += 1
            step1_set = set()
            for state in step0_set:
                for index, num in enumerate(state):
                    step1_set.add(state)
                    num = int(num)
                    new_state_format = state[:index] + '%d' + state[index + 1:]

                    def add_state(new_num):
                        new_state = new_state_format % new_num
                        if new_state not in end_set:
                            step1_set.add(new_state)

                    add_state((num + 1) % 10)
                    add_state((num + 9) % 10)
            if len(step1_set) == len(step0_set):
                return -1
            step0_set = step1_set


solution = Solution()
print(solution.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
