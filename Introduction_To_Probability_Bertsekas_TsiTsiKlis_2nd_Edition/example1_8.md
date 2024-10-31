### Problem :
#### Statement 
A conservative design team, call it C and an innovative design team call it N , are asked to sperately design a new product within a month.  
from past experience we know that :  
(a) The probability that team C is successfull is 2/3
(b) The probability that team N is successfull is 1/2
(c) The probability that at least one team is is successful is 3/4
#### Question 
Assuming that exactly one successfull design is produced , what is the probability that is was design by team N?

### Solution
Let us first understand the problem, by highlighting the explicit problem statement 

are asked to design a product : both teams are asked. 
One of the outcomes is success : 
Seperatly : means outcomes of Team A is indepdent from that outcome of Team B . 

Second Let us read the problem statement to see what is needed 

Team C is successfull is 2/3 : there are two possibility that team C was successfull and Team N (CN) not successful or Team C was susccessful and Team N was successful (CN')

P(CN) + P(CN') = 2/3


CN  : Both teams were successfull  ( H H ).
C'N' : Both teams are unsuccessfull  ( T T ).
C'N : Conservative team is not successfull and Innovative Team is successfull ( H T )
CN' : Concervative team is successfull and  Innovative team is successfull  ( T H )

Now we understand the general sample space. now let us understand the conditional probability .  
Assuming that exactly one successful design is produced ( assuming one head shows up ) what is the probability that is designed by team N . so we are looking the probability where team N successed and the other team fail P(C'N)

1 = P(CN) + P(C'N') + P(C'N) + P(CN')
P(C'N') = 1/4 ( probability of no team is successul = 1 -3/4 )
