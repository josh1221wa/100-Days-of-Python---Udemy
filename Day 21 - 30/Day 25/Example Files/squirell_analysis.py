import pandas

data = pandas.read_csv("D:\\Desktop\\Computer\\Python\\100 Days of Python - Udemy\\Day 25\\Example Files\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_dict = {
    "Fur Color" : [],
    "Count" : []
}

fur_list = data["Primary Fur Color"].tolist()
for i in fur_list:
    if i not in data_dict["Fur Color"]:
        data_dict["Fur Color"].append(i)
        data_dict["Count"].append(0)
    else:
        data_dict["Count"][data_dict["Fur Color"].index(i)] += 1


df = pandas.DataFrame(data_dict)
df.to_csv(r"D:\Desktop\Computer\Python\100 Days of Python - Udemy\Day 25\Example Files\new_data.csv")