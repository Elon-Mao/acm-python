# https://leetcode.cn/problems/dungeon-game/submissions/

class Solution(object):

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        max_i = len(dungeon) - 1
        max_j = len(dungeon[0]) - 1
        infinity = float("inf")

        def min_full_hp(i, j, full_hp, hp):
            hp = hp + dungeon[i][j]
            if hp < 1:
                full_hp += 1 - hp
                hp = 1
            move_to_right = move_to_down = infinity
            if j < max_j:
                move_to_right = min_full_hp(i, j + 1, full_hp, hp)
            if i < max_i:
                move_to_down = min_full_hp(i + 1, j, full_hp, hp)
            new_full_hp = min(move_to_right, move_to_down)
            return new_full_hp if new_full_hp is not infinity else full_hp

        return min_full_hp(0, 0, 1, 1)

solution = Solution()
print(solution.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
