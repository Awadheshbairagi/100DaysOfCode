class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent_count = 0

        # Iterate through each word in the words list
        for word in words:
            is_word_consistent = True

            # Check each character in the current word
            for char in word:
                is_char_allowed = False

                # Check if the current character is in the allowed string
                for allowed_char in allowed:
                    if allowed_char == char:
                        is_char_allowed = True
                        break  # Character found, no need to continue searching

                # If the character is not allowed, mark the word as inconsistent
                if not is_char_allowed:
                    is_word_consistent = False
                    break  # No need to check remaining characters

            # If the word is consistent, increment the count
            if is_word_consistent:
                consistent_count += 1

        return consistent_count