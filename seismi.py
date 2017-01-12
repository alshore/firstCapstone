import urllib
import json
from collections import namedtuple

url = "http://www.seismi.org/api/eqs/"
url += raw_input("Enter the year to check: ")
url += "/"
url += raw_input("Enter the month (03 for March): ")
url += "?"
url += "min_magnitude="
url += raw_input("Enter minimum magnitude: ")

result = urllib.urlopen(url)
data = json.loads(result.read())

print data

xit = raw_input("Do you want to continue? ")