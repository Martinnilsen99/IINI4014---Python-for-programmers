# A simple program with the main purpose of sorting a list of words by size and lexicographically
from tabulate import tabulate


def generateListFromFile(filename):
    with open(filename) as file:
        # This removes all the special characters and splits all the lines into a list
        listOfLines = file.read().translate(
            dict.fromkeys(map(ord, u",!.;?:"))).splitlines()
        ListWithoutEmptyLines = list(filter(None, listOfLines))
    return ListWithoutEmptyLines


# This method swaps two elements in a list
def swapElements(unsorted_list, indexOne, indexTwo):
    temp = unsorted_list[indexOne]
    unsorted_list[indexOne] = unsorted_list[indexTwo]
    unsorted_list[indexTwo] = temp


def bubbleSort(unsorted_list):  # Standard bubblesort
    sorted_list = []
    for x in unsorted_list:
        sorted_list.append(x)
    for i in range(len(sorted_list) - 1, 0, -1):
        for j in range(i):
            if len(sorted_list[j]) > len(sorted_list[j + 1]):
                # If the first word is longer than the second, swap places
                swapElements(sorted_list, j, (j + 1))
            elif len(sorted_list[j]) == len(sorted_list[j + 1]):
                # If the words has the same length, sort lexicographically
                if sorted_list[j] > sorted_list[j + 1]:
                    swapElements(sorted_list, j, (j + 1))
    return sorted_list


def main():
    filename = "./Strings.txt"
    unsorted_list = generateListFromFile(filename)
    sorted_list = bubbleSort(unsorted_list)
    print(tabulate(zip(unsorted_list, sorted_list),
                   headers=["Usortert", "Sortert"]))


if __name__ == "__main__":
    main()
