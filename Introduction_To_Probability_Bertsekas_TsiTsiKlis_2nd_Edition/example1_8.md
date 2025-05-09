### Problem :
#### Statement 
A conservative design team, call it C and an innovative design team call it N , are asked to seperately design a new product within a month.  
from past experience we know that :  
(a) The probability that team C is successfull is 2/3
(b) The probability that team N is successfull is 1/2
(c) The probability that at least one team is is successful is 3/4
#### Question 
Assuming that exactly one successfull design is produced , what is the probability that is was design by team N?

### Solution

#### Given Information 
Let us first read the problem statement, trim uncessary information and extract the necessary ones and rewrite the problem 

Necessary information : 
are asked to design a product : both teams are asked. 
One of the outcomes is success. 
Seperatly : means outcomes of Team A is indepdent from that outcome of Team B . 

#### Assumptions
The sample space has two outcomes , success and failure
when the problem state from past experience , it means when this same experiments were done in the past , the probabilities were as follows 
P(C) is 2/3 means when both teams tried the conservative teams was successfull two third of the time but also in this case the innovative team could have ben successful or unseccessfull 

P(C) is actually = P(CN) + P(CN') where N' is when the N team was not successfull  
P(N) is actually = P(CN) + P(C'N) where C' is when the C team was not successfull 
that's 3 equations 2 unknowns 
At least one team is successfull means P(C'N) +P(CN') - P(CN) = 3/4 
thats 3 equations 3 unknowns 

P(CN) + P(CN')  0*P(C'N)= 2/3
P(CN) + P(C'N)  0*P(CN')= 1/2
-P(CN) + P(CN') + P(C'N)  = 3/4

#### Restatement 

Two teams N and C are asked to create a design a product independently . Previously when these two teams were asked to design 






CN  : Both teams were successfull  ( H H ).
C'N' : Both teams are unsuccessfull  ( T T ).
C'N : Conservative team is not successfull and Innovative Team is successfull ( H T )
CN' : Concervative team is successfull and  Innovative team is successfull  ( T H )
