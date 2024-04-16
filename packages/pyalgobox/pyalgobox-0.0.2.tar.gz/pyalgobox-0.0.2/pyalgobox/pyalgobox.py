import timeit
import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

class SortingAlgorithm:
    def sort(self, arr: list) -> list:
        raise NotImplementedError
    def time(self, arr: list) -> float:
        start_time = timeit.default_timer()
        self.sort(arr.copy())
        end_time = timeit.default_timer()
        return end_time - start_time


class BubbleSort(SortingAlgorithm):
    def sort(self, arr: list) -> list:
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class InsertionSort(SortingAlgorithm):
    def sort(self, arr: list) -> list:
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


class SelectionSort(SortingAlgorithm):
    def sort(self, arr: list) -> list:
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

class MergeSort(SortingAlgorithm):
    def sort(self,arr: list) -> list:
        if len(arr) > 1:
            r = len(arr)//2
            L = arr[:r]
            M = arr[r:]
            self.sort(L)
            self.sort(M)
            i = j = k = 0
            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = M[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(M):
                arr[k] = M[j]
                j += 1
                k += 1
        return arr

class QuickSort(SortingAlgorithm):
    def sort(self, arr: list) -> list:
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class HeapSort(SortingAlgorithm):
    def sort(self, arr: list) -> list:
        if len(arr) <= 1:
            return arr
        self.heapify(arr)
        for i in range(len(arr) - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr[:i])
        return arr

    def heapify(self, arr: list) -> None:
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(arr, n, i)

    def max_heapify(self, arr: list, n: int, i: int) -> None:
        left = 2 * i + 1
        right = 2 * i + 2
        max_index = i
        if left < n and arr[left] > arr[max_index]:
            max_index = left
        if right < n and arr[right] > arr[max_index]:
            max_index = right
        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]
            self.max_heapify(arr, n, max_index)

class CountingSort(SortingAlgorithm):
    def sort(self, arr: list) -> list:
        if len(arr) <= 1:
            return arr
        min_value = min(arr)
        max_value = max(arr)
        range_size = max_value - min_value + 1
        count_arr = [0] * range_size
        output_arr = [0] * len(arr)
        for num in arr:
            count_arr[num - min_value] += 1
        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i - 1]
        for num in arr[::-1]:
            output_arr[count_arr[num - min_value] - 1] = num
            count_arr[num - min_value] -= 1
        return output_arr

class RadixSort(SortingAlgorithm):
    def sort(self, arr: list) -> list:
        if len(arr) <= 1:
            return arr
        max_value = max(arr)
        max_digits = len(str(max_value))
        for i in range(max_digits):
            buckets = [[] for _ in range(10)]
            for num in arr:
                digit = (num // (10 ** i)) % 10
                buckets[digit].append(num)
            arr = [num for bucket in buckets for num in bucket]

def comparebarn(n: int) -> None:
    arr = [random.randint(1, 100000) for _ in range(n)]
    bubble_sort = BubbleSort()
    bubble_sort_time = bubble_sort.time(arr)

    insertion_sort = InsertionSort()
    insertion_sort_time = insertion_sort.time(arr)

    selection_sort = SelectionSort()
    selection_sort_time = selection_sort.time(arr)

    merge_sort = MergeSort()
    merge_sort_time=merge_sort.time(arr)

    quick_sort=QuickSort()
    quick_sort_time=quick_sort.time(arr)

    heap_sort=HeapSort()
    heap_sort_time=heap_sort.time(arr)

    counting_sort=CountingSort()
    counting_sort_time=counting_sort.time(arr)

    radix_sort=RadixSort()
    radix_sort_time=radix_sort.time(arr)

    threshold = 0.01

    if max(bubble_sort_time, insertion_sort_time, selection_sort_time,merge_sort_time,quick_sort_time,heap_sort_time,counting_sort_time,radix_sort_time) < threshold:
        scale = 'log'
    else:
        scale = 'linear'
    algorithms = ['Bubble Sort', 'Insertion Sort', 'Selection Sort','Merge Sort','Quick Sort','Heap Sort','Counting Sort','Radix Sort']
    times = [bubble_sort_time, insertion_sort_time, selection_sort_time,merge_sort_time,quick_sort_time,heap_sort_time,counting_sort_time,radix_sort_time]
    cmap = LinearSegmentedColormap.from_list('gradient', ['#355C7D', '#6C5B7B', '#C06C84'])
    plt.bar(algorithms, times, color=[cmap(i / len(algorithms)) for i in range(len(algorithms))])
    plt.xlabel('Sorting Algorithms', fontsize=12)
    plt.ylabel('Average Execution Time (seconds)' if scale == 'linear' else 'Logarithmic Scale', fontsize=12)
    plt.title(f'Comparison of Time Complexities for n = {n} (scale={scale})', fontsize=14)
    plt.yscale(scale)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def comparebar(arr: list) -> None:
    bubble_sort = BubbleSort()
    bubble_sort_time = bubble_sort.time(arr)

    insertion_sort = InsertionSort()
    insertion_sort_time = insertion_sort.time(arr)

    selection_sort = SelectionSort()
    selection_sort_time = selection_sort.time(arr)

    merge_sort = MergeSort()
    merge_sort_time=merge_sort.time(arr)

    quick_sort=QuickSort()
    quick_sort_time=quick_sort.time(arr)

    heap_sort=HeapSort()
    heap_sort_time=heap_sort.time(arr)

    counting_sort=CountingSort()
    counting_sort_time=counting_sort.time(arr)

    radix_sort=RadixSort()
    radix_sort_time=radix_sort.time(arr)

    threshold = 0.01

    if max(bubble_sort_time, insertion_sort_time, selection_sort_time,merge_sort_time,quick_sort_time,heap_sort_time,counting_sort_time,radix_sort_time) < threshold:
        scale = 'log'
    else:
        scale = 'linear'
    algorithms = ['Bubble Sort', 'Insertion Sort', 'Selection Sort','Merge Sort','Quick Sort','Heap Sort','Counting Sort','Radix Sort']
    times = [bubble_sort_time, insertion_sort_time, selection_sort_time,merge_sort_time,quick_sort_time,heap_sort_time,counting_sort_time,radix_sort_time]
    cmap = LinearSegmentedColormap.from_list('gradient', ['#355C7D', '#6C5B7B', '#C06C84'])
    plt.bar(algorithms, times, color=[cmap(i / len(algorithms)) for i in range(len(algorithms))])
    plt.xlabel('Sorting Algorithms', fontsize=12)
    plt.ylabel('Average Execution Time (seconds)' if scale == 'linear' else 'Logarithmic Scale', fontsize=12)
    plt.title(f'Comparison of Time Complexities for array = {arr} (scale={scale})', fontsize=14)
    plt.yscale(scale)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def compareplotn(n: int) -> None:
    arr = [random.randint(1, 100000) for _ in range(n)]
    bubble_sort = BubbleSort()
    bubble_sort_time = bubble_sort.time(arr)

    insertion_sort = InsertionSort()
    insertion_sort_time = insertion_sort.time(arr)

    selection_sort = SelectionSort()
    selection_sort_time = selection_sort.time(arr)

    merge_sort = MergeSort()
    merge_sort_time=merge_sort.time(arr)

    quick_sort=QuickSort()
    quick_sort_time=quick_sort.time(arr)

    heap_sort=HeapSort()
    heap_sort_time=heap_sort.time(arr)

    counting_sort=CountingSort()
    counting_sort_time=counting_sort.time(arr)

    radix_sort=RadixSort()
    radix_sort_time=radix_sort.time(arr)

    threshold = 0.01

    if max(bubble_sort_time, insertion_sort_time, selection_sort_time,merge_sort_time,quick_sort_time,heap_sort_time,counting_sort_time,radix_sort_time) < threshold:
        scale = 'log'
    else:
        scale = 'linear'

    algorithms = ['Bubble Sort', 'Insertion Sort', 'Selection Sort','Merge Sort','Quick Sort','Heap Sort','Counting Sort','Radix Sort']
    times = [bubble_sort_time, insertion_sort_time, selection_sort_time,merge_sort_time,quick_sort_time,heap_sort_time,counting_sort_time,radix_sort_time]
    plt.plot(algorithms, times, marker='o')
    plt.xlabel('Sorting Algorithms')
    plt.ylabel('Average Execution Time (seconds)' if scale == 'linear' else 'Logarithmic Scale')
    plt.title(f'Comparison of Time Complexities for n = {n}')
    plt.yscale(scale)
    plt.show()

def compareplot(arr: list) -> None:
    bubble_sort = BubbleSort()
    bubble_sort_time = bubble_sort.time(arr)

    insertion_sort = InsertionSort()
    insertion_sort_time = insertion_sort.time(arr)

    selection_sort = SelectionSort()
    selection_sort_time = selection_sort.time(arr)

    merge_sort = MergeSort()
    merge_sort_time=merge_sort.time(arr)

    quick_sort=QuickSort()
    quick_sort_time=quick_sort.time(arr)

    heap_sort=HeapSort()
    heap_sort_time=heap_sort.time(arr)

    counting_sort=CountingSort()
    counting_sort_time=counting_sort.time(arr)

    radix_sort=RadixSort()
    radix_sort_time=radix_sort.time(arr)

    threshold = 0.01

    if max(bubble_sort_time, insertion_sort_time, selection_sort_time,merge_sort_time,quick_sort_time,heap_sort_time,counting_sort_time,radix_sort_time) < threshold:
        scale = 'log'
    else:
        scale = 'linear'

    algorithms = ['Bubble Sort', 'Insertion Sort', 'Selection Sort','Merge Sort','Quick Sort','Heap Sort','Counting Sort','Radix Sort']
    times = [bubble_sort_time, insertion_sort_time, selection_sort_time,merge_sort_time,quick_sort_time,heap_sort_time,counting_sort_time,radix_sort_time]
    plt.plot(algorithms, times, marker='o')
    plt.xlabel('Sorting Algorithms')
    plt.ylabel('Average Execution Time (seconds)' if scale == 'linear' else 'Logarithmic Scale')
    plt.title(f'Comparison of Time Complexities for array = {arr}')
    plt.yscale(scale)
    plt.show()

def compare_two_algorithmsn(algorithm1: SortingAlgorithm, algorithm2: SortingAlgorithm, n: int) -> None:
    arr = [random.randint(1, 100000) for _ in range(n)]
    time1 = algorithm1.time(arr)
    time2 = algorithm2.time(arr)
    algorithms = [algorithm1.__class__.__name__, algorithm2.__class__.__name__]
    times = [time1, time2]
    cmap = LinearSegmentedColormap.from_list('gradient', ['#355C7D', '#6C5B7B', '#C06C84'])
    plt.bar(algorithms, times, color=[cmap(i / len(algorithms)) for i in range(len(algorithms))])
    plt.xlabel('Sorting Algorithms', fontsize=12)
    plt.ylabel('Average Execution Time (seconds)', fontsize=12)
    plt.title(f'Comparison of {algorithms[0]} and {algorithms[1]} for n = {n} (scale=linear)', fontsize=14)
    plt.tight_layout()
    plt.show()

def compare_three_algorithmsn(algorithm1: SortingAlgorithm, algorithm2: SortingAlgorithm, algorithm3: SortingAlgorithm, n: int) -> None:
    arr = [random.randint(1, 100000) for _ in range(n)]
    time1 = algorithm1.time(arr)
    time2 = algorithm2.time(arr)
    time3 = algorithm3.time(arr)
    algorithms = [algorithm1.__class__.__name__, algorithm2.__class__.__name__, algorithm3.__class__.__name__]
    times = [time1, time2, time3]
    cmap = LinearSegmentedColormap.from_list('gradient', ['#355C7D', '#6C5B7B', '#C06C84'])
    plt.bar(algorithms, times, color=[cmap(i / len(algorithms)) for i in range(len(algorithms))])
    plt.xlabel('Sorting Algorithms', fontsize=12)
    plt.ylabel('Average Execution Time (seconds)', fontsize=12)
    plt.title(f'Comparison of {algorithms[0]}, {algorithms[1]}, and {algorithms[2]} for n = {n} (scale=linear)', fontsize=14)
    plt.tight_layout()
    plt.show()

def compare_two_algorithms(algorithm1: SortingAlgorithm, algorithm2: SortingAlgorithm, arr: list) -> None:
    time1 = algorithm1.time(arr)
    time2 = algorithm2.time(arr)
    algorithms = [algorithm1.__class__.__name__, algorithm2.__class__.__name__]
    times = [time1, time2]
    cmap = LinearSegmentedColormap.from_list('gradient', ['#355C7D', '#6C5B7B', '#C06C84'])
    plt.bar(algorithms, times, color=[cmap(i / len(algorithms)) for i in range(len(algorithms))])
    plt.xlabel('Sorting Algorithms', fontsize=12)
    plt.ylabel('Average Execution Time (seconds)', fontsize=12)
    plt.title(f'Comparison of {algorithms[0]} and {algorithms[1]} for array = {arr} (scale=linear)', fontsize=14)
    plt.tight_layout()
    plt.show()

def compare_three_algorithms(algorithm1: SortingAlgorithm, algorithm2: SortingAlgorithm, algorithm3: SortingAlgorithm, arr: list) -> None:
    time1 = algorithm1.time(arr)
    time2 = algorithm2.time(arr)
    time3 = algorithm3.time(arr)
    algorithms = [algorithm1.__class__.__name__, algorithm2.__class__.__name__, algorithm3.__class__.__name__]
    times = [time1, time2, time3]
    cmap = LinearSegmentedColormap.from_list('gradient', ['#355C7D', '#6C5B7B', '#C06C84'])
    plt.bar(algorithms, times, color=[cmap(i / len(algorithms)) for i in range(len(algorithms))])
    plt.xlabel('Sorting Algorithms', fontsize=12)
    plt.ylabel('Average Execution Time (seconds)', fontsize=12)
    plt.title(f'Comparison of {algorithms[0]}, {algorithms[1]}, and {algorithms[2]} for array = {arr} (scale=linear)', fontsize=14)
    plt.tight_layout()
    plt.show()

def algotime(algorithms: list[SortingAlgorithm], arr: list) -> None:
    times = [algorithm.time(arr) for algorithm in algorithms]
    names = [algorithm.__class__.__name__ for algorithm in algorithms]
    for i, name in enumerate(names):
        print(f"{name}: {times[i]:.10f} seconds")

def algotimen(algorithms: list[SortingAlgorithm], n: int) -> None:
    arr = [random.randint(1, 100000) for _ in range(n)]
    times = [algorithm.time(arr) for algorithm in algorithms]
    names = [algorithm.__class__.__name__ for algorithm in algorithms]
    for i, name in enumerate(names):
        print(f"{name}: {times[i]:.10f} seconds for n = {n}")

bubble = BubbleSort()
insertion = InsertionSort()
selection = SelectionSort()
merge=MergeSort()
quick=QuickSort()
counting=CountingSort()
heap=HeapSort()
radix=RadixSort()