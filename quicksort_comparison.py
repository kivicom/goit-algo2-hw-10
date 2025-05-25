import random
import timeit
import matplotlib.pyplot as plt
from tabulate import tabulate

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # Останній елемент як опорний
    left = []
    right = []
    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr)-1)]  # Випадковий опорний елемент
    left = []
    right = []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
    return randomized_quick_sort(left) + [pivot] * arr.count(pivot) + randomized_quick_sort(right)

def generate_test_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def compare_quicksort_methods():
    sizes = [10_000, 50_000, 100_000, 500_000]
    num_trials = 5
    deterministic_times = []
    randomized_times = []

    for size in sizes:
        deterministic_total = 0
        randomized_total = 0

        for _ in range(num_trials):
            arr = generate_test_array(size)
            
            # Вимірювання часу для детермінованого QuickSort
            deterministic_time = timeit.timeit(lambda: deterministic_quick_sort(arr.copy()), number=1)
            deterministic_total += deterministic_time

            # Вимірювання часу для рандомізованого QuickSort
            randomized_time = timeit.timeit(lambda: randomized_quick_sort(arr.copy()), number=1)
            randomized_total += randomized_time

        # Обчислення середнього часу
        avg_deterministic = deterministic_total / num_trials
        avg_randomized = randomized_total / num_trials
        deterministic_times.append(avg_deterministic)
        randomized_times.append(avg_randomized)

        # Виведення результатів для поточного розміру масиву
        print(f"\nРозмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {avg_randomized:.4f} секунд")
        print(f"   Детермінований QuickSort: {avg_deterministic:.4f} секунд")

    # Побудова таблиці
    table = [[size, f"{r_time:.4f}", f"{d_time:.4f}"] for size, r_time, d_time in zip(sizes, randomized_times, deterministic_times)]
    print("\nТаблиця результатів:")
    print("Розмір масиву | Рандомізований QuickSort (с) | Детермінований QuickSort (с)")
    print("--------------|-----------------------------|-----------------------------")
    print(tabulate(table, tablefmt="plain"))

    # Побудова графіка
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, randomized_times, label="Рандомізований QuickSort", color="blue")
    plt.plot(sizes, deterministic_times, label="Детермінований QuickSort", color="orange")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння продуктивності QuickSort")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Аналіз результатів
    print("\nАналіз:")
    print("Рандомізований QuickSort зазвичай показує кращу продуктивність на великих масивах, оскільки випадковий вибір опорного елемента зменшує ймовірність найгіршого випадку (O(n^2)), який частіше трапляється в детермінованому QuickSort, особливо якщо масив частково відсортований. Однак різниця в продуктивності може бути незначною для випадкових даних.")

if __name__ == "__main__":
    compare_quicksort_methods()
