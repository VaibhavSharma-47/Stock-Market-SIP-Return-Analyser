import csv
filename ="CSVForMonth.csv"

fields = [] 
rows = [] 
def rate_find(sip_amount,Port):
    l = 0
    h = 1
    rate = (l + h)/2.0
    for i in range(20):
        M =sip_amount*((1 + rate)*(month_diff) - 1) * (rate+1)
        if(M>Port):
            h= rate
            rate = (l+h)/2.0
        elif (M<Port):
            l=rate
            rate = (l+h)/2.0
        else:
            return rate
        
    return rate
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
    # get total number of rows 
    print("Total no. of rows: %d"%(csvreader.line_num)) 
  
# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 
  
#  printing first 5 rows 
sip_amount = 1000.0
units = 0.0
# year  = int(input("\nEnter Year to start from\n")) 
# month = int(input("\nMonth \n"))

# year_e  = int(input("\nEnter Year to end from\n")) 
# month_e = int(input("\nMonth \n"))
year, month,year_e,month_e =2015,0,2019,0
month_diff = (year_e-year)*12 + (month_e - month)
print(rows[(year-2000)*12+month])
fd_rate = 0.07
for row in range((year-2000)*12+month,(year_e-2000)*12+month_e+1): 
    # parsing each column of a row 
    #print(rows[row][1])
    units += 1000/float(rows[row][1])
    #print(row[1])
protfolio = units*float(rows[(year_e-2000)*12+month_e][1])
principal = sip_amount*(month_diff*12)
rate = 12*( pow(protfolio/(principal),1.0/(month_diff)*12)-1)
print("Invested money",principal)
print("FOR SIP")
print("Portflio value",protfolio)


M =sip_amount*((1 + fd_rate)*(month_diff) - 1) * (fd_rate+1)
print("At fd  u get ",M)
print("Profit of ",protfolio-M)
print("Rate ",rate_find(sip_amount,protfolio))
print("FOR LumpSum" )
units=principal/float(rows[(year-2000)*12+month][1])
print("Curr value ", units*float(rows[(year_e-2000)*12+month_e][1]))
print("Rate ",rate)