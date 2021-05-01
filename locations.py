import csv

reader = csv.reader(open(r"db-locations.csv"), delimiter=',')
filtered = filter(lambda p: 'Andre Iguodala' == p[3], reader)

for row in filtered:
	print(row)