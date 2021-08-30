import unittest
from typing import Optional, List, Generic, TypeVar

T = TypeVar("T")


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


class Node(Generic[T]):
    __slots__ = ("item", "next")

    def __init__(self, item: T, pointer: Optional["Node"] = None):
        self.item = item
        self.next: Optional["Node"] = pointer


class linkedlist(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = Node(item=None)

    @property
    def length(self) -> int:
        node: Node = self.head.next
        cnt: int = 0
        while node:
            cnt += 1
            node = node.next
        return cnt

    def __str__(self) -> str:
        node: Node = self.head.next
        result: str = ''
        while node.next:
            result += str(node.item) + ", "
            node = node.next
        return result + str(node.item)


class Stack(Generic[T], linkedlist[T]):
    def push(self, item: T) -> None:
        new_node: Node[T] = Node[T](item=item)
        node: Node = self.head
        while node.next:
            node = node.next
        node.next = new_node
        return

    def pop(self) -> T:
        node = self.head
        if not node.next:
            raise ValueError("stack is empty")

        while node.next.next:
            node = node.next
        temp = node.next
        node.next = node.next.next
        return temp.item


class Queue(Generic[T], linkedlist[T]):
    def append(self, item: T) -> None:
        new_node: Node[T] = Node[T](item=item)
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node
        return

    def popleft(self) -> T:
        node = self.head
        if not node.next:
            raise ValueError(" is empty")
        else:
            temp = node.next
            node.next = node.next.next
            return temp.item


class bheap(Generic[T]):
    def __init__(self, lst: List[T]):
        self.lst = lst
        self.N = len(lst) - 1

    def heapify(self) -> None:
        for i in range(self.N // 2, 0, -1):
            self.downheap(i)

    def downheap(self, i: int) -> None:
        while i * 2 <= self.N:
            k = i * 2
            # 자식끼리 비교
            if k < self.N and self.lst[k] > self.lst[k + 1]:
                k += 1
            if self.lst[k] > self.lst[i]:
                break
            self.lst[k], self.lst[i] = self.lst[i], self.lst[k]
            i = k

    def heappush(self, value) -> None:
        self.lst.append(value)
        self.N += 1
        self.upheap(self.N)

    def upheap(self, j) -> None:
        while j > 1 and self.lst[j] < self.lst[j // 2]:
            self.lst[j], self.lst[j // 2] = self.lst[j // 2], self.lst[j]
            j //= 2

    def heappop(self) -> Optional[T]:
        if self.N == 0:
            return None
        minnum = self.lst[1]
        self.lst[1], self.lst[-1] = self.lst[-1], self.lst[1]
        del self.lst[-1]
        self.N -= 1
        self.downheap(1)
        return minnum

    def __str__(self) -> str:
        return " ".join(map(str, self.lst))


class Node(Generic[T]):
    """
    tree node
    """

    def __init__(self, key: T, value: T, left: Optional["Node"] = None, right: Optional["Node"] = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST(Generic[T]):
    def __init__(self):
        self.root = None

    # 탐색연산
    def get(self, k: T) -> Optional[T]:
        return self.get_item(self.root, k)

    def get_item(self, n: Node[T], k: T) -> Optional[T]:
        if n == None:
            return None
        if n.key > k:
            return self.get_item(n.left, k)
        elif n.key < k:
            return self.get_item(n.right, k)
        else:
            return n.value

    # 삽입연산
    def put(self, key: T, value: T) -> None:
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n: Node[T], key: T, value: T):
        if n == None:
            return Node(key, value)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            # 이미 키가 있으면 값만 갱신
            n.value = value
        return n

    # 최솟값 찾기
    def min(self) -> Optional[T]:
        if self.root == None:
            return None
        return self.minnum(self.root).value

    def minnum(self, n: Node[T]):
        if n.left == None:
            return n
        return self.minnum(n.left)

    # 최솟값 삭제
    def delete_min(self) -> None:
        if self.root == None:
            raise ValueError
        self.root = self.del_min(self.root)

    def del_min(self, n: Node[T]) -> Optional[Node[T]]:
        if n.left == None:
            return n.right
        n.left = self.del_min(n.left)
        return n

    def delete(self, key: T) -> None:
        self.root = self.del_node(self.root, key)

    def del_node(self, n: Node[T], key: T) -> Optional[Node[T]]:
        if n == None:
            return None
        if n.key > key:
            n.left = self.del_node(n.left, key)
        elif n.key < key:
            n.right = self.del_node(n.right, key)
        else:
            if n.left == None:
                return n.right
            if n.right == None:
                return n.left
            target = n
            new_n = self.minnum(target.right)
            new_n.right = self.del_min(target.right)
            new_n.left = target.left
            return new_n


###정렬

## 선택정렬
class sortType(Generic[T]):
    def __init__(self, lst: List) -> None:
        self.lst = copy.deepcopy(lst)

    def sort(self):
        pass


class selection_sort(sortType[T]):
    def __init__(self):
        super().__init__()

    def sort(self):
        copy: List = self.lst.copy()
        for i in range(len(copy) - 1):
            minnum: int = i
            for j in range(i, len(copy)):
                if copy[i] > copy[j]:
                    minnum = j
            copy[j], copy[minnum] = copy[minnum], copy[j]


# class insertion_sort(sortType(Generic[T])):
#     def sort(self) -> copy[T]:
#         super().__init__()
#         copy: List = self.lst.copy()
#         for i in range(1, len(copy)):
#             for j in range(i, 0, -1):
#                 if copy[i - 1] > copy[j]:
#                     copy[j], copy[j - 1] = copy[j - 1], copy[j]
#         return copy
import copy
class heap_sort(sortType[T]):
    def __init__(self, lst: List):
        super().__init__(copy.deepcopy(lst))
        self.create_heap()
        self.sort()

    def sort(self) -> List[T]:
        N = len(self.lst) - 1
        for i in range(N):
            self.lst[1], self.lst[N] = self.lst[N], self.lst[1]
            self.downheap(1, N - 1)
            N -= 1

    def create_heap(self) -> None:
        hsize: int = len(self.lst) - 1
        for i in reversed(range(1, hsize // 2 + 1)):
            self.downheap(i, hsize)

    def downheap(self, i: int, size: int):
        while i * 2 <= size:
            k = i * 2
            if k < size and self.lst[k] < self.lst[k + 1]:
                k += 1
            if self.lst[i] >= self.lst[k]:
                break
            self.lst[i], self.lst[k] = self.lst[k], self.lst[i]
            i = k

#병합정렬 -nlogn
class merge_sort(sortType[T]):
    def __init__(self, lst):
        self.lst = self.sort(copy.deepcopy(lst))


    def sort(self, lst):
        if len(lst) < 2:
            return lst

        #분할
        mid = len(lst) // 2
        low = self.sort(lst[:mid])
        high = self.sort(lst[mid:])
        #해결
        merged_lst = []
        l = h = 0
        while l < len(low) and h < len(high):
            if low[l] < high[h]:
                merged_lst.append(low[l])
                l += 1
            else:
                merged_lst.append(high[h])
                h += 1
        merged_lst += low[l:]
        merged_lst += high[h:]
        #정복
        return merged_lst

#퀵정렬 / [참고](https://mong9data.tistory.com/48)
class quick_sort(sortType[T]):
    def __init__(self, lst):
        self.lst = self.sort(copy.deepcopy(lst), 0, len(lst) - 1)

    def sort(self, lst, low, high):
        if low < high:
            pivot = self.partition(lst, low, high)
            self.sort(lst, low, pivot - 1)
            self.sort(lst, pivot + 1, high)
        return lst

    def partition(self, lst, pivot, high):
        left = pivot + 1
        right = high
        while True:
            while left < high and lst[left] < lst[pivot]:
                left += 1
            while right > pivot and lst[right] > lst[pivot]:
                right -= 1
            if right <= left:
                break
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        lst[pivot], lst[right] = lst[right], lst[pivot]
        return right

### 크루스칼
class kruskal:
    def __init__(self, lst: List):
        self.lst = lst

    def result(self) -> List:
        mst = []
        p = []
        N = len(set(num[1] for num in self.lst])) - 1
        for i in range(N):
            p.append(i)
        tree_edges = 0
        mst_cost = 0
        while True:
            if tree_edges == N - 1:
                break
            u, v
if __name__ == '__main__':
    a = [12, 15, 67, 87, 14, 19, 20, 21]
    h = quick_sort(a)
    print(h.lst)