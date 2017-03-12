import csv

def format(i):
    with open("vhi_id_"+str(i)+"_2017-02-26_.csv",'r') as csv_in:
        with open("_vhi_id_"+str(i)+"_2017-02-26_.csv",'w') as csv_out:
            reader = csv.reader(csv_in)
            writer = csv.writer(csv_out)
            for row in reader:
                if row[0][0] != "M":
                    if row[0][0] != "<":
                        data_year = row[0][0]+row[0][1]+row[0][2]+row[0][3]
                        data_weak = row[0][5]+row[0][6]
                        data_provinceID = row[0][9] + row[0][10] + row[0][11] + row [0][12] + row[0][13]+ '.' + row[1]
                        data_SMN = row[2]
                        data_SNT = row[3]
                        data_VHI = row[4]
                else:
                    data_year = "year"
                    data_weak = "weak"
                    data_provinceID = "provinceID"
                    data_SMN = "SMN"
                    data_SNT = "SNT"
                    data_VHI = "VHI"
                writer.writerow([data_year,data_weak,data_provinceID,data_SMN,data_SNT,data_VHI])

    print('success' + str(i))
        
for i in range(1,25):
    format(i)




