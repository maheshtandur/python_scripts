"""
Sort the number 
Even Before sortingt 1: [8, 6, 4, 2, 1, 3, 5, 7, 9, 13, 17, 19, 25]
Even after sorting   2: [25, 19, 17, 13, 9, 8, 7, 6, 5, 4, 3, 2, 1]
"""

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
