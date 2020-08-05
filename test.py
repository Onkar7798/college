import csv
csv_file2 = open('colleges.csv', 'a')
csv_writer = csv.writer(csv_file2)
li = ['1','3424','fag','sgs','dgsfgs','sdsdf']
csv_writer.writerow(li)

csv_file2.close()