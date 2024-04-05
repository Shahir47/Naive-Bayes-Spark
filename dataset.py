import csv
import re

csvfile = open('cyberbullying_tweets.csv', newline='', encoding='utf-8')
reader = csv.reader(csvfile)

csvfile2 = open('cyberbullying_tweets_output.csv', 'w', newline ='')
writer = csv.writer(csvfile2)

# writer.writerow(['review', 'rating'])

for row in reader:
    row[0] = "".join([i if ord(i)<128 else '' for i in row[0]])
    row[0] = re.sub('\n', ' ', row[0])
    # if(row[1]!='rating'):
    #     row[1] = str(row[1][0])
    # if(len(row[0]) > 0 and len(row[1])==1):
    #     writer.writerow(row)
    if(len(row[0]) > 0):
        writer.writerow(row)


dt = {
    'not_cyberbullying' : '1',
    'gender' : '2',
    'religion' : '3',
    'other_cyberbullying' : '4',
    'age' : '5',
    'ethnicity' : '6'
}

import csv

csvfile = open('cyberbullying_tweets_output.csv', newline='')
reader = csv.reader(csvfile)

fhand = open('CyberBullying.txt', 'w')

i = 0

for row in reader:
    if(row[0]!='tweet_text' and len(row[0])>0):
        fhand.write(f"{row[0]}\t{row[1]}\t{dt[row[1]]}")
        fhand.write("\n")