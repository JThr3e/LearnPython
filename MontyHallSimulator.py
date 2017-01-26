import random
i = 0
winSwitch = 0
loseSwitch = 0
winRS = 0
winNoSwitch = 0
loseNoSwitch = 0
winRNS = 0
runs = 9
while i < runs:
	i+=1
	sel = [1,0,0]
	pos = [0,0,0]
	j = 0
	for a in pos:
		index = random.randint(0, len(sel)-1)
		pos[j] = sel[index]
		del sel[index]
		j+=1
	pick = random.randint(0,2)
	k = 0
	goatIndecies = []
	for b in pos:
		#print("b: "+str(b))
		#print("k: "+str(k))
		if b == 0 and k != pick:
			goatIndecies.append(k)
		k+=1
	hostPickIndex = random.randint(0, len(goatIndecies)-1)
	hostPick = goatIndecies[hostPickIndex]
	
	#print("pos: " + str(pos))
	#print("goats: " + str(goatIndecies))
	#print("pick: " + str(pick))
	#print("hPick: " + str(hostPick))
	#print("=============================")
	
	switch = 0
	if (pick + hostPick) == 1:
		switch = 2
	if (pick + hostPick) == 2:
		switch = 1
	if (pick + hostPick) == 3:
		switch = 0
	#print("switch: " + str(switch))
	#print("=============================")
	
	if(pos[switch] == 1):
		winSwitch += 1
	else:
		loseSwitch += 1
	if(pos[pick] == 1):
		winNoSwitch += 1
	else:
		loseNoSwitch += 1
winRS = winSwitch / runs
winRNS = winNoSwitch / runs
print("winSwitch: " + str(winSwitch))
print("loseSwitch: " + str(loseSwitch))
print("winNoSwitch: " + str(winNoSwitch))
print("loseNoSwitch: " + str(loseNoSwitch))
print("Win Ratio Switch: " + str(winRS))
print("Win Ration No Switch: " + str(winRNS))

	
	
		
	
	


