#%% md
# More examples on different type of sprting
#### For more information refer to the <a href = 'https://docs.python.org/3.7/library/string.html'>Python Documentation</a>
#%%

#%% md
# Sorting even number first.
Example: Ascending Soretd List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 17, 19, 25]
Even First sorted List 1: [8, 6, 4, 2, 1, 3, 5, 7, 9, 13, 17, 19, 25]
#%%
def sort_even_num_first(num_list):
    print (f'Default List: {num_list}')
    list_len = len(num_list)
    sorted_list_1 = []
    sorted_list_2 = []
    for i in range(0, (list_len)): # This for  loop give index value of list
        #print (i) # This print index valuev of list
        # < gives ascending order list
        #c>cgives descending order list
        for j in range((i+1), list_len):
            if num_list[i] > num_list[j]:
                num_list[i] = num_list[i] * num_list[j]
                num_list[j] = num_list[i]//num_list[j]
                num_list[i] = num_list[i]//num_list[j]                 
        if num_list[i]%2 != 0:
            print(num_list[i])
            sorted_list_1.append(num_list[i])
            sorted_list_2.insert(0, num_list[i])
        else:
            sorted_list_1.insert(0, num_list[i])
            sorted_list_2.insert(0, num_list[i])    
    print (f'Ascending Soretd List: {num_list}')
    print (f'Even First sorted List 1: {sorted_list_1}')
    print (f'Even First sorted List 2: {sorted_list_2}')

num_list = [1,5,2,7,6,3,4,9,8,25,19,13,17]
sort_even_num_first(num_list)


#%% md
# Bubble sorting example
 A bubble sort will compare the first and second elements
#%%
def bubble_sort(my_list):
    print("unsorted List: ", my_list)

    list_len = len(my_list)
    print("length: ", list_len)
    for i in range(len(my_list)):
        # print (i)
        for j in range((i + 1), len(my_list)):
            if my_list[i] > my_list[j]:
                my_list[i] = my_list[i] * my_list[j]
                my_list[j] = my_list[i] // my_list[j]
                my_list[i] = my_list[i] // my_list[j]
    print("Sorted List: ", my_list)


test = [6, 5, 8, 2, 3, 45, 87, 24, 70]
bubble_sort(test)

#%% md
# Selection sorting example
The selection sort finds the smallest or highest values in each iteration 
and moves those values to the ordered list.
#%%
def selection_sort(my_list):
    print("unsorted List: ", my_list)
    list_len = len(my_list)
    print("length: ", list_len)
    for i in range(0, len(my_list)):
        print (i)
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[i]:
                my_list[i] = my_list[i] * my_list[j]
                my_list[j] = my_list[i]//my_list[j]
                my_list[i] = my_list[i]//my_list[j]
        print("-->", my_list)
    print("Sorted List: ", my_list)

test = [6, 5, 8, 2, 3, 45, 87, 24, 70]
selection_sort(test)

#%% md
# Linear search: Searching a string/char one by one in a list or sting
#%% 
def linear_searchh(my_list, item):
    i = 0
    found = "No"
    print (f"List to be searched: {my_list}")
    while i < len(my_list):
        if (my_list[i] == item):
            found = "Yes"
        i += 1
    if found == "No":
        print(f'The number your searching \"{item}\" is not in the list: ')
    else:
        print(f'The number: \"{item}\" is found in the list: ')

my_list = [6,5,8,2,3,45,87,24,70]
linear_searchh(my_list, 87)

#%% md
# Binary search: Searches a string/char by dividing the list in two half.
#%%
def binary_search(my_list, item):
    print ("Initial sorted list to be searched: ", my_list)
    found = "No"
    first = 0
    last = len(my_list) - 1

    while first <= last and found == "No":
        print (f'first: {first} and Last: {last}')
        midpoint = (first + last)//2
        print ('===> midpoint ', midpoint)
        print ('my_list[midpoint] value: ', my_list[midpoint])
        if my_list[midpoint] == item:
            print(f'The number: \"{item}\" is found in the list...!!! ')
            found = "Yes"
        else:
            if my_list[midpoint] < item:
                first = midpoint + 1
                print ('===== first ', first)
            else:
                last = midpoint -1
                print ('===== last ', last)

my_list = [6,5,8,2,3,45,87,24,70]
test = sorted(my_list)
binary_search(test, 87)

#%% md
# Insertion sort: sorting the list by exchanging the items.
#%% 
def insertion_sort(my_list):
    print (f"Default un sorted List: {my_list}")
    
    a_my_list = my_list
    # Ascending Sort
    for i in range(len(a_my_list)):
        j = i + 1 
        for j in range(len(a_my_list)):
            if a_my_list[i] < a_my_list[j]:
                temp = a_my_list[i]
                a_my_list[i] = a_my_list[j]
                a_my_list[j] = temp
    print (f'Ascending Soretd List: {a_my_list}')
    
    # descending Sort
    d_my_list = my_list
    for i in range(len(d_my_list)):
        j = i + 1 
        for j in range(len(d_my_list)):
            if d_my_list[i] > d_my_list[j]:
                temp = d_my_list[i]
                d_my_list[i] = d_my_list[j]
                d_my_list[j] = temp
    print ('descending Soretd List: %s'% d_my_list)

my_list = [6,5,5, 8,2,3,45, 8, 87,24,70]
insertion_sort(my_list)

#%% md
# Print example:
#%%
name = "Mahesh Tandur"
age = 42
string = "\nHello %s and my age is %i" % (name, age)
print (string)
print ('--->  %s ' % string)

#%% md
# xxxx
#%%



#%% md
# xxxx
#%%
