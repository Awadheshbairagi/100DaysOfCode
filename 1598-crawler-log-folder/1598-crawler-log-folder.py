class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder_depth = 0

        # Iterate through each log operation
        for current_operation in logs:
            # Go up one directory if "../" is encountered, but don't go above the root
            if current_operation == "../":
                folder_depth = max(0, folder_depth - 1)
            # Increase depth if the log is not 'stay in the current directory'
            elif current_operation != "./":
                # Go down one directory
                folder_depth += 1
            # Ignore "./" operations as they don't change the current folder

        return folder_depth