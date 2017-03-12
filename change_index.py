import os

index = ["22","24","23","25","3","4","8","19","20","21","9","10","11","12","13","14","15","16","17","18","6","1","2","7","5"]

counter = 0
files = os.listdir('.')

for file_name in files:
    if file_name.startswith("_vhi"):
        counter+= 1
        os.rename(file_name,"vhi_id_"+index[counter]+"_2017-02-26.csv")


