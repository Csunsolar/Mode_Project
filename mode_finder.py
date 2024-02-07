numbers = [1,2,3,1,1]

unique_num = []
for number in numbers:
    if number not in unique_num:
        unique_num.append(number)

if len(unique_num) == len(numbers):
    print("There is no mode.")
    exit()
  
#The below works for majority between two integers
# balance = 0

# for num in numbers:
#     if balance == 0:
#         mode = num
#     if num == mode:
#         balance += 1
#     else:
#         balance -= 1
    
#creates dict with keys being the unique numbers from the numbers list
counter_dict = dict.fromkeys(unique_num, 0)

for num in numbers:
    x = counter_dict.get(num)
    x += 1
    counter_dict.update({num:x}) 

test = max(counter_dict.values())
for k in counter_dict:
    if counter_dict[k] == test:
        print(k)
