#!/usr/bin/env python
# coding: utf-8

# In[46]:


import os
import csv

# input file
election_data_csv = os.path.join('.', 'Resources', 'election_data.csv')
# output file
election_data_txt = os.path.join('.', 'analysis', 'election_analysis.txt')

total_votes = 0
candidates_name_list = [""]
candidates_votecount_list = [0]
winner = ''
winner_count = 0
lines = []

# open and read the csv file
with open (election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # read header row and skip
    csv_header = next(csvfile)
       
    # loop through the rest of the file one row at a time
    for row in csvreader:
        
        # increment the total votes counter
        total_votes += 1
        
        # Determine how many candidates are stored in the candidates list already
        candidates_list_length = len(candidates_name_list)
        
        candidate_found = False
        
        # If the very first candidate in the file, write out their name and vote count in the candidate lists
        if candidates_votecount_list[0] == 0:
            candidate_found = True
            candidates_name_list[0] = row[2]
            candidates_votecount_list[0] = 1
        else:
            # Else check current row from file and loop through each element in the candidates list to see if the name already exists
            for x in range(candidates_list_length):
                # If the name is already in the candidates list, just add 1 to their vote count
                if candidates_name_list[x] == row[2]:
                    candidate_found = True
                    candidates_votecount_list[x] += 1
            # If the candidate is not already in the list, append the new name and first vote to the list
            if candidate_found == False:
                candidates_name_list.append(row[2])
                candidates_votecount_list.append(1)
            
# set up all of formatted output variables
blank = ''
line1 = ('Election Results')
line2 = '--------------------------'
line3 = f'Total Votes: {total_votes}'
line4 = '--------------------------'

# start creating lines list for output
lines = [line1, blank, line2, blank, line3, blank, line4, blank]

# loop through each candidate
for candidates_index in range(candidates_list_length):
    
    # calculate candidates winning percentage
    candidates_percentage = round((candidates_votecount_list[candidates_index] / total_votes * 100), 3)
    candidates_percentage_display = str(candidates_percentage) + '%'
    
    # determine winner - if more votes than the previously saved vote count, update the winner 
    if candidates_votecount_list[candidates_index] > winner_count:
        winner_count = candidates_votecount_list[candidates_index]
        winner = candidates_name_list[candidates_index]

    # continue to append the string with candidate name, percentage, and vote count
    lines.append(
                 str(candidates_name_list[candidates_index]) + ': ' +
                 str(candidates_percentage_display) + ' (' +
                 str(candidates_votecount_list[candidates_index]) + ')'
                )
    # blank line
    lines.append('')

# append the remaining output lines to the list
line6 = '--------------------------'
line7 = f'Winner: {winner}'
line8 = '--------------------------'
lines.append(line6)
lines.append(blank)
lines.append(line7)
lines.append(blank)
lines.append(line8)

# open and write output txt file
with open(election_data_txt, 'w') as txtfile:

    for line in lines:
        
        # write each line to the terminal
        print(line)
        
        # write each same line to the output txt file
        txtfile.write(line)
        # line break for txt file
        txtfile.write('\n')
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




