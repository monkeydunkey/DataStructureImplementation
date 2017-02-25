class minHeap(object):
    def __init__(self):
        self.arr = []
    def percolate_up(self, arr, ind):
        if ind == 0:
            return arr
        parent = (ind-1)/2
        if arr[parent] > arr[ind]:
            arr[ind], arr[parent] = arr[parent], arr[ind]
            return self.percolate_up(arr, parent)
        else:
            return arr
    def insert(self, value):
        self.arr.append(value)
        self.arr = self.percolate_up(self.arr, len(self.arr) -1)

    def percolate_down(self, arr, parent):
        if len(arr) <= 1 or 2*(parent +1) >= len(arr):
            return arr
        left_child = 2*(parent + 1) - 1
        right_child = left_child + 1
        if arr[parent] < min(arr[left_child], arr[right_child]):
            return arr
        else:
            if arr[left_child] < arr[right_child]:
                arr[parent], arr[left_child] = arr[left_child], arr[parent]
                return self.percolate_down(arr, left_child)
            else:
                arr[parent], arr[right_child] = arr[right_child], arr[parent]
                return self.percolate_down(arr, right_child)

    def delete_min(self):
        self.arr[-1], self.arr[0] = self.arr[0], self.arr[-1]
        del self.arr[-1]
        self.arr = self.percolate_down(self.arr, 0)


if __name__ == '__main__':
    heap = minHeap()
    heap.insert(10)
    print heap.arr
    heap.insert(3)
    print heap.arr
    heap.insert(11)
    print heap.arr
    heap.insert(2)
    print heap.arr
    heap.insert(1)
    print heap.arr
    heap.insert(7)
    print heap.arr
    heap.delete_min()
    heap.delete_min()
    print heap.arr
    heap.delete_min()
    print heap.arr
