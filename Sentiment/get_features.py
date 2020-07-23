import xlrd
import csv
from textblob import TextBlob
import enchant

file_loc = "C:/Users/Student/Desktop/More Reviewws/Sisters.xlsx"
d = enchant.Dict()

workbook = xlrd.open_workbook(file_loc)
sheet = workbook.sheet_by_index(0)

print(sheet.nrows)

# Positive, Negative, No. of positive, No. of negative, Total
pos = neg = nop = non = tot = 0

for i in range(sheet.nrows):
    sent = sheet.cell_value(i,0).split();
    corrected = ""
    for word in sent:
        if (d.check(word) == 0):
            list = d.suggest(word)
            if (len(list) > 0):
                corrected = corrected + " " + list[0]

        else:
            corrected = corrected + " " + word

            
    sentence = TextBlob(corrected)
    pol = sentence.sentiment.polarity

    if(pol > 0) :
        pos = pos + pol
        nop = nop + 1

    elif(pol < 0) :
        neg = neg + pol
        non = non + 1

    tot = tot + pol


print(nop)
print(pos)
print("\n")
print(non)
print(neg)
print("\n")
print(tot)


with open("features.csv","a") as features:
    writer = csv.writer(features)
    writer.writerow([nop,pos,non,neg])
    
#workbook2 = xlsxwriter.Workbook('Features.xlsx')
#worksheet = workbook2.add_worksheet()

#worksheet.write(0,1,nop)
#worksheet.write(1,1,pos)
#worksheet.write(2,1,non)
#worksheet.write(3,1,neg)

#workbook2.close()
