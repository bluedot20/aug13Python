def mostfrqletter(s): 
	s = s.lower()
	s = s.replace(" ", "")
	maxCount = 0 
	maxLetter = ""

	for i in range(0, len(s)): 
		if s.count(s[i]) > maxCount: 
			maxCount = s.count(s[i])
			maxLetter = s[i]
		if s.count(s[i]) == maxCount: 
			if s[i] < maxLetter: 
				maxLetter = s[i]
				maxCount = s.count(s[i])
	return maxLetter

print(mostfrqletter("we attacK AT DAWN"))			


# print(ord("a"))
# print(chr(97))
# print("a" > "b")
# print("A" > "a")


