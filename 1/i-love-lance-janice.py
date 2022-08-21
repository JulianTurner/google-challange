def solution(x):
	LOWER_START = 97
	CHARACTER_COUNT = 25

	output = '';

	#for each character in the string
	for i in range(len(x)):
	#if the character is a alphabetical character
		if x[i].isalpha():
			#if the character is a lowercase character
			if x[i].islower():
				#change [a..z] is replaced with the corresponding one in [z..a]
				# get the ascii value of the character in the alphabet
				ascii_value = ord(x[i])
				#print('lower scii value: ', ascii_value)
				# get the position of the character in the alphabet
				position = ascii_value - LOWER_START
				#print('lower postion alphabet:', position)
				new_ascii_value = LOWER_START + CHARACTER_COUNT - position
				#print('lower postion ascii:', new_ascii_value)
				#print(chr(new_ascii_value))
				output += chr(new_ascii_value)
			#if the character is a uppercase character
			if x[i].isupper():
				output += x[i]
		#if the character is a non alphabetical character then return the character
		else:
			output += x[i]
	print(output)


solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")