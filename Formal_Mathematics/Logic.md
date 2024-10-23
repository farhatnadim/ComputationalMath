# Logic

## Terms and Definitions

Proposition : is a statement that is either true or false. 

Implication :  $ P \rightarrow Q $ has the truth table $P = P \land Q $. Implication is by itself another proposition 
the truth table is latex is as below.  
  
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

The implication which is also a proposition can be defined as below. 

```lean
P → Q -- P implies Q
#check(P → Q) -- Prop
```