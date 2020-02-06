import csv

file_csv = open("cstmc-CSV-en.csv", 'r')
data_dict = []

reader = csv.DictReader(file_csv, delimiter='|')
for row in reader:
    if len(row.keys()) != 36:
        del row[None]
    data_dict.append(row)
column_names = list(data_dict[0].keys())

# count in every categories
categories_1 = [one_dict['category1'] for one_dict in data_dict]
categories_2 = [one_dict['category2'] for one_dict in data_dict]
categories_3 = [one_dict['category3'] for one_dict in data_dict]
categories = categories_1 + categories_2 + categories_3
set_of_categories = set(categories)
dict_categories = {}

for category in set_of_categories:
    dict_categories[category] = categories.count(category)
categories, count_of_categories = list(dict_categories.keys()), list(dict_categories.values())
file_csv.close()

file_output = open('object-stats.csv', 'w', newline='')
writer = csv.DictWriter(file_output, fieldnames=['Category', 'Count'])
writer.writeheader()

for (category, count_of_category) in zip(categories, count_of_categories):
    writer.writerow({'Category': category, 'Count': count_of_category})
file_output.close()
