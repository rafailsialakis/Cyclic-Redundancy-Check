import math
SNR = int(input("Please input the value of the SNR: "))
sp = math.log(2,1+SNR)
print("Spectral density is",sp)
