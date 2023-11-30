class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        result = []
        previous = products
        for i in range(len(searchWord)):
            temp = []
            for product in previous:
                if len(product) > i and product[i] == searchWord[i]:
                    temp.append(product)

            previous = temp
            result.append(temp[:3])

        return result