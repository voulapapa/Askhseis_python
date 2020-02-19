#ΕΡΓΑΣΙΑ: 9
#Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει έναν αριθμό τον τριπλασιάζει, προσθέτει ένα και στην συνέχεια προσθέτει τα ψηφία του. Η διαδικασία επαναμβάνεται μέχρι ο αριθμός να γίνει μονοψήφιος
num =int( input('Give a number:'))
digitsum = 0 
num  =  num  * 3 + 1
while len(str(num)) > 1  :
    listnum=str(num)
    listnum=list(listnum) 
    for i in listnum:
        digitsum= digitsum + int(i)
        num = digitsum
    digitsum=0
    print(num)
print ('to teliko noymero einai:',num)  
