import csv
with open ('election_data.csv') as csvfile: 
    
#Set variable for csv and delimiter
    csvreader=csv.reader(csvfile, delimiter=',') 
    
    #Read the header row first
    header=next(csvreader) 

    #Generate lists for 
    voterids=[] #Generate list for the "Voter ID" 
    counties=[] #Generate list for "County" 
    candidates=[] #Generate list for the "Candidate"
    candidatenames=[] #Generate list for actual candidate names
    totaleachcan=[] #Generate list for total votes for each candidate
    resultprintcan=[] #Generate list for result printout of each candidate
    totaleachcanperc=[] #Generate list for % of votes for each candidate

    #Set starting positions
    loop1=0
    loop2=0
    loop3=0
    loop4=0
    line_count=0
    winnervotes=0
    loservotes=0
   
    
    #Read in row data after the header and write data into assigned column numbers 
    for row in csvreader:
        voterid=row[0] 
        voterids.append(voterid) #Add next line to list voterids
        county=row[1] 
        counties.append(county) #Add next line to list counties
        candidate=row[2]      
        candidates.append(candidate) #Add next line to list candidates
    
    #Count the total number of voter IDs to determine total vote count 
    line_count= len(voterids) 
    
    #print(line_count)

candidatenames.append(candidates[0]) #Pre-loadfirst candidate name for comparison

#First loop is through the list of candidates to determine candidates voted for (variable loop1 as loop index counter)
for loop1 in range (line_count-1):
    if candidates[loop1+1] != candidates[loop1] and candidates[loop1+1] not in candidatenames:
        candidatenames.append(candidates[loop1+1])

n=len(candidatenames)

#Range of loop depending on how many candidates were found, count total votes of candidates
for loop2 in range (n): 
    totaleachcan.append(candidates.count(candidatenames[loop2])) 

#Set loservoters =maximum votes to compare 
loservotes=line_count 

#Calculate % per candidate found
for loop3 in range(n):
    totaleachcanperc.append(f'{round((totaleachcan[loop3]/line_count*100), 4)}%') 
    #Find candidate with highest vote count
    if totaleachcan[loop3]>winnervotes:
        winner=candidatenames[loop3]
        winnervotes=totaleachcan[loop3]
    #Find candidate with lowest vote count
    if totaleachcan[loop3]<loservotes:
        loser=candidatenames[loop3]
        loservotes=totaleachcan[loop3]

#Format output of list "resultprintcan"
for loop4 in range(n):
    resultprintcan.append(f'{candidatenames[loop4]}: {totaleachcanperc[loop4]} ({totaleachcan[loop4]})')

#Each candidate's results printed on new line on output 
resultlines='\n'.join(resultprintcan)

#Generate & print analysis results 
analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {line_count}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner} :)\n\
Last: {loser} :(\n\
----------------------------\n'
print(analysis)

#Open file and if none exists, write into a new text file named "pypoll.txt"
file1=open("pypoll.txt","w") 
#Write analysis results into text file 
file1.writelines(analysis) 
#Close write command 
file1.close() 