#Binary search algorithm
class Main:
    def binSearch(arr, target):
        left = 0
        right = len(arr) -1

        while left <= right:#while left and right keep their position
            mid = (left + right) // 2#set mid to middle of working set

            if arr[mid] == target:#if mid is the target return the target
                return mid + 1

            if arr[mid] < target:#if mid is less then target left is now one greater then mid
                left = mid + 1

            else:#if mid is greater then target right is now one lest then mid
                right = mid -1

        #if not found
        return -1

    #Bouble sort algorithm
    def boubleSort(arr):
        n = len(arr)
        swapped = False

        for i in range(n):#same as (int i = 0; i< n-1; i++) so loop continues till all arr done
            swapped = False

            for j in range(0, n - 1 - i):#also loops till array is done
                if arr[j] > arr[j+1]:#if first number is bigger than second swap them
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    # This is equivalent to:
                    # temp = arr[j]
                    # arr[j] = arr[j + 1]
                    # arr[j + 1] = temp

                    swapped = True

            if not swapped:#ie all are in order
                break

        return arr

    if __name__ == '__main__':
        arr = list(map(int, input("Please enter the array to be searched: ").split()))#get the user to input a numbers to sort
        #input gets the user input as a string
        #split splits the input into different variables divided by white spaces
        #map(int) converts these inputs from string variables to int values
        #list turns these values into a list/array

        sortedArr = boubleSort(arr)
        print(sortedArr)

        target = int(input("What is the target number? :"))

        position = binSearch(sortedArr, target)
        if position == -1:
            print("The target number,", target, "wasn't in the array")

        else:
            print("The target number", target, "was found at the position", position)



