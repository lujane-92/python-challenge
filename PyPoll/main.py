import os
import csv

poll_csv = os.path.join("/Users/lujan/Downloads/Instructions/PyPoll/Resources/election_data.csv")

with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    votes = []
    unique = []
    khan = []
    correy = [] 
    li = []
    otooley =[]
    results =[]
    
    for row in csvreader:
        vote = row[2]
        votes.append(vote)

    for x in votes: 
        if x not in unique:
            unique.append(x)

    for x in votes: 
        if x == "Khan":
            khan.append(x)
    khan_p = float("{0:.2f}".format(len(khan)/len(votes)*100))
    results.append(khan_p)
    

    for x in votes: 
        if x == "Correy":
            correy.append(x)
    correy_p = float("{0:.2f}".format(len(correy)/len(votes)*100))
    results.append(correy_p)
    
    for x in votes: 
        if x == "Li":
            li.append(x)
    li_p = float("{0:.2f}".format(len(li)/len(votes)*100))
    results.append(li_p)

    for x in votes: 
        if x == "O'Tooley":
            otooley.append(x)
    otooley_p = float("{0:.2f}".format(len(otooley)/len(votes)*100))
    results.append(otooley_p)

    winner = 0
    for x in results:
        if x > winner:
            winner = x

print ("Election Results")
print ("----------------------------")
print (f"Total Votes: {len(votes)}")
print (f"Khan: {khan_p}00% ({len(khan)})")
print (f"Correy: {correy_p}00% ({len(correy)})")
print (f"Li: {li_p}00% ({len(li)})")
print (f"O'Tooley: {otooley_p}00% ({len(otooley)})")
print ("----------------------------")
print (f"Winner: {unique[results.index(winner)]}")
print ("----------------------------")

output_file = os.path.join("/Users/lujan/Desktop/Election_Results.txt")


with open(output_file,"w") as file:
    file.write ("Election Results")
    file.write("\n")
    file.write ("----------------------------")
    file.write("\n")
    file.write (f"Total Votes: {len(votes)}")
    file.write("\n")    
    file.write (f"Khan: {khan_p}00% ({len(khan)})")
    file.write("\n")
    file.write (f"Correy: {correy_p}00% ({len(correy)})")
    file.write("\n")   
    file.write (f"Li: {li_p}00% ({len(li)})")
    file.write("\n")    
    file.write (f"O'Tooley: {otooley_p}00% ({len(otooley)})")
    file.write("\n")    
    file.write ("----------------------------")
    file.write("\n")    
    file.write (f"Winner: {unique[results.index(winner)]}")
    file.write("\n")    
    file.write ("----------------------------")
    