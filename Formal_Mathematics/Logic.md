# Logic

## Terms and Definitions

Proposition : is a statement that is either true or false.  
Axiom : is a statement that is assumed to be true.  
logical deductions(inference rules) : are used to prove new propostions using previously proved one  
Proof : a proof is a method to ascertain the truth of a proposition. a proof is built from sequences of logical deductions, previously proven statements, and axioms.  



Implication : is a fundamental inference rule. a Proof of P taken together P implies Q is a proof of Q  
$ P \rightarrow Q $ has the truth table $P = P \land Q $. 
the implication truth table is as below.  and you can that if P is true and P implies Q is true, then Q is true. 
  
$ \begin{array}{|c|c|c|}
P & Q & P \rightarrow Q \\
\hline
T & T & T \\
T & F & F \\
F & T & T \\
F & F & T \\
\end{array} $

## Lean 

in Lean, we can define a proposition as a type. 

```lean
P : Prop -- P is a proposition
#check(P) -- Prop
```
a hypothesis of a proposition is an element of the proposition type. 

```lean
example( hP : P) : P := by -- hp is a proof of P
    exact hP

```

The implication which is also a proposition can be defined as below. 

```lean
P → Q -- P implies Q
#check(P → Q) -- Prop
```