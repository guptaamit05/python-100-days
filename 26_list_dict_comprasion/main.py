

number = [1,2,3]


double_number = [x*2 for x in number]
# print(double_number)


stringg  ="Angela"
each_char = [char for char in stringg]
# print(each_char)


db_num = [x*2 for x in range(1,5)]
# print(db_num)



# find common number in both file file1.txt and file2.txt
first = open('./file1.txt')
second = open('./file2.txt')

first_list = [int(x.strip()) for x in first.readlines()]
second_list = [int(x.strip()) for x in second.readlines()]

result = [item for item in first_list if item in second_list]
# print(result)
    # file1 = f.readlines()
# with open('./file2.txt') as f:
#     file2 = f.readlines()


# print(file1, file2)
# result = 

# print(result)



sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split(" ")}

# print(result)



weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {key:(( val * 9/5)+32) for key,val in weather_c.items()}
print(weather_f)