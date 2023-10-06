class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the input list is empty, there is no common prefix
        if not strs:
            return ""
        
        # Sort the list of strings to ensure the shortest and longest strings are at the extremes
        strs.sort()
        # Take the first and last strings in the sorted list
        first_str = strs[0]
        last_str = strs[-1]
        
        # Compare the characters of the first and last strings
        common_prefix = []
        for i in range(len(first_str)):
            # If the characters match, add to the common prefix
            if i < len(last_str) and first_str[i] == last_str[i]:
                common_prefix.append(first_str[i])
            # If characters don't match, break the loop
            else:
                break
        
        # Join the characters to form the common prefix string
        return ''.join(common_prefix)
