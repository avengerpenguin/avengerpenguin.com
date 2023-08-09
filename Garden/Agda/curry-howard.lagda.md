```agda
data Either (A : Set) (B : Set) : Set where
  left : A → Either A B
  right : B → Either A B

cases : {A B C : Set} → Either A B → (A → C) → (B → C) → C
cases (left a) f _ = f a
cases (right b) _ g = g b
```

```agda
data ⊤ : Set where
  tt : ⊤

data ⊥ : Set where
-- no constructors

data _×_ (A B : Set) : Set where
  _,_ : A → B → A × B
infixr 4 _,_

fst : {A B : Set} → A × B → A
fst (x , y) = x
snd : {A B : Set} → A × B → B
snd (x , y) = y

proof1 : {A B : Set} → A → (B → A)
proof1 a b = a

proof2 : {A : Set} → (A × ⊤) → Either A ⊥
proof2 (a , b) = left a

proof3 : {A B C : Set} → (A → (B → C)) → ((A × B) → C)
proof3 f (a , b) = f a b

proof4 : {A B C : Set} → (A × (Either B C)) → Either (A × B) (A × C)
proof4 (a , left b) = left (a , b)
proof4 (a , right c) = right (a , c)

proof5 : {A B C D : Set} → ((A → C) × (B → D)) → ((A × B) → (C × D))
proof5 (f , g) (a , b) = (f a) , (g b)
```

```agda
fun : {P : Set} → (Either P (P → ⊥) → ⊥) → ⊥
fun f = f (right (λ x → f (left x)))
```
