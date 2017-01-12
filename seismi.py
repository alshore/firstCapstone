import urllib
import json
# generate url
url = "http://www.seismi.org/api/eqs/"
url += raw_input("Enter the year to check: ")
url += "/"
url += raw_input("Enter the month (03 for March): ")
url += "?"
url += "min_magnitude="
url += raw_input("Enter minimum magnitude: ")
# use urllib to open url
result = urllib.urlopen(url)
# read json data from url
data = json.loads(result.read())
# print json info as dictionary
print data
# just so the results appear and stay (not disappear)
xit = raw_input("Do you want to continue? ")