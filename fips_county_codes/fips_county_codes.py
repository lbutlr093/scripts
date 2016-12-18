import urllib
import os

fipsfile = urllib.URLopener()
fipsfile.retrieve("http://www2.census.gov/geo/docs/reference/codes/files/national_county.txt", "fips_codes.txt")

## Open txt - replace ',' with '|' and remove index(2) column
with open("fips_codes.txt") as inputfile:
	with open("fips_county_codes.txt", "w") as outputfile:
		for line in inputfile:
			fields = line.split(",")
			fields.pop(1)
			outputfile.write("|".join(fields))

## Clean up
os.remove("fips_codes.txt")