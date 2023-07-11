#function name ds with parameters roll_no and name.

rollno=int(input("Enter your roll number:"))
name=input("Enter your name:")
ds={
   "rollno": rollno,
   "name":name,
}  
print(ds)
# Add parameters to a list
#using append

my_list=[]
my_list.append(rollno)
my_list.append(name)

# Add parameters to a list
#using extend

my_list=[]
my_list.extend([rollno,name])

# Add parameters to a tuple
my_tuple = (ds)
print("Tuple:", my_tuple)

# Add parameters to a set

my_set = set()
#my_set.add(ds)
print("Set:",my_set)


# Add parameters to a dictionary

my_dict = {}
my_dict['Roll No'] = ds
my_dict['Name'] = ds
print("Dictionary:", my_dict)

# Change values during runtime

roll_no_new = input("Enter new Roll No: ")
name_new = input("Enter new Name: ")
ds[0] = roll_no_new
ds[1] = name_new
my_tuple = (roll_no_new, name_new)

my_list = []

roll_no_new = input("Enter new Roll No: ")
name_new = input("Enter new Name: ")
new_data = {'Roll No': roll_no_new, 'Name': name_new}

for item in my_list:
    if item['Roll No'] == roll_no_new or item['Name'] == name_new:
       
        break
else:
    my_list.append(new_data)

# Delete data structures

del ds
del my_list
del my_tuple
del my_set
del my_dict