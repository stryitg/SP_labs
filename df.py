import pandas 

def cr8_df(path):
    df = pandas.read_csv(path,index_col=False,header=0)
    return df
    
def min_max_year(path,year):
    df = cr8_df(path)
    curr_min = 100
    curr_max = 0
    for index, row in df.iterrows():
        if row["year"] == year:
            if curr_max < row["VHI"]:
                curr_max = row["VHI"]
            if curr_min > row["VHI"]:
                curr_min = row["VHI"]
    print("min: " + str(curr_min) + " max: "+ str(curr_max) )


def drought(path):
    df = cr8_df(path)
    for index,row in df.iterrows():
        if row["VHI"] < 15:
            print(row)


min_max_year("vhi_id_1_2017-02-26.csv",1988)

drought("vhi_id_1_2017-02-26.csv")
