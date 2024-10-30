# Logic

## Terms and Definitions

Proposition : is a statement that is either true or false.  
Axiom : is a statement that is assumed to be true.  
logical deductions(inference rules) : are used to prove new propostions using previously proved one  
Proof : a proof is a method to ascertain the truth of a proposition. a proof is built from sequences of logical deductions, previously proven statements, and axioms.  



Implication : is a fundamental inference rule. a Proof of P taken together P implies Q is a proof of Q  
$P \rightarrow Q$ has the truth table $P = P \land Q$. 
the implication truth table is as below.  and you can that if P is true and P implies Q is true, then Q is true. 
  
$\begin{array}{|c|c|c|}
P & Q & P \rightarrow Q \\
\hline
T & T & T \\
T & F & F \\
F & T & T \\
F & F & T \\
\end{array}$

## Lean 

in Lean, we can define a proposition as a type. 

```lean
P : Prop -- P is a proposition
#check(P) -- Prop
```
a hypothesis or proof  of a proposition is an element of the proposition type, when we used the `exact` keyword as if we are saying that  we provided that proof hP that the proposition is true, so lean closes the proof

```lean
example( hP : P) : P := by -- hp is a proof of P
    exact hP

```

The implication which is also a proposition can be defined as below. 

```lean
P → Q -- P implies Q
#check(P → Q) -- Prop
```

let us do two exercies with implication also by introducing the `intro` and the `apply` keyword. 

Exercise 1 : Assume we know that Q is true. We want to prove the P -> Q is true . From the definition of implication above for P-> Q to be true we need Q true and P true hence the intro keyword which introduces the proposition that P is true and then we use exact to close the argument

```lean
-- Assume `Q` is true. Prove that `P → Q`.
example (hQ : Q) : P → Q := by
  -- The goal is of the form `X → Y` so we can use `intro`
  intro h
  -- now `h` is the hypothesis that `P` is true.
  -- Our goal is now the same as a hypothesis so we can use `exact`
  exact hQ
```
Exercises 2 : Assume  P -> Q is true and P is true deduce that Q is true. `apply` is get when P is true using the implication P -> Q we can deduce that Q is true. 


```lean
example ( h : P → Q) ( hP : P) : Q := by
  -- The goal is `Q` so we can use `apply`
  apply h
  -- The goal is now `P` so we can use `exact`
  exact hP
```
