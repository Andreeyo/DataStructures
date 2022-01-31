class Array:
    my_array = []
    counter = int(input("Enter size of array"))

    for i in range(1, counter+1):
        my_array.append(int(input("Enter digits {}:".format(i))))

    print(my_array)


if __name__ == '__main__':

    access = Array()
    while True:
        action = input("What task do you want to perform? "
                       "[a] clear list,"
                       "[b] add item"
                       "[c] sort list"
                       "[d] number of elements"
                       "[e] minimum and maximum numbers"
                       "[f] average of items"
                       "[g] number prior to minimum")
        if action not in "abcdefg" or len(action) != 1:
            print("Please enter an action")
            continue

        if action == 'a':
            access.my_array.clear()
            print("You have cleared the list")

        elif action == 'b':
            access.my_array.append(int(input("Enter a digit")))
            print("list appended with: ", access.my_array)

        elif action == 'c':
            access.my_array.sort()
            print("sorted array: ", access.my_array)

        elif action == 'd':
            print("Length of array", len(access.my_array))

        elif action == 'e':
            Min = access.my_array[0]
            Max = access.my_array[0]

            for i in access.my_array:
                if i < Min:
                    Min = i
                elif i > Max:
                    Max = i
            print("Min number: {}, Max number: {}".format(Min, Max))

        elif action == 'f':
            average = sum(access.my_array) / len(access.my_array)
            print("Average of list is:", average)

        elif action == 'g':
            index_of_min = access.my_array.index(min(access.my_array))
            if index_of_min == 0:
                print("Index of min is 0, no prior number")
            else:
                print("Prior element to Min:", access.my_array[index_of_min - 1])


