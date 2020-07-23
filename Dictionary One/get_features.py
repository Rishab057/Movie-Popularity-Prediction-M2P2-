import xlrd
import csv
from textblob import TextBlob
import enchant

d = enchant.Dict()

file_loc = "Uncle.xlsx"
workbook = xlrd.open_workbook(file_loc)
sheet = workbook.sheet_by_index(0)

print(sheet.nrows)

text_file = open("Dict.txt", "r")

word_list = text_file.read().splitlines()

feature_vector = [0]*len(word_list)

for i in range(sheet.nrows):
    sent = sheet.cell_value(i,0).lower()
    sent = sent.split();
    corrected = ""
    for word in sent:
        if (d.check(word) == 0):
            list = d.suggest(word)
            if (len(list) > 0):
                corrected = corrected + " " + list[0]

        else:
            corrected = corrected + " " + word

    corrected = corrected.lower()        
    sentence = TextBlob(corrected)
    pol = sentence.sentiment.polarity

    corrected = corrected.split();

    if(pol >= 0) :
        for word in corrected:
            try:
                if(word_list.index(word) > 103):
                    feature_vector[word_list.index(word)-104]+=1

                elif(word_list.index(word) >= 0):
                    feature_vector[word_list.index(word)]+=1

            except:
                pass
                

    elif(pol < 0) :
        for word in corrected:
            try:
                if(word_list.index(word) >= 0 & word_list.index(word) <= 103 ):
                    feature_vector[word_list.index(word)+104]+=1

                elif(word_list.index(word) >= 104 & word_list.index(word) <= 207):
                    feature_vector[word_list.index(word)]+=1

            except:
                pass
            
print(feature_vector)


with open("features.csv","a") as features:
    writer = csv.writer(features)
    writer.writerow(feature_vector)
    