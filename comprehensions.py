# How many votes did you get?
# Total votes in the election
# Calculate the percentage of votes you received

my_votes = float(input('How many votes did you get in the election?'))
total_votes = float(input('What is the total votes in the election?'))
percentage_votes = round(((my_votes / total_votes) * 100),2)
print('I got ' +str(percentage_votes)+'% of the votes')

