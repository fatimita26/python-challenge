import csv

# Set path for file
csvpath = "PyPoll/Resources/election_data.csv"

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
#requirements:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
    csv_row1 = next(csvreader)
    total_votes = 1
    
    candidate_votes = 1
    votes_dict = {csv_row1[2] : int(candidate_votes)}
    #iterate trough the data
    for row in csvreader:
        #cumilative votes
        total_votes += 1
        candidate_name = row[2]
        #check if a new candiate. add candidate to the dictionary,initial votes at 1
        if candidate_name not in votes_dict:
            votes_dict[candidate_name] = 1
        #if Candidate already in the dictionary, update votes count
        else:
            candidate_votes = votes_dict[candidate_name]
            votes_dict.update({candidate_name:candidate_votes +1})
#print statements    
            
print("Election Results")
print("--------------------------------------")
print(f'Total Votes:  {total_votes}')
print("--------------------------------------")
#print results for each candidate
for candidate,votes in votes_dict.items():
    percentage = votes/total_votes * 100   
    print(f'{candidate} : {round(percentage,3)}% ({votes})')
print("--------------------------------------")
#sort in 
a = dict(sorted(votes_dict.items(), key=lambda x: x[1],reverse=True))

print(f"Winner: {list(a.keys())[0]}")

