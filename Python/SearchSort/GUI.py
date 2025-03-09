from tkinter import *


def bubble_sort():
    global sorted
    arr = list(map(int, e_sort.get().split()))
    n = len(arr)
    if len(arr) > 1:
        for i in range(n):
            for j in range(0, n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        sort_label.config(text=str(arr))
        sorted = arr


def bin_search():
    global sorted
    if len(sorted) > 0:
        left = 0
        right = len(sorted) - 1
        target = int(e_search.get())
        found = False

        while left <= right:
            mid = (left + right) // 2

            if sorted[mid] > target:
                right = mid - 1

            if sorted[mid] < target:
                left = mid + 1

            else:
                search_label.config(text="Number searched found at position " + str(mid + 1))
                found = True
                break

        if not found:
            search_label.config(text="Number searched not in array")

    else:
        search_label.config(text="No array to search!")
        sort_label.config(text="Please enter array to search")


root = Tk()
root.title("Search Sort")

sorted = []

e_sort = Entry(root, width=30)
sort_button = Button(root, text="Sort", padx=16, pady=10, command=bubble_sort)
sort_label = Label(root, text="Sorted array")

e_search = Entry(root, width=30)
search_button = Button(root, text="Search", padx=10, pady=10, command=bin_search)
search_label = Label(root, text="Position of searched item")

e_sort.grid(row=0, column=0, padx=20, pady=20)
sort_button.grid(row=1, column=0, padx=20, pady=20)
sort_label.grid(row=2, column=0, padx=20, pady=20)
e_search.grid(row=3, column=0, padx=20, pady=20)
search_button.grid(row=4, column=0, padx=20, pady=20)
search_label.grid(row=5, column=0, padx=20)

root.mainloop()
