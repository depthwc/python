import csv

# reader

# with open('data.csv', newline='') as file:
#     reader = csv.reader(file, delimiter= ' ', quotechar = ',')
#     for i in reader:
#         print(' , '.join(i))


# writer

# with open('data2.csv', 'w' ,newline='') as file:
#     w = csv.DictWriter(file, fieldnames = ['Name','Type'])

#     w.writeheader()
#     w.writerow({'Name': 'Jhon' , 'Type': 'killer'})


with open('data.csv', newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    # ... process CSV file contents here ...