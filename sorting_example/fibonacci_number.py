# -*- coding: utf-8 -*-
"""
This python program prints Fibonacci number

@author: mtandur
"""

def feb_number_gen(num):
    """
    This python function prints given Fibonacci number
    :return:
    """
    print(f'Generate Fibonacci for number: ', num)

    i = 0
    old = 0
    new = 1
    feb_list = [0, 1]

    if num == 1:
        feb_list.append(num)
    else:
        while i <= num:
            feb_num = old + new
            old = new
            new = feb_num
            #print(f'feb_num = ', feb_num)
            feb_list.append(feb_num)
            i = i + 1
    print(f'Fibonacci number: ', feb_list)

feb_number_gen(2)
