import random
import time
import matplotlib.pyplot as plt

# -------------------------
# Алгоритми сортування
# -------------------------


def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]  # Середній елемент
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


# -------------------------
# Вимірювання часу
# -------------------------


def measure_time(sort_fn, arr, repeats=5):
    times = []
    for _ in range(repeats):
        copy_arr = arr.copy()
        start = time.perf_counter()
        sort_fn(copy_arr)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)


# -------------------------
# Тестування
# -------------------------

sizes = [10_000, 50_000, 100_000, 500_000]
results_random = []
results_deterministic = []

print("Починаємо тестування...\n")
for size in sizes:
    test_array = [random.randint(0, 1_000_000) for _ in range(size)]
    print(f"Розмір масиву: {size}")

    rand_time = measure_time(randomized_quick_sort, test_array)
    det_time = measure_time(deterministic_quick_sort, test_array)

    print(f"  Рандомізований QuickSort: {rand_time:.4f} секунд")
    print(f"  Детермінований QuickSort: {det_time:.4f} секунд\n")

    results_random.append(rand_time)
    results_deterministic.append(det_time)

# -------------------------
# Графік
# -------------------------

plt.figure(figsize=(10, 6))
plt.plot(sizes, results_random, marker="o", label="Рандомізований QuickSort")
plt.plot(sizes, results_deterministic, marker="s", label="Детермінований QuickSort")
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння QuickSort алгоритмів")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------
# Висновок
# -------------------------

print("Висновок:")
for i, size in enumerate(sizes):
    faster = (
        "рандомізований"
        if results_random[i] < results_deterministic[i]
        else "детермінований"
    )
    print(f"  Для масиву розміром {size} швидший був {faster} QuickSort.")
