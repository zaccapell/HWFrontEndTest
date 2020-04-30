import classifications
import extractions
import json

# BK = classifications.find_values('Black Knight', ['Closing Disclosure', 'Credit Report', 'Security Intrument Rider - ARM', 'W2'])
# GG = classifications.find_values('Google', ['Closing Disclosure', 'Credit Report', 'Security Intrument Rider - ARM', 'W2'])
# HW = classifications.find_values('Heavywater', ['Closing Disclosure', 'Credit Report', 'Security Intrument Rider - ARM', 'W2'])
# WB = classifications.find_values('We Bank', ['Closing Disclosure', 'Credit Report', 'Security Intrument Rider - ARM', 'W2'])
# print(BK)

# classifications.cleaner('Black Knight')

# x = extractions.group_sort(extractions.find_values('W2'))
# print(x)

# extractions.exports()
# print(list(json.load(open('./documents-file-map.json'))))

print(extractions.exports())
