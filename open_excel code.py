from csv import reader

opened_file = open(r"C:\Users\lenovo\Documents\wait.csv")
read_file = reader(opened_file)
apps_data = list(read_file)



for i in apps_data[1:]:

    print(i)