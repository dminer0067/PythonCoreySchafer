import csv

html_output = ""
names = []

with open("Patron.csv","r") as readfile:
    csv_data = csv.reader(readfile)
    
    next(csv_data) #to remove header
    next(csv_data) #To remove first line of Bad data from csv file.
    
    #print(csv_data)
    for line in csv_data:
        if line[0] == "No Reward":
            break
        names.append(f"{line[0]} {line[1]}")


html_output += f"<p> Currently there are {len(names)} Public contributors. Thanks to All...!! </p>"         
html_output += "\n<ul>"

for name in names:
    html_output += f"\n \t <li>{name}</li>"
    
html_output += "\n</ul>"
    
print(html_output)
# with open("Paton.html","w") as htmlwriter:
#     htmlwriter.write(html_output)
    

# for name in names:
#     print(name)
    
    