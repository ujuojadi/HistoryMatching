# "NAME: JESSICA OBIANUJU OJADI "
# "LINKEDIN NAME: JESSICA OJADI"
# "LINKEDIN URL: https://www.linkedin.com/in/jessica-ojadi-6b1877118"

# TO CALCULATE THE TIME COEFFICIENT
from matplotlib import pyplot as plt

perm= int(input("Enter your permeabilty: " ))
porosity = float(input("Enter your porosity: "))
viscosity = float(input("Enter your viscosity: "))
constantF= float(input("Enter your pore compressibility constant: "))
constantW= float(input("Enter your water compressibility constant: "))
constant =constantW + constantF
radius = float(input("Enter your radius:"))
timeYear = int(input("Enter the number of years:"))

td  = (2.309* perm ) / (porosity * viscosity * constant * (radius**2))
td = round(td, 2)
print(td)
print(f"Dimensionless time coefficient is {td}t with respect to t")
timeD ={i: round((td* i),3)  for i in range(0, timeYear)}
print(f"Dimensionless Time = {timeD}")



# TO CALCULATE THE ACQUIFER

print("calculating  Acquifer ")
TotalD = float(360)
influxD= float(input("Enter your influxD:" ))
porosity = float(input("Enter your porosity:"))
height = float(input("Enter your height:"))
constantF= float(input("Enter your pore compressibility constant: "))
constantW= float(input("Enter your water compressibility constant: "))
constant =constantW + constantF
radius = float(input("Enter your radius:"))
freq = influxD / TotalD
AcquiferC = (1.119 * freq * porosity *height *constant * (radius **2))
AcquiferC = round(AcquiferC)
print(f" U = {AcquiferC} bbl/psi")

# TO CALCULATE THE 	Wd AT r10

print("calculating Wd at r10.....")
def floats(n, word):
	nums = []
	print(f"{word}")
	for i in range(0, n):
		d = float(input())
		nums.append(d)
	print(nums)
	return nums

pressureT = floats(timeYear, "Enter the values of change in pressure(p) at r10")
waterT = floats(timeYear, "Enter the values of Cumulative Water Influx at r10 (Wd)")

waterInflux10 =  [[i * j for i in pressureT] for j in waterT[::-1]]
# print(f"Wd at r10 =  {waterInflux10}")

def calc(x, y, z):
	breed=[]
	while y<10:
		breed.append(x[y][z])
		y +=1
		z+=1
	return breed

def yes(beef):
	block = []
	j=0
	for i in range(0, timeYear):
		ble= AcquiferC * sum(calc(beef, i, j))
		ble = round(ble/1000000, 3)
		block.append(ble)
	block = block[::-1]
	return block

We10 = yes(waterInflux10)
print(f"Wd at r10 = {We10}")

# TO CALCULATE Wd AT r5

print("calculating Wd at r5.....")

waterT = floats(timeYear, "Enter the values of Cumulative Water Influx  at r5 (Wd)")

waterInflux5 =  [[i * j for i in pressureT] for j in waterT[::-1]]
We5 = yes(waterInflux5)
print(f"We at r5 = {We5}")


# MBC TO CALCULATE THE F AND E

nN = float(input("Enter OOIP: "))
Bw = float(input("Enter FormationVol factor for water: "))
Swc = float(input("Enter water Saturation: "))



print("calculating  values of F")
Np = floats(timeYear, "Enter the values of Cumulative Oil produced(Np)")
Bo = floats(timeYear, "Enter the values of Formation Vol factor for Oil(Bo)")
Bg = floats(timeYear, "Enter the values ofFormation Vol factor of gas(Bg)")
Rs = floats(timeYear, "Enter the values of  Solution GOR(Rs)")
Rp = floats(timeYear, "Enter the values of cumulative producing GOR(Rp)")

def solve(Np,Bo, Rp, Rs, Bg):
	blep=[]
	for i in range(0, timeYear):
		Fo = round(Np[i] * (Bo[i] + ((Rp[i] -Rs[i]) *Bg[i])), 3)
		blep.append(Fo)
	print(blep)
	return blep

Mmrb = solve(Np, Bo, Rp, Rs, Bg)
print(f"F = {Mmrb}")

print("calculating  values of E...")
# Bo = floats(timeYear, "Enter the values of Formation Vol factor for Oil(Bo)")
Boi = floats(1, "Enter the initial value Formation Vol factor for Oil(Boi)")
# Rs = floats(timeYear, "Enter the values of  Solution GOR(Rs)")
Rsi = floats(1, "Enter the initial value Solution GOR(Rsi)")
# Bg = floats(timeYear, "Enter the values ofFormation Vol factor of gas(Bg)")

def solved(Bo, Boi, Rs, Rsi, Bg):
	lope = []
	Boi = Boi * timeYear
	Rsi =Rsi * timeYear
	for i in range(0, timeYear):
		Eo = round(((Bo[i] -Boi[i]) + (Rsi[i] - Rs[i]) * Bg[i]), 4)
		lope.append(Eo)
	return lope

rbStb = solved(Bo, Boi, Rs, Rsi, Bg)
print(f"E = {rbStb}")

def ratio(m1, m2):
	ratioR = []
	for i in range(0, timeYear):
		ratioO = round((m1[i]/m2[i]), 1)
		ratioR.append(ratioO)
	return ratioR

FEo = ratio(Mmrb, rbStb)
WeEo10 = ratio(We10, rbStb)
WeEo5 = ratio(We5, rbStb)

print(f"F/Eo = {FEo}")
print(f"We/Eo at r10 = {WeEo10}")
print(f"We/Eo at r5 = {WeEo5}")


# PLOTTING THE GRAPH

Npintercept =[312]
x10base = [0]
x5base = [0]
Npintercept.extend(FEo)
x10base.extend(WeEo10)
x5base.extend(WeEo5)
plt.plot(x10base, Npintercept, color='k', marker='.', linestyle='--', label="rd10")
plt.plot(x5base, Npintercept, color='b', marker='*', label="rd5")
plt.title("A graph of F/Eo and W/Eo at rd10 and rd5")
plt.xlabel("W/Eo(MMstb)")
plt.ylabel("F/Eo(Mmstb)")
plt.legend()
plt.show()



















