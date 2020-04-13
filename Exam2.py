# Exam 2 -- Benjamin Lemery
import Search_Methods
import random

# Part 1
list = []

# Part 2
while True:
    menu_selection = int(input("Select which algorithm you wish to use. Press 1-5\n"
                               "Enter 1 to use Bubble Sort\n"
                               "Enter 2 to use Selection Sort\n"
                               "Enter 3 to use Insertion Sort\n"
                               "Enter 4 to use Merge Sort\n"
                               "Enter 5 to use Quick Sort\n"
                               "Press 6 to exit\n"
                               "Enter a number: "))
    # Part 6
    if menu_selection == 6:
        exit()
    # Part 3
    numbers_to_sort_selection = int(input("Enter how many numbers you wish to sort: "))

    for i in range(0, numbers_to_sort_selection):
        num = random.randrange(0,100000)
        list.append(num)

    # Part 4
    if menu_selection == 1:
        sort = Search_Methods.bubble_sort(list)
    elif menu_selection == 2:
        sort = Search_Methods.selection_sort(list)
    elif menu_selection == 3:
        sort = Search_Methods.insertion_sort(list)
    elif menu_selection == 4:
        sort = Search_Methods.merge_sort(list)
    elif menu_selection == 5:
        sort = Search_Methods.quick_sort(list)


    print("\n""The sorted list values are: " + str(list) + "\n")

    # Part 5
    list = []


