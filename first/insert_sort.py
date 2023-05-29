class SequentialInsertionSort:
    def sort(self, array):
        """
        Сортує масив за допомогою алгоритму сортування вставкою (sequential insertion sort).

        Параметри:
        array (list): Масив, який потрібно відсортувати.

        Повертає:
        list: Відсортований масив.
        """
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array


import concurrent.futures


class ParallelInsertionSort:
    def sort(self, array):
        """
        Сортує масив за допомогою паралельного алгоритму сортування вставкою (parallel insertion sort).

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

            sorted_left = left_future.result()
            sorted_right = right_future.result()

        return self.merge(sorted_left, sorted_right)

    def merge(self, left, right):
        """
        Об'єднує два відсортованих масиви в один відсортований масив.

        Параметри:
        left (list): Відсортований масив.
        right (list): Відсортований масив.

        Повертає:
        list: Об'єднаний та відсортований масив.
        """
        merged = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged