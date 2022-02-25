import csv

from numpy import delete

with open("names.csv","r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    with open("newnames_dict.csv","w") as dictwriter:
        fname = ['first_name','last_name']
        
        dictcsvwriter = csv.DictWriter(dictwriter,fieldnames=fname,delimiter='\t')
        
        dictcsvwriter.writeheader()
        
        for line in csvreader:
            del line ['email']
            dictcsvwriter.writerow(line)
    
   
       