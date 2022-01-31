def counting_sort(array):
    mx = max(array)
    nl = [0 for i in range(mx + 1)]
    rl = []
    for i in array:
        nl[i] += 1
    for i in range(len(nl)):
        if nl[i] != 0:
            rl += [i for n in range(nl[i])]
    return rl


def main():
    ls = []
    size = int(input("Input range? "))

    for i in range(1, size + 1):
        ls.append(int(input("Enter Numbers {} : ".format(i))))
    result = counting_sort(ls)
    print("Sorted array is", result)

    def search():
        find = int(input("Search for Number: "))
        try:
            idx = result.index(find)
            print('The index of {} is {} '.format(find, idx))
        except ValueError:
            print("Can't find Number {}".format(find))
    print(search())


main()