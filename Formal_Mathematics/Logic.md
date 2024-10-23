# Logic

## Terms and Definitions

Proposition : is a statement that is either true or false. 

Implication :  P -> Q has the truth table P = P Q . 

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