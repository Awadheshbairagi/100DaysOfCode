class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  # Sort the folder paths lexicographically
        result = [folder[0]]  # Initialize the result list with the first folder
        
        for path in folder[1:]:
            if not path.startswith(result[-1] + '/'):  # Check if the path is not a prefix of the last folder in result
                result.append(path)  # If not a prefix, add it to the result
        
        return result
