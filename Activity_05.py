input_line=input("enter the numbers to be added with a space separating each : ")
number_string_list=input_line.split()
sum=0
for i in number_string_list:
    sum=sum+int(i)
print("the sum of the numbers = %d"%sum)

