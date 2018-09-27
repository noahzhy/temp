
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
* `exact` means
* Using `Qed` to end the demonstration.
