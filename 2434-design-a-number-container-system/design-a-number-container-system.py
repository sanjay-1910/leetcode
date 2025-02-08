# from collections import defaultdict,Sortedset

class NumberContainers:

    def __init__(self):
        self.index_dic = {}  # Maps index -> number
        self.num_dic = defaultdict(SortedSet)  # Maps number -> set of indices

    def change(self, index: int, number: int) -> None:
        if index not in self.index_dic:
            self.index_dic[index] = number
            self.num_dic[number].add(index)
        else:
            old_number = self.index_dic[index]
            self.num_dic[old_number].remove(index)  # Remove index from old number's set
            #we can also use discard to remove elements from the SortedSet
            # if not self.num_dic[old_number]:  # Remove empty set
            #     del self.num_dic[old_number]
            self.index_dic[index] = number
            self.num_dic[number].add(index)
    def find(self, number: int) -> int:
        if(number not in self.num_dic or not self.num_dic[number]):
            return -1
        else:
            return self.num_dic[number][0]



        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)