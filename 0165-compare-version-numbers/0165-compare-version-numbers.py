class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the versions by '.'
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        # Make both version lists equal in length by appending zeros
        diff = len(v1) - len(v2)
        if diff > 0:
            v2.extend([0] * diff)
        else:
            v1.extend([0] * abs(diff))

        # Compare versions
        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1

        return 0

