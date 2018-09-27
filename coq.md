# The contents of Coq what I understood
## First of all
**Trips:**

* Every Coq command should be end with `.`  
* Using annotation by `(* COMMENTS HERE *)`

## Hello World
**Start the first proof**  
E.g.
```
Theorem my_first_proof : (forall A : Prop, A -> A).
Proof.
  intros A.
  intros proof_of_A.
  exact proof_of_A.
Qed.
```

* Using `Theorem` to declare a theorem.
* `forall` means ∀.
* `Prop` means proposition.
* Using `Proof` to start to prove something.
* Using `intros` to introduce some assumptions.
* Using `exact` if the subgoal matches an hypothesis what we can finish the proof by using this assumption.
* Using `Qed` to end the demonstration.

## True or False
It's like a kind of `structure` in C++, and you can create a new type by using command `Inductive`.  

```
Inductive False : Prop := .

Inductive True : Prop :=
  | I : True.

Inductive bool : Set :=
  | true : bool
  | false : bool.
```


## Prop
`Prop` means proposition.

### Connectives and Logical Constants
* `->`, P -> Q means if P then Q. It's just `→` in Discrete mathematics.
* `/\`, P /\ Q means P and Q. It's just `∧` in Discrete mathematics.
* `\/`, P \/ Q means P or Q. It's just `∨` in Discrete mathematics.
* `~`, ~ P means not P. It's just `┐` in Discrete mathematics.
* `<->`, P <-> Q means P is equivalent to Q. P <-> Q ≡ (P -> Q) /\ (Q -> P).

### the first proof of this case
E.g.  
```
Lemma I : P -> P.
  intro p.
  exact p.
Qed.
```

* Using `Lemma` to declare a lemma.
* Using `Proof` to start to prove something.
* Using `intro` to introduce the assumptions.
* Using `exact` if the subgoal matches an hypothesis what we can finish the proof by using this assumption.
* Using `Qed` to end the demonstration.






## Pred










## Bool
### Defining & Operating
#### First of all

**Trips:**  

* `bool = { true , false }` it's a definition.
* `negb` is a function and it can be defined by pattern.

E.g.  
```
Definition negb (b:bool) : bool :=
  match b with
  | true => pattern1
  | false => pattern2
  end.
```

Some boolean functions can be defined easily.  

E.g.
```
Definition andb(b c:bool) : bool :=
  if b then c else false.
```

### Reasoning about Bool
E.g.
```
Lemma negb_idem' : forall b :bool, negb (negb b) = b.
intro b.
destruct b;
  reflexivity.
Qed.
```

* Using `destruct` b creates a case for b = true and one for b = false.
* Using `reflexivity` to make some simplified goals.
