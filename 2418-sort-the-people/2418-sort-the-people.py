class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        number_of_people = len(names)
        height_to_name_map = dict(zip(heights, names))
        sorted_heights = sorted(heights, reverse=True)
        sorted_names = [height_to_name_map[height] for height in sorted_heights]
        return sorted_names