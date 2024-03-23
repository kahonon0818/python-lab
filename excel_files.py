# file modes: "w", "r", "a", "x" ...

#example1
import csv
with open("week23.csv", "w") as f:
    pen = csv.writer(f)
    header =["Name", "Cel phone", "city"]
    pen.writerow(header)
    pen.writerow(["Serge", "317 444 9168" , "Danville"])
    
f.close

#example2
import csv
with open("week23.csv", "w") as f:
    pen = csv.writer(f)
    header =["Name", "Cel phone", "city"]
    pen.writerow(header)
    entry1=["Serge", "317 444 9168" , "Danville"]
    pen.writerow(entry1)

f.close