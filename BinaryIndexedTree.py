# 树状数组或二叉索引树
# 用于计算前缀和与区间问题
# O(logn)的单点修改和区间查询


class BinaryIndexedTree:

    def __init__(self, array):
        size = len(array)
        self.bitree = [0] * (size+1)
        self.array = [0] * size
        for i in range(size):
            if array[i]:
                self.update(i,array[i])


    def query(self, i):
        return self.array[i]
        # return self.get_prefix_sum(i) - self.get_prefix_sum(i-1)

    def update(self,i, v):
        self.array[i]+=v
        index = i+1
        while index<len(self.bitree):
            self.bitree[index] += v
            index += self.lowbit(index)

    def get_prefix_sum(self,i):
        '''
        param i: index in array
        '''
        s = 0
        index = i+1
        while index>0:
            s+=self.bitree[index]
            index -= self.lowbit(index)
        return s

    def get_range_sum(self,l,r):
        return self.get_prefix_sum(r)-self.get_prefix_sum(l-1)

    @staticmethod
    def lowbit(i):
        return i&(-i)

if __name__ == '__main__':
    # array = [2,1,1,9,2,3,4,5,6,7,8,9]
    # array = [1]*38
    array = [1,2,3,4,5,6,7,2,3,4,5,6,7,8,9,10,2,1,2,3,4,5,6,7,8,9,10,2,3,4,2,1,4,5,1,2,4,5]
    bitree = BinaryIndexedTree(array)
    print(bitree.array)
    print(bitree.bitree[1:])
    print(bitree.get_range_sum(2,5))
    print(bitree.get_prefix_sum(4))


