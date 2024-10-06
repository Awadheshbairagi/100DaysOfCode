class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        total_chemistry = 0

        # Calculate the target sum
        target_team_skill = skill[0] + skill[-1]

        # Iterate through half of the array, pairing players from both ends
        for i in range(n // 2):
            # If any team's skill doesn't match the target, return -1
            if skill[i] + skill[-i - 1] != target_team_skill:
                return -1

            # Calculate and add the chemistry of the current team
            total_chemistry += skill[i] * skill[-i - 1]

        return total_chemistry