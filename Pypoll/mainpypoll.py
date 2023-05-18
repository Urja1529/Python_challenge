import os
import csv
candidate=set()
candidate_name=[]
#Path to file
path=os.path.join('..','Resources','election_data.csv')
#opening file
with open (path,'r') as data_file:
    #Reding File and skipping Header
    reader=csv.reader(data_file,)
    header=next(reader)
    #Counting Total Number of Votes
    rows=list(reader)
    num_votes=len(rows)
    #creating set to store unique name of candidates and counting their votes
    for row in rows:
       candidate.add(row[2])
    Vote_count = dict.fromkeys(candidate, 0) 
    for row in rows:
        b= Vote_count[row[2]]=Vote_count[row[2]]+1
            
    winner=max(zip(Vote_count.values(),Vote_count.keys()))[1]  
    
    print("Election Results ")     
    
    print("--------------------------------------------")
   
    print(f"Total Number of votes :{num_votes}")

    print("---------------------------------------------")
    
    for candidate_names in candidate:
        #calculating percentage votes and printing them
        Percentage=(Vote_count[candidate_names]/num_votes)*100
        print(f"{candidate_names} : {Percentage}: ({Vote_count[candidate_names]})")
    
    print("---------------------------------------------")
    print(f"Winner: {winner}")
    #printing name to text file
    with open("output.txt",'w') as text_file:
        text_file.write(f"Election Results ")
        text_file.write("--------------------------------------------")
        text_file.write(f"Total Number of votes :{num_votes}")
        text_file.write("---------------------------------------------")
        text_file.write(f"{candidate_names} : {Percentage}: ({Vote_count[candidate_names]})")
        text_file.write("---------------------------------------------")
        text_file.write(f"Winner: {winner}")      
    