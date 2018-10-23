import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows

	file = open(file, "r")
	file_list = file.readlines()
	headings = file_list[0].rstrip('\n').split(',')
	del file_list[0]
	data_list = []

	for line in file_list:
		data_dict = {}
		line_list = line.rstrip('\n').split(',')
		index = 0
		for heading in headings:
			data_dict[heading] = line_list[index]
			index += 1
		data_list.append(data_dict)

	return data_list

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	data_list = sorted(data, key=lambda k: k[col])
	return (data_list[0].get("First") + " " +  data_list[0].get("Last"))


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	senior = 0
	junior = 0
	sophomore = 0
	freshman = 0

	for dictionary in data:
		year = dictionary.get("Class")
		if year == "Senior":
			senior += 1
		if year == "Junior":
			junior += 1
		if year == "Sophomore":
			sophomore += 1
		if year == "Freshman":
			freshman += 1

	tuple_list = [('Senior', senior), ('Junior', junior), ('Sophomore', sophomore), ('Freshman', freshman)]
	return sorted(tuple_list, key=lambda k: k[1], reverse = True)


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	month_list = {}
	for dictionary in a:
		dob = dictionary["DOB"]
		month = dob.split("/")[0]
		month_list[month] = month_list.get(month, 0) + 1
	return int(sorted(month_list, key = month_list.get)[-1])

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	file = open(fileName, 'w')

	data_list = sorted(a, key = lambda k: k[col])

	for person in data_list:
		first = person['First']
		last = person['Last']
		email = person['Email']
		file.write(first + ',' + last + ',' + email + '\n')
	file.close()

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	num_ppl = 0
	total = 0
	today = date.today()

	for person in a:
		num_ppl += 1
		dob = person["DOB"].split('/')
		y = today.year - int(dob[2])
		total += y

	return int(total / num_ppl)


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
