file = open("usdtoinr.csv", "r")
print("Enter dates in format m/d/yyyy")
start = raw_input("Enter the starting date: ")
end = raw_input("Enter the ending date: ")
"""
for aline in file:
	test_samples = aline.strip().split(",")
	if(start == test_samples[0]):
		start1 = test_samples[1]
	if(end == test_samples[0]):
		end1 = test_samples[1]
print(float(start1)-float(end1))
file.close()
"""
# Code displays the prices from start date to end date.
for aline in file:
	test_samples = aline.strip().split(",")
	if(start == test_samples[0]):#Finds the start of the datalist
		pass# If found just pass and print he price.
	print(test_samples[1])
	if(test_samples[0] == end):#Finds the end value entered by the user.
		file.close()# If found closes the file and exits from the program
		exit()
	


