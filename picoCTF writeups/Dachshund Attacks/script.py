import owiener

e= 32400602412872852778393972484623781579537845813330656619686816284095459468564676335322989571735039469603991835385320831150155789870154059089926421259249664194838210283087742287534066696568540960771110377155151200042881535024902541308926263940902204850114424370400196766565727879457079638882611099814399771353
n= 144931067782173472082261840232961327225764782074821665349472404547293156792748532083745480518432642300672229277728650322770781246061655139453659612368204716729231682575882413757672788673948275809780507549823383569780435501150831216384343414727154443948343048465555728745926437586047890230682454478041952453133

d = owiener.attack(e, n)

if d is None:
    #print("Failed")
else:
    print("Hacked d={}".format(d))
    
#d= put the value of d you get here
c=6460399147538247613054191413464402487060199648137456785525526699573262618355297904729372320892925925000176991302363422918297891637282105188829348275914715018443981785025746899796567377202810419915660413940061116734274588900749794264748930605480877763990029633428908002686917034953175071858461510217619857961

print(hex(pow(c,d,n)))