name = "rUdYY bHAI"
print(name[::-2])
print(len(name))
# print(len("RUDDY BHAI"))
print(name.lower())
print(name.title())
print(name.count("U"))
name1="86779"
print(name1.isdigit())
x=4
y=55
print("sex is guud at ",x+y)

regular_string = "C:\new_folder\file.txt"  # here due to \n in adress of string it takes as a new line command 
print("Regular String:", regular_string)   # so to avoide this we uses raw string method..

raw_string = r"C:\new_folder\file.txt"     # it is used when you hav t write the complete path of an directory.
print("Raw String:", raw_string)

b=name.split()
print(b)