import csv

inputFileName = '1.txt'
outputFileName = 'output.csv'

START = '____________________________________________________________\n'
BODY = 'Full text:'
SUBJECT = 'Subject:'
DATE = 'Publication date:'

allNews = {}

with open(inputFileName, 'r', encoding='utf-8') as file:
    lineNumber = 0
    lineInSingleNews = 0
    titleInSingleNews = ''
    contentInSingleNews = ''
    isContent = False

    while line := file.readline():

        if (line == START):
            lineInSingleNews = 0
            contentInSingleNews = ''

        # title
        if (lineInSingleNews == 2):
            titleInSingleNews = str(lineNumber) + '_' + line.replace('\n', '')
            allNews[titleInSingleNews] = {}

        # date
        if (line.startswith(DATE)):
            dateInSingleNews = line.replace('\n', '').replace(DATE, '').replace('\xa0', '')
            allNews[titleInSingleNews]['date'] = dateInSingleNews

        if (line.startswith(BODY)):
            isContent = True

        if (line.startswith(SUBJECT)):
            isContent = False
            allNews[titleInSingleNews]['body'] = contentInSingleNews.replace('\n', '').replace(BODY, '').replace('\xa0', '')

        if (isContent and (not line.startswith('Credit:')) and (not line.startswith('Subscribe to WSJ:')) ):
            contentInSingleNews = contentInSingleNews + line 

        lineInSingleNews = lineInSingleNews + 1
        lineNumber = lineNumber + 1


# print(news)

fields = [ 'title', 'body', 'date' ]

# write nested dic to csv
with open(outputFileName, "w", encoding='utf-16', newline='') as f:
    w = csv.DictWriter(f, fields)
    for key, val in allNews.items():
        row = {'title': key}
        row.update(val)
        w.writerow(row)
                   