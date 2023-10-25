class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Combine names and heights into pairs and sort them based on heights in descending order
        sorted_pairs = sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
        
        # Extract the sorted names from the sorted pairs
        sorted_names = [name for name, height in sorted_pairs]
        
        return sorted_names
