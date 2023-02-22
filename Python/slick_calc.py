# In which we attempt to calculate birth and death rates for a population over a given number of years
# Inspired by Samsons Lock: OGW, Grix's Echidna Slickwolves


#Stats of the Slickwolf Population
Starting_Population = 50 # 25 m, 25f, they partner for like, so gender will be ignored (for now)
Breeding_Interval = 1 # How long to birth one batch of pups (In Years)
Litter_Size = 5 #Five Pups per litter
Maturity_Age = 3 #How old a wolf need to be to mate
Death_Age = 15 #age that a wolf dies
Final_Year = 15 #How far out to calculate

#Init Generation List
year = 0 #starts at zero, +1 per loop
population = [Starting_Population]
age = [Maturity_Age]

#Calculation function
def breed(Year):
	count = 0
	for i in age:
		#if  i >= Death_Age or i == "Dead":
		#	population[count] = 0
		#	age[count] = "Dead"
		if i >= Maturity_Age - 1:				#Make Elif when death is feasible
			births = Litter_Size * int(population[count]/2)
			if count == 0:
				population.append(births)
			else:
				population[Year] += births
			age[count] += 1
		else:
			age[count] += 1
		count += 1
	age.append(0)
			

# Main While Loop
print("Slickwolves detected, calculating population rates...")
while year < Final_Year:
	counter = 0
	sum = 0
	print("Year " + str(year) + ":")
	for i in population:
		print("\tGeneration " + str(counter) + ":\t" + str(age[counter]) + "yo\t" + str(i) + " slickwolves")
		sum += i
		counter += 1
	print(str(sum) + " Slickwolves Total\n")
	year += 1
	breed(year)
	

