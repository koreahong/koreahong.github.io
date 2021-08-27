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
            #자식끼리 비교
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

    #탐색연산
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

    #삽입연산
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
            #이미 키가 있으면 값만 갱신
            n.value = value
        return n


    #최솟값 찾기
    def min(self) -> Optional[T]:
        if self.root == None:
            return None
        return self.minnum(self.root).value

    def minnum(self, n: Node[T]):
        if n.left == None:
            return n
        return self.minnum(n.left)

    #최솟값 삭제
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


if __name__ == '__main__':
    a = [12,15,67,87,14,19,20,21]
    h = bheap[int](a)
    h.heapify()
    print(h)


