class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        square_count, circular_count = students.count(1), students.count(0)
        
        for sandwich in sandwiches:
            if sandwich == 1 and square_count > 0:
                square_count -= 1
            elif sandwich == 0 and circular_count > 0:
                circular_count -= 1
            else:
                # No student can take the sandwich, so stop here
                break
        # Return the number of remaining students in the queue
        return square_count + circular_count
