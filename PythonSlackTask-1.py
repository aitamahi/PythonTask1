### 1. Python program to find largest number in list
list1=[3232,444,523,122,23432,3232,45322,32,5355]
max1=list1[0]
for i in list1:
    if i > max1:
        i,max1=max1,i
print("Largest Number in the List is",max1)

####### or #########
list1=[3232,444,523,122,23432,3232,45322,32,5355]
print("Largest Number in the List is",max(list1))

#-----------------------------------------------------------------

## 2.Python Program to print second largest number in the list

list2=[34322,444,523,122,23432,3232,45322,32,5355]
res_list=[]
res_list=sorted(list2)
print("Second Largest number in list is",res_list[-2])

#------------------------------------------------------------------        
## 3. Python program to merge two lists and sort it

list3=[35345345,43453463,544,99032,23,4353,5792,9808]
list4=[8794,5556,34,89,7,56,3223,56,666,93,35,55]

merge_list= list3+list4
print("Merged order of list is",merge_list)

sort_list= sorted(merge_list)
print("Sorted order of list is",sort_list)

#-------------------------------------------------------------------

## 4. Python program to swap first and last values of list

list5=['Maheswari',43534,4534,'My','Name','is','Aita',9876543210]
first_ele=list5[0]
last_ele=list5[-1]
res_string=list5[1:-1]
res_string.insert(0,last_ele)
res_string.append(first_ele)
print(res_string)


