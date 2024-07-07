

import csv

# Get input file 
election_csv = "PyPoll/Resources/election_data.csv"

#Initialising total count
total_count = 0 


candidatevotes = {}

# open  election_data file
with open(election_csv, newline='') as csvfile:

    # specify delimiter for csv files
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first
    csv_header = next(csvreader)


    # Read each row of data after the header
    for row in csvreader:
        total_count += 1
        if row[2] not in candidatevotes:
            candidatevotes[row[2]] = 1
        else:
            candidatevotes[row[2]] += 1   
        
        


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_count))
print("-------------------------")

for candidate, votes in candidatevotes.items():
    print(candidate + ": " + "{:.3%}".format(votes/total_count) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(candidatevotes, key=candidatevotes.get)

print(f"Winner: {winner}")

# write to output file

f = open("PyPoll/Analysis/election_results.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Votes: " + str(total_count))
f.write('\n')
f.write("-------------------------")
f.write('\n')

for candidate, votes in candidatevotes.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/total_count) + "   (" +  str(votes) + ")")
    f.write('\n')
  
f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')
