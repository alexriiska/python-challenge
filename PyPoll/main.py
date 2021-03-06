# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote

#import modules
import os
import csv

#import the csv path
csvpath = "/Resources/election_data.csv"

# Open the CSV
with open(csvpath, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skip the header row
    csv_header = next(csvreader)
    
    #store the data of the csv as a list
    values = [each [2] for each in csvreader]
    rowcount = len(values)
        
    #create a list to store the names of the candidates
    candidates = {}
    #count = list()
    
    for i in range(0,rowcount):
        candidate = values[i]
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1
    
    winner = max(candidates, key = candidates.get)
    
        
#print statements

print('Election Results')
print('----------------------------')

#print the number of total votes
print(f'Total number of votes cast: {rowcount}')
print('----------------------------')

#print the name of each candidate, followed by the percent of the total votes they received, and the number of votes they received
#use a for loop to iterate through the created lists
for candidate, votes in candidates.items():
        print(f'{candidate}:({(votes/rowcount*100):.3f}%) ({votes})')

print('----------------------------')

#The winner of the election based on popular vote.
print(f'Winner: {winner}')

print('----------------------------')


# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

with open("Election Results.txt", mode = "w") as file:
    file.write('Election Results')
    file.write("\n")
    file.write('----------------------------')
    file.write("\n")
    file.write(f'Total number of votes cast: {rowcount}')
    file.write("\n")
    file.write('----------------------------')
    file.write("\n")
    for candidate, votes in candidates.items():
            file.write(f'{candidate}:({(votes/rowcount*100):.3f}%) ({votes})')
            file.write("\n")
    file.write('----------------------------')
    file.write("\n")
    file.write(f'Winner: {winner}')
    file.write("\n")
    file.write('----------------------------')
        
