class SequentialQuicksort:
    def sort(self, array):
        """
        Сортує масив за допомогою алгоритму швидкого сортування (sequential quicksort).

        Параметри:
        array (list): Масив, який потрібно відсортувати.

        Повертає:
        list: Відсортований масив.
        """
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return self.sort(left) + middle + self.sort(right)


import concurrent.futures


class ParallelQuicksort:
    def sort(self, array):
        """
        Сортує масив за допомогою паралельного алгоритму швидкого сортування (parallel quicksort).

        Параметри:
        array (list): Масив, який потрібно відсортувати.

        Повертає:
        list: Відсортований масив.
        """
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            left_future = executor.submit(self.sort, left)
            right_future = executor.submit(self.sort, right)

            return left_future.result() + middle + right_future.result()