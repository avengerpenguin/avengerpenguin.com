Showing equivalence between the forms:

```
f: (a, b) -> c
g: a -> b -> c
```

```coq
Require Import Coq.Init.Datatypes.

Parameters A B C : Set.

Definition curry (f:  A * B -> C) := fun a => fun b => f (a, b).
Definition uncurry (g: A -> B -> C) := fun p => g (fst p) (snd p).
```

```coq
Theorem inv : forall f a b, uncurry (curry f) (a,b) = f(a,b).
Proof.
  intros.
  unfold curry, uncurry.
  simpl.
  reflexivity.
Qed.
```

```coq
Theorem inv2 : forall g a b, curry (uncurry g) a b = g a b.
Proof.
  intros.
  unfold curry, uncurry.
  simpl.
  reflexivity.
Qed.
```
