#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:32:44 2018

@author: zahoornovman
"""

import copy



def read_file(sudoku_file):
    '''
    Reading sudoku puzzle from csv file.
    '''
    
    f = open(sudoku_file,"r")
    sud = []
    for i in range(9):
        line = f.readline()
        line = line.strip('\n')
        sud.append(line.split(sep=','))
    f.close()
    return sud


def replace_nones(sud):
    '''
    Replace every empty str in entire sudoku puzzle to an empty list
    '''
    for List in sud:
        for value in range(9):
            if List[value] == '':
                List[value]= []
    return sud

def printing_my_sudoku():
    print ('____________')
    for line in range(9):
        x='|'
        for element in range(9):
            if type(sud[line][element]) == list:
                x= x+' '
            else:
                x=x+sud[line][element]
            if element == 2 or element == 5:
                x=x+'|'
        print (x+'|')
        if line == 2 or line ==5:
            print ('|-----------|')
    print (' -----------')




def comparing_a_row(line):
    '''
    Comparing a line in sudoku to find possible values for missing numbers.
    This fn checks for  numbers that are missing and then adds them to as 
    possible values to the indexs consisting of lists
    Question: what if they are lists within the list  
    '''
    possible_values = []
    for i in range(1,10):
        if str(i) not in line:
            possible_values.append(str(i))
    # possible_values has to not be empty to account for lines that already have all values
    if possible_values > []: 
        for index in range(9):
            # if element in for loop is a list
            if type(line[index]) == list:
               x= compare_two_lists(line[index],possible_values) 
               line[index] = x
               # if length of new possible value list is 1,
               # then we convert list to int type
               if len(line[index]) is 1:
                   line[index] = line[index][0]


def compare_two_lists(old_possible_values,new_possible_values):
    '''
    This fn compares two lists and returns the unique numbers in the two list
    if first list is empty then it appends the second list to first list and
    returns that list
    '''
    if old_possible_values == []:
        x= old_possible_values + new_possible_values
    elif old_possible_values > []:
        x =  list(set(old_possible_values).intersection(new_possible_values))
    return x
 
def comparing_vertical_columns():
    line = []
    #for loop to access every vertical line(column) in sudoku
    for column in range(9):
        #for loop to access row of each column in sudoku
        for row in range(9):
            line.append(sud[row][column])
       # print(line)
        comparing_a_row(line)
        for i in range(9):
            sud[i][column] = line[i]      
       #print(line)
        line=[]
    
def comparing_horizontal_rows():
        for line in range(9):
            comparing_a_row(sud[line])

   
def comparing_one_block(column,row):      
    temp_line = []
    for x in column:
        for y in row:
            temp_line.append(sud[x][y])
        #print(temp_line)
    comparing_a_row(temp_line)
    index=0
    for x in column:
        for y in row:
            sud[x][y]=temp_line[index]
            index += 1     
    temp_line = []
   
def comparing_blocks():
    indexes=[[0,1,2],[3,4,5],[6,7,8]]
    for x in indexes:
        for y in indexes:
            comparing_one_block(x,y)         


if __name__=='__main__':                   
    sud = read_file("../Data/SudokuSolver_Medium1.csv")
    replace_nones(sud)
    # intial printing
    printing_my_sudoku()
    loops =0      
    while True:
        temp_sud = copy.deepcopy(sud)
        comparing_horizontal_rows()
        comparing_vertical_columns()
        comparing_blocks()
        if temp_sud == sud:
            break 
        loops +=1
        continue
    print(loops)

      
    #printing after first execution 
    printing_my_sudoku()
