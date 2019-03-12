import unittest
from heap import *

class TestHeap(unittest.TestCase):
        
    def test_01_enqueue(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertTrue(insert)
        self.assertEqual(test_heap.contents(), [10, 6, 9, 2, 5, 7, 8])

    def test_02_dequeue(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.dequeue(), 9)
        self.assertEqual(test_heap.get_size(), 5)
        self.assertEqual(test_heap.contents(), [8, 6, 7, 2, 5])

#    def test_03_heap_contents(self):
#        test_heap = MaxHeap(8)
#        test_heap.build_heap([1, 2, 3])
#        self.assertEqual(test_heap.contents(), [3, 2, 1])

    def test_05_build_heap(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_05_is_empty(self):
        test_heap = MaxHeap(5)
        self.assertTrue(test_heap.is_empty())

    def test_06_is_full(self):
        test_heap = MaxHeap(5)
        built = test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.is_full())

    def test_07_get_heap_cap(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertEqual(test_heap.get_capacity(), 7)

    def test_08_get_size(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.get_size(), 6)

    def test_09_perc_down(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_10_perc_up(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_up(6)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

#    def test_11_heap_sort_ascending(self):
#        test_heap = MaxHeap()
#        list1 = [2, 9, 7, 6, 5, 8]
#        test_heap.heap_sort_ascending(list1)
#        self.assertEqual(test_heap, [2, 5, 6, 7, 8, 9])

    def test_my_enqueue(self):
        heap = MaxHeap()
        self.assertTrue(heap.enqueue(19))
        self.assertEqual(heap.contents(), [19])
        self.assertTrue(heap.enqueue(100))
        self.assertEqual(heap.contents(), [100, 19])
        self.assertTrue(heap.enqueue(36))
        self.assertEqual(heap.contents(), [100, 19, 36])
        self.assertTrue(heap.enqueue(2))
        self.assertTrue(heap.enqueue(3))
        self.assertTrue(heap.enqueue(25))
        self.assertTrue(heap.enqueue(1))
        self.assertEqual(heap.contents(), [100, 19, 36, 2, 3, 25, 1])
        self.assertTrue(heap.enqueue(17))
        self.assertTrue(heap.enqueue(7))
        self.assertEqual(heap.contents(), [100, 19, 36, 17, 3, 25, 1, 2, 7])
        heap2 = MaxHeap(1)
        self.assertTrue(heap2.enqueue(19))
        self.assertEqual(heap2.contents(), [19])
        self.assertFalse(heap2.enqueue(100))

    def test_my_peek(self):
        heap = MaxHeap()
        self.assertTrue(heap.enqueue(19))
        self.assertTrue(heap.peek(), 19)
    
    def test_my_dequeue(self):
        heap = MaxHeap(10)
        heap.build_heap([19, 100, 36, 2, 3, 25, 1, 17, 7])
        self.assertEqual(heap.contents(), [100, 19, 36, 17, 3, 25, 1, 2, 7])
        self.assertEqual(heap.dequeue(), 100)
        self.assertEqual(heap.contents(), [36, 19, 25, 17, 3, 7, 1, 2])
        heap2 = MaxHeap(1)
        self.assertEqual(heap2.dequeue(), None)

    def test_my_get_size(self):
        heap = MaxHeap()
        self.assertTrue(heap.enqueue(19))
        self.assertEqual(heap.get_size(), 1)
        self.assertTrue(heap.enqueue(100))
        self.assertEqual(heap.get_size(), 2)
        
    def test_my_build_heap(self):
        heap = MaxHeap()
        heap.build_heap([19, 100, 36, 2, 3, 25, 1, 17, 7])
        self.assertEqual(heap.contents(), [100, 19, 36, 17, 3, 25, 1, 2, 7])
        heap2 = MaxHeap(1)
        heap2.build_heap([19, 100, 36, 2, 3, 25, 1, 17, 7])
        self.assertEqual(heap2.contents(), [100, 19, 36, 17, 3, 25, 1, 2, 7])
        self.assertEqual(heap2.get_capacity(), 9)

    def test_my_heap_sort_ascending(self):
        heap = MaxHeap()
        list_to_sort = [19, 100, 36, 2, 3, 25, 1, 17, 7]
        heap.heap_sort_ascending(list_to_sort)
        self.assertEqual(list_to_sort, [1, 2, 3, 7, 17, 19, 25, 36, 100])

if __name__ == "__main__":
    unittest.main()
