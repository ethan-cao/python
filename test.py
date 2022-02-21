filename = 'test.csv'

# counter is a dictionary
# topic -> its frequency
# this needs to be created outside the loop!!!
counter = {}

# first, remove quotes(") and empty string ( ) from the csv file directly using sublime text
# so we have simple input to handle

with open(filename, 'r', encoding='utf-8') as file:
    while line := file.readline().strip():
        # split by ,
        topic_list = line.split(',')
        # print(topic_list)
        # remove empty ones
        unique_topic_list = list(filter(None, topic_list))
        # print(unique_topic_list)

        # now we can count the frequency

        # check each topic
        for topic in unique_topic_list:
            if topic in counter:
                # if the topic already in the dictionary, take current count and increase 1
                current_count = counter.get(topic)
                counter[topic] = current_count + 1
            else:
                # if the topic is not in the dictionary, set the frequency to 1
                counter[topic] = 1


print('counter is ')
print(counter)