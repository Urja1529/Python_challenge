import os
import csv
candidate=set()
candidate_name=[]
#vote_count=[]
#total_count=0
path=os.path.join('..','Resources','election_data.csv')
with open (path,'r') as data_file:
    reader=csv.reader(data_file,)
    header=next(reader)
    rows=list(reader)
    num_votes=len(rows)
    for row in rows:
       candidate.add(row[2])
    Vote_count = dict.fromkeys(candidate, 0) 
    for row in rows:
        b= Vote_count[row[2]]=Vote_count[row[2]]+1
       
    #print(Vote_count["Diana DeGette"])
    #print(Vote_count)
    
        
    winner=max(zip(Vote_count.values(),Vote_count.keys()))[1]  
    #print(winner)
    # for candidate_name,count in vote_count.items():
    #    print(f"{candidate_name} :{count} votes")
    print("Election Results ")     
    
    print("--------------------------------------------")
   #print(Total_vote)
    print(f"Total Number of votes :{num_votes}")

    print("---------------------------------------------")
    # for key,value in Vote_count.items():
    #     print(f"{ key } : {value}  ")
    for candidate_names in candidate:
        
        Percentage=(Vote_count[candidate_names]/num_votes)*100
        print(f"{candidate_names} : {Percentage}: ({Vote_count[candidate_names]})")
    # zip_object=(zip(candidate_names,Vote_count.items()))[1]
    # for candidate_names in zip_object:
    #     print(f" {candidate}")
    
    print("---------------------------------------------")
    print(f"Winner: {winner}")
    #Print(f"")-

    #print(f"Candidate name: {candidate}")  