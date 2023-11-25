from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        mutations = {'A', 'C', 'G', 'T'}
        queue = deque([(startGene, 0)])
        
        while queue:
            gene, num_mutations = queue.popleft()
            
            if gene == endGene:
                return num_mutations
            
            gene_list = list(gene)
            for i in range(len(gene_list)):
                original = gene_list[i]
                for mutation in mutations:
                    if mutation != original:
                        gene_list[i] = mutation
                        new_gene = ''.join(gene_list)
                        if new_gene in bank_set:
                            queue.append((new_gene, num_mutations + 1))
                            bank_set.remove(new_gene)
                gene_list[i] = original
        
        return -1
