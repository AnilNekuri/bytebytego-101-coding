# ByteByteGo 101 Coding Problems

My Python solutions to the ByteByteGo 101 coding interview problems, listed in the order I completed them.

## Completed problems

1. [Pair Sum](1.pair_summ.py) - Finds two numbers in a sorted array that add up to a target using two pointers.
2. [Triplet Sum](2.triplet_sum.py) - Finds unique triplets whose sum is zero by sorting and reducing the problem to pair sum.
3. [Valid Palindrome](3.is_palindrome.py) - Checks whether a string is a palindrome while ignoring punctuation, spaces, and letter casing.
4. [Largest Container](4.largest_container.py) - Calculates the largest container area using two pointers.
5. [Shift Zeros to the End](5.zero_shift_end.py) - Moves all zeros to the end of an array in place while preserving the order of nonzero values.
6. [Next Lexicographical Sequence](6.next_lexicographical_sequence.py) - Produces the next lexicographically greater arrangement of a string.
7. [Verify Sudoku Board](7.verify_sudoku_board.py) - Validates rows, columns, and 3 x 3 grids with sets.
8. [Zero Striping](8.zero_striping.py) - Sets a matrix cell's entire row and column to zero whenever that cell is zero.
9. [Longest Chain of Consecutive Numbers](9.longest_chain_of_consecutive_numbers.py) - Uses a set to find the longest consecutive sequence in an unsorted array.
10. [Geometric Sequence Triplets](10.geometric_sequence_triplets.py) - Counts geometric-progression triplets using frequency maps on both sides of each value.
11. [Linked List Reversal](11.linked_list_reversal.py) - Reverses a singly linked list with iterative and recursive implementations.
12. [Remove Kth Node from the End](12.remove_kth_last_node.py) - Removes the node that is k positions from the end of a singly linked list using a dummy head and two pointers.
13. [Linked List Intersection](13.linked_list_intersection.py) - Finds the first common node in two singly linked lists by traversing both lists with two pointers.
14. [LRU Cache](14.lru_cache.py) - Implements a least-recently-used cache with a hashmap and a doubly linked list, evicting the least recently used entry when capacity is exceeded.

## Running a solution

Each numbered file can be run directly with Python. For example:

```powershell
python .\11.linked_list_reversal.py
```

The linked-list solution uses the shared `ListNode` class in [ds.py](ds.py).
