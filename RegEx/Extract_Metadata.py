import re

f = open('data/Reuter_Corpus/reut2-000.sgm', 'r')
for line in f:
    datetime = re.search('<DATE>\s*([^\s]+?)\s+(.+?)<\/DATE>',line)
    title = re.search('<TITLE>(.+?)<\/TITLE>',line)
    location = re.search('<DATELINE>\s*(.+?),',line)
    end = re.search('</REUTERS>',line)
    if datetime:
        print("Date: " + datetime.group(1))
        print("Time: " + datetime.group(2))
    elif title:
        print("Title: " + title.group(1))
    elif location:
        print("Location: " + location.group(1))
    elif end:
        print
f.close()
