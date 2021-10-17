import pandas as pd

#read data from csv file and choosing important for us columns
data_t = pd.read_csv('C:/ABD-a/ABD/lab2/Original data/earthquake_data.csv', sep=',', usecols= ['Do you think the "Big One" will occur in your lifetime?', 'Age', 'What is your gender?'])
#changing columns names
data_tidy = data_t.rename(columns = {'Do you think the "Big One" will occur in your lifetime?': 'Answer to question', 'What is your gender?': 'Gender'}, inplace = False)
#changing the order of columns
data_tidy = data_tidy.reindex(columns=['Age', 'Gender', 'Answer to question'])
print('result after renaming columns, head:')
print(data_tidy.head(3))
#all empty answers filled with NaN
nan_value = float("NaN")
data_tidy.replace("", nan_value, inplace=True)
#delete empty or partially empty records for better visuality of data (erasing invalid answers, with NaN)
data_tidy.dropna(inplace=True)
#save data frame to csv file
data_tidy.to_csv('C:/ABD-a/ABD/lab2/Analysis Data/earthquake_data_results.csv', index=False)
