odd_number_list=[]
even_number_list=[]

for number in range(1000,2000):
    if number % 2 == 0:
      
        odd_number_list.append(number)
        continue
    if number %2 != 0:
       
        even_number_list.append(number)
        continue
    
print("odd number is:\n",odd_number_list)
print("even number is:\n",even_number_list)
