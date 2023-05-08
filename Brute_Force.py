import string
import random
import itertools
import datetime

# size of password 
N = 4

def brute_force(password, char_list):
	count = 0
	start_time = datetime.datetime.now()
	
	# iterate thru each permutation of characters
	for pwd in itertools.product(char_list, repeat = N):
		permutation = "".join(pwd)
		count += 1
		
		# compare the permutation with the password
		if permutation == password:
		
			# get the time when they matched
			end_time = datetime.datetime.now()
			
			# find the difference between the start time to time the password was found 
			time_delta = end_time - start_time
			seconds = time_delta.total_seconds()
			
			# output the results 
			pwd_str = "Generated password is: " + str(permutation) + "\n"
			print(pwd_str, end='')
			f.write(pwd_str)
			s = permutation.encode('utf-8')
			hex_str = "Generated password in hex is: " + str(s.hex()) + "\n"
			print(hex_str, end='')
			f.write(hex_str)
			count_str = "Found the password after " + str(count ) +  " guesses.\n"
			print(count_str, end='')
			f.write(count_str)
			time_str = "It took " + str(seconds) + " seconds to find the password.\n"
			print(time_str, end='')
			f.write(time_str)
			
			break
			
	return seconds 

# main function of program 
if __name__ == "__main__":

	# create the output file
	f = open("output.txt", "w")
	
	# create the introductory string 
	intro = "Assignment #7 for ICS 462\n\n"
	print(intro, end='')
	f.write(intro)
				
	# create random password of only capital letters 
	password = "".join(random.choices(string.ascii_uppercase, k = N))

	# create list of characters that could be in password
	char_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

	seconds1 = brute_force(password, char_list)

	print()
	f.write("\n")

	# create new list of characters 
	char_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789:;><=?@{}\\_\'')

	# create random password from characters in char_list 
	password = "".join(random.choices(char_list, k = N))

	seconds2 =  brute_force(password, char_list)

	print()
	f.write("\n")
	
	difference = "It took %.2f times as long with the expanded character set to guess the password." % (seconds2/seconds1)

	print(difference)
	f.write(difference)
