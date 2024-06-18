msg = "350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213".split()
#print(msg)

mods = [i for i in range(0,37)]
#print(mods)

chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
#print(chars)

d  = {mods[i]:chars[i] for i in range(0,37)}
#print(d)


FLAG = "picoCTF{"

for i in range(len(msg)):
    FLAG += d[int(msg[i]) % 37]
FLAG += "}"


print(FLAG)

#picoCTF{R0UND_N_R0UND_ADD17EC2} -> FLAG