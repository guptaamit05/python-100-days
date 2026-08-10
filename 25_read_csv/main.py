# import csv

# with open("./weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temprature = []
#     for row in data:
#         if row[1] != 'temp':
#             temprature.append(int(row[1]))
#     print(temprature)

#  read CSV using pandas library...
import pandas

# data = pandas.read_csv("./weather_data.csv")
# print(data['temp'])



# dict_data = data.to_dict()
# print(dict_data)

# temp_list =  data['temp'].to_list()
# print(temp_list)

# print(f"Avg Temprature: {sum(temp_list)/len(temp_list)}")
# print(f"Avg using pandas library: {data['temp'].mean()}")

# print(f"Max Temp using pandas fun: {data['temp'].max()}")
# print(f"Minimum Temp using pandas fun: {data['temp'].min()}")


# print(data[data['day'] == 'Monday'] )

# print(f"Max temprature row: {data[data['temp'] == data['temp'].max()]}")




central_data = pandas.read_csv("./2018_Central_Park_Data.csv")
primary_fur_color_col = central_data['Primary Fur Color']


gray_color = len(central_data[primary_fur_color_col =='Gray'])
red_color = len(central_data[primary_fur_color_col =='Cinnamon'])
black_color = len(central_data[primary_fur_color_col =='Black'])

data_dict = {
    "Fur Color":['red', 'cinnamon', 'black'],
    "Count":[gray_color, red_color, black_color]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
