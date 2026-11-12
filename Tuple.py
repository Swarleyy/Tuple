# In[5]:
numbers=(10,20,30,40,50,60,70,80,90)
print("Tuple:",numbers)
print("4th element form first:",numbers[3])
print("4th element form last:",numbers[-4])

# In[4]:
numbers=(10,20,30,40,50,60,70,80,90)
element=int(input("Enter element to search:"))
if element in numbers:
    print("Element exists in tuple")
else:
    print("Element does not exists in tuple")

# In[6]:
#convert list into tuple
number_list=[10,20,30,40,50]
number_tuple=tuple(number_list)
print("List:",number_list)
print("Tuple:",number_tuple)

# In[7]:
#find index of an item in a tuple
number=[10,20,30,40,50]
element=int(input("Enter element:"))
if element in number:
    print("Element exists at index:", number.index(element))
else:
    print("Element does not exist")

# In[15]:
#replace last value of tuple in a list to 100
number=[(10,20,30),(40,50,60),(70,80,90)]
new_list=[]
for tup in number:
    new_tup= tup[:-1] + (100,)
    new_list.append(new_tup)
print("Original List:",number)
print("Updated List:",new_list)

# In[17]:
#find max and min ekement in tuple
numbers=[20,17,30,37,7,200]
maximum=max(numbers)
minimum=min(numbers)
print("Maximum:",maximum)
print("Minimum:",minimum)

# In[21]:
#to swap the first and last element of tuple
numbers=(20,17,30,37,7,200)
new_tuple=(numbers[-1],) + numbers[1:-1] + (numbers[0],)
print("Original Tuple:",numbers)
print("Updated Tuple:",new_tuple)
