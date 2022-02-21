import pandas as pd

df = pd.read_csv('final_entity.csv')

def isNaN(num):
    return num != num

print(df.index)
# print(list(df.columns))
# print('PERSON' in list(df.columns))

for index, row in df.iterrows():
    # print(row['LABEL'])
    # print(type(row))
    # print(row)
    if not isNaN(row['LABEL']):
        label_list = row['LABEL'].split(',')
        for label in label_list:
            if label in list(df.columns):
                # print('true ', label)
                # row[label] = 'True'
                # print(row[label])
                df.loc[index, label] = True

print(df)
df.to_csv('final_entity_result.csv', sep = ',')