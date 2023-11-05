class Solution:
    def isNumber(self, s: str) -> bool:
        # Define states and transitions for the FSM
        states = [
            {"digit": 1, "sign": 2, "dot": 3},
            {"digit": 1, "dot": 4, "exponent": 5},
            {"digit": 1, "dot": 3},
            {"digit": 4},
            {"digit": 4, "exponent": 5},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7}
        ]
        
        current_state = 0
        
        # Helper function to get the input type for the FSM
        def get_input_type(char):
            if char.isdigit():
                return "digit"
            elif char in "+-":
                return "sign"
            elif char == ".":
                return "dot"
            elif char in "eE":
                return "exponent"
            else:
                return "invalid"
        
        # Process each character in the input string
        for char in s.strip():
            input_type = get_input_type(char)
            if input_type == "invalid":
                return False
            if input_type not in states[current_state]:
                return False
            current_state = states[current_state][input_type]
        
        # Check if the final state is valid (1, 4, 7)
        return current_state in [1, 4, 7]
