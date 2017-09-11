#Chris Osufsen
#Section 03
#5/1/2017

#Sentiment Analysis
#Data of movie ratings followed by the review given by the critic.
#Program takes into acount the rating and every individual word in the review.

import time
begin_time = time.time()
#set up empty dictionary to hold words
sentiment = {}

#open reviews
file_object = open('movie_reviews.txt', 'r')

#grab data from file
alldata = str.lower(file_object.read())
#close file
file_object.close()

#cut based on new line character to analyze each review
split_reviews = alldata.split('\n')

print('Initializing sentiment database')
#examine every review in database
for review in split_reviews:
    words = review.split(' ')

    for word in words:
        if word not in sentiment:
            sentiment[word] = [1, int(words[0])]
        else:
            sentiment[word][0] += 1
            sentiment[word][1] += int(words[0])
    #examine every word in this review
    #add to sentiment dictionary if neccessary, update if exists already

end_time = time.time()

#display stats
time = format(end_time - begin_time, '.2f')
print('Sentiment database initilization complete')
print('Total unique words analyzed:', len(sentiment))
print('Analysis took', time, 'seconds to complete')
print('')

#convert to lowercase
phrase = str.lower(input('Enter a phrase to test: '))
phrase_split = phrase.split()

total_avg = 0
amount = 0

#count values to figure out the average score for the phrase
for word in phrase_split:
    if word in sentiment:
        avg_score = sentiment[word][1] / sentiment[word][0]
        print('* \'', word, '\' appears ', sentiment[word][0], ' times with an average score of ', avg_score, sep = '')
        total_avg += avg_score
        amount += 1
    else:
        print('* \'', word, '\' does not appear in any movie reviews', sep = '')

#if no words appear in reviews
if amount == 0:
    print('Not enough words to determine sentiment.')
#else display the average and if > 2 display as a positive statement.
#if less, display asnegative
else:
    print('Average score for this phrase is:', total_avg / amount)
    if (total_avg / amount) > 2:
        print('This is a POSITIVE phrase')
    else:
        print('This is a NEGATIVE phrase')

    
