
FULL_NAME = "edwin"


def build_unsorted_array(full_name):
    letters = []
    seen = set()

    for ch in full_name:
        if not ch.isalpha():
            continue

        key = ch.upper()

        if key in seen:
            continue

        seen.add(key)
        letters.append(key)

    return letters


def selection_sort(arr):
    result = arr[:]
    n = len(result)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j

        if min_index != i:
            result[i], result[min_index] = result[min_index], result[i]

    return result


def main():
    unsorted_array = build_unsorted_array(FULL_NAME)
    sorted_array = selection_sort(unsorted_array)

    print("Full Name:", FULL_NAME)
    print("Unsorted array:", unsorted_array)
    print("Sorted array:  ", sorted_array)


if __name__ == "__main__":
    main()
