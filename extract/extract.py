import csv

inputFileName = 'test_nyt.txt'
outputFileName = 'output.csv'

END_OF_DOCUMENT = 'End of Documen\n'
BODY = 'Body\n'
LANGUAGE = 'Language:'
LENGTH = 'Length:'
DATE = 'Load-Date:'

allNews = {}
news = {}


with open(inputFileName, 'r', encoding='utf-8') as file:
    lineNumber = 0
    lineInSingleNews = 0
    titleInSingleNews = ''
    contentInSingleNews = ''
    isContent = False

    while line := file.readline():

        if (line == END_OF_DOCUMENT):
            lineInSingleNews = 0
            contentInSingleNews = ''

        # title
        if (lineInSingleNews == 3):
            titleInSingleNews = str(lineNumber) + '_' + line.replace('\n', '')
            allNews[ titleInSingleNews] = {}

          # if titleInSingleNews in news:
          #   news[titleInSingleNews] = news[titleInSingleNews] + 1 
          # else:
          #   news[titleInSingleNews] = 1

        # date
        if (line.startswith(DATE)):
            dateInSingleNews = line.replace('\n', '').replace(DATE, '').replace('\xa0', '')
            allNews[titleInSingleNews]['date'] = dateInSingleNews

        # count
        if (line.startswith(LENGTH)):
            countInSingleNews = line.replace('\n', '').replace(LENGTH, '').replace('\xa0', '')
            allNews[titleInSingleNews]['count'] = countInSingleNews

        if (line == BODY):
            isContent = True

        if (line.startswith(LANGUAGE)):
            isContent = False
            allNews[titleInSingleNews]['body'] = contentInSingleNews.replace('\n', '').replace('Body', '').replace('\xa0', '')

        if (isContent and (not line.startswith('http')) and (not line.startswith('Classification')) and (not line.startswith('Graphic'))):
            contentInSingleNews = contentInSingleNews + line 

        lineInSingleNews = lineInSingleNews + 1
        lineNumber = lineNumber + 1


# print(news)

fields = [ 'title', 'count', 'body', 'date' ]

# write nested dic to csv
with open(outputFileName, "w", encoding='utf-16', newline='') as f:
    w = csv.DictWriter(f, fields)
    for key, val in allNews.items():
        row = {'title': key}
        row.update(val)
        w.writerow(row)
                   