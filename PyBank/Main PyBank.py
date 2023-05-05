#CSV module import 
import csv

#specify source CSV file path
with open ('budget_data.csv') as csvfile: 

    #Set variable and delimiter
    csvreader=csv.reader(csvfile, delimiter=',')
    
    #Read the header row first
    header=next(csvreader)

    #Create list named "months" for the "Date" column
    months=[] 
    #Create list named "prolosses" for the "Profit/Losses" column
    prolosses=[] 

    #Set starting points for variables
    total=0
    a_change=0
    m_change=0
    m_count=0
    delta1=0
    delta2=0
    delta_line1=0
    delta_line2=0
    loop1=0
    loop2=0

    #Write row data into lists
    for row in csvreader:
        month=row[0] 
        proloss=row[1] 
        months.append(month) 
        prolosses.append(proloss) 
    
    #Count the total of months
    m_count = len(months) 

#Calculate total for ProLosses List 
for loop1 in range (m_count):
    total=total+int(prolosses[loop1]) 

#Calculate sum of changes through list prolosses (variable loop2 as loop index counter)
for loop2 in range (m_count-1): #Restrict loop to avoid overflow (last line +1)
    a_change=a_change+(float(prolosses[loop2+1])-float(prolosses[loop2])) #
#print(a_change/(m_count-1))

 #Calculate monthly change
    m_change=(float(prolosses[loop2+1])-float(prolosses[loop2]))
    
     #Determine greatest increase
    if m_change>delta1:
        delta1=m_change
        delta_line1=loop2
    else:
        delta1=delta1

#Determine greatest decrease
    if m_change<delta2: 
        delta2=m_change
        delta_line2=loop2
    else:
        delta2=delta2


#Generate and print analysis output
analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {m_count}\n\
Total Amount: ${total}\n\
Average Change: ${round(a_change/(m_count-1),2)}\n\
Greatest Increase in Profits: {months[delta_line1+1]} (${int(delta1)})\n\
Greatest Decrease in Profits: {months[delta_line2+1]} (${int(delta2)})\n'

print(analysis) 

#Write into text file named pybank.txt
file1=open("pybank.txt","w") #Open or if file does not exist then create file named pybank.txt
file1.writelines(analysis) #Write analysis into pybank.txt
file1.close() #Close pybank.txt write mode