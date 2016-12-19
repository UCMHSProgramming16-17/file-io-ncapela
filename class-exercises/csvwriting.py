#Import csv library
import csv

#Opem the CSV file
csvfile = open("csvfile.csv", "w")

#Create the Csv writer
csvwriter = csv.writer(csvfile, delimiter = ",")

# Write rows to the file
csvwriter.writerow([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
csvwriter.writerow(["Real", "Madrid", "Is", "Going", "To", "Win", "The", "UCL", "In", "2017"])
csvwriter.writerow(['original', 'x2', 'x3', 'x4', 'x5'])
for x in range(500):
  csvwriter.writerow([x, x*2, x*3, x*4, x*5])
  
# Close the file
  csvfile.close()