class Solution:
	def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

		def Profit_Gain(current_pass , current_total):

			return (current_pass + 1) / (current_total + 1) - current_pass / current_total

		total_classes = len(classes)

		heap = []

		for i in range(total_classes):

			current_gain = Profit_Gain(classes[i][0] , classes[i][1])

			heapq.heappush(heap, [-current_gain , classes[i][0] , classes[i][1]])

		while extraStudents:

			gain , student , total = heapq.heappop(heap)

			student , total = student + 1, total + 1

			new_gain = Profit_Gain(student , total)

			heapq.heappush(heap, [-new_gain , student , total])

			extraStudents = extraStudents - 1

		pass_ratio = 0

		while heap:

			current_gain , student , total = heapq.heappop(heap)

			pass_ratio = pass_ratio + student / total

		result = pass_ratio / total_classes

		return result