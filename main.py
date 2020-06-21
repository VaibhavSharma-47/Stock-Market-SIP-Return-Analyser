import csv
filename ="CSVForMonth.csv"

fields = [] 
rows = [] 
def rate_find_sip(sip_amount,Port,month_diff):
    l = 0
    h = 1
    rate = (l + h)/2
    
   
    for i in range(20):
        
        monthly_interest = rate/12
        #print(rate , monthly_interest)
        
        M =sip_amount*((pow(1 + monthly_interest,month_diff) -1)/monthly_interest) * (monthly_interest+1)        
        if(M>Port):
            h= rate
            rate = (l+h)/2.0
        elif (M<Port):
            l=rate
            rate = (l+h)/2.0
        else:
            return rate
        
    return rate
def rate_find_lump(lump,Port,month_diff):
    l = 0
    h = 1
    n = 1
    rate = 1*(pow(Port/lump,1/n)-1)
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
#Un Comment these lines to calculate custom
# year  = int(input("\nEnter Year to start from\n")) 
# month = int(input("\nMonth \n"))

# year_e  = int(input("\nEnter Year to end from\n")) 
# month_e = int(input("\nMonth \n"))
year, month,year_e,month_e =2015,0,2019,0
month_diff = (year_e-year)*12 + (month_e - month)
print(rows[(year-2000)*12+month])
print(rows[(year_e-2000)*12+month_e])
fd_rate = 0.07
i = fd_rate/12
for row in range((year-2000)*12+month,(year_e-2000)*12+month_e+1): 
    # parsing each column of a row 
    #print(rows[row][1])
    temp = 1000/float(rows[row][1])

    units += temp
    print(temp)
    #print(row[1])
print("Months ",month_diff)
row_number_end = (year_e-2000)*12+month_e
print("row end",rows[row_number_end])
protfolio = units*float(rows[row_number_end][1])
principal = sip_amount*(month_diff)
rate = 12*( pow(protfolio/(principal),1.0/(month_diff)*12)-1)
print("Invested money",principal)
print("FOR SIP")
print("Portflio value",protfolio)


fd_amount =sip_amount*((pow(1 + i,month_diff) -1)/i) * (i+1)
print("At fd at 7% u get ",fd_amount)
print("Profit of over fd",protfolio-fd_amount)
print("Rate for Sip ",rate_find_sip(sip_amount,protfolio,month_diff))
print("For LumpSum at the start day" )
units=principal/float(rows[(year-2000)*12+month][1])
print("Units owned",units)
print("Curr value ", units*float(rows[(year_e-2000)*12+month_e][1]))
print("Rate for lumpsum",rate_find_lump(principal,protfolio,month_diff))
#print("Rate is",rate)