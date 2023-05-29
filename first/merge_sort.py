class SequentialMergeSort:
    def sort(self, array):
        """
        Сортує масив за допомогою алгоритму злиття (sequential merge sort).

        Параметри:
        array (list): Масив, який потрібно відсортувати.

        Повертає:
        list: Відсортований масив.
        """
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        left = self.sort(left)
        right = self.sort(right)
        return self.merge(left, right)

    def merge(self, left, right):
        """
        Злиття двох відсортованих масивів у відсортований масив.

        Параметри:
        left (list): Відсортований масив.
        right (list): Відсортований масив.

        Повертає:
        list: Злитий відсортований масив.
        """
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result


import concurrent.futures


class ParallelMergeSort:
    def sort(self, array):
        """
        Сортує масив за допомогою паралельного алгоритму злиття (parallel merge sort).

        Параметри:
        array (list): Масив, який потрібно відсортувати.

        Повертає:
        list: Відсортований масив.
        """
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            left_future = executor.submit(self.sort, left)
            right_future = executor.submit(self.sort, right)

            return self.merge(left_future.result(), right_future.result())

    def merge(self, left, right):
        """
        Злиття двох відсортованих масивів у відсортований масив.

        Параметри:
        left (list): Відсортований масив.
        right (list): Відсортований масив.

        Повертає:
        list: Злитий відсортований масив.
        """
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result