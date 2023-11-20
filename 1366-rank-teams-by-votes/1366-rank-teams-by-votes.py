from collections import defaultdict

class Solution:
    def rankTeams(self, votes):
        vote_count = defaultdict(lambda: [0] * len(votes[0]))

        for vote in votes:
            for i, team in enumerate(vote):
                vote_count[team][i] -= 1

        sorted_teams = sorted(vote_count.keys(), key=lambda x: (vote_count[x], x))
        return ''.join(sorted_teams)
