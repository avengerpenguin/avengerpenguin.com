```agda
data Nat : Set where
  zero : Nat
  suc : Nat → Nat


data Vec (A : Set) : Nat → Set where
  [] : Vec A zero
  _::_ : {n : Nat} → A → Vec A n → Vec A (suc n)
infixr 5 _::_
```

Down from:

```agda
downFrom : (n : Nat) → Vec Nat n
downFrom zero = []
downFrom (suc n) = n :: downFrom n

```

Tail:

```agda
head : {A : Set}{n : Nat} → Vec A (suc n) → A
head (x :: xs) = x
tail : {A : Set}{n : Nat} → Vec A (suc n) → Vec A n
tail (x :: xs) = xs
```

Dot product:

```agda
_+_ : Nat → Nat → Nat
zero + y = y
(suc x) + y = suc (x + y)

_*_ : Nat → Nat → Nat
zero * _ = zero
(suc x) * y = y + (x * y)


dotProduct : {n : Nat} → Vec Nat n → Vec Nat n → Nat
dotProduct [] [] = zero
dotProduct (x :: xs) (y :: ys) = (x * y) + dotProduct xs ys
```

```agda
data Fin : Nat → Set where
  zero : {n : Nat} → Fin (suc n)
  suc : {n : Nat} → Fin n → Fin (suc n)

lookupVec : {A : Set} {n : Nat} → Vec A n → Fin n → A
lookupVec (x :: xs) zero = x
lookupVec (x :: xs) (suc i) = lookupVec xs i

putVec : {A : Set}{n : Nat} → Fin n → A → Vec A n → Vec A n
putVec zero y (x :: xs) = y :: xs
putVec (suc i) y (x :: xs) = x :: putVec i y xs
```

Pair:

```agda
data Σ (A : Set) (B : A → Set) : Set where
  _,_ : (x : A) → B x → Σ A B


data _×_ (A B : Set) : Set where
  _,_ : A → B → A × B
infixr 4 _,_

_×’_ : (A B : Set) → Set
A ×’ B = Σ A (λ _ → B)

to : {A B : Set } -> (A × B) → (A ×’ B)
to (a , b) = a , b

from : {A B : Set } -> (A ×’ B) → (A × B)
from (a , b) = a , b

data List (A : Set) : Set where
  [] : List A
  _::_ : A → List A → List A

List’ : (A : Set) → Set
List’ A = Σ Nat (Vec A)

fstΣ : {A : Set}{B : A → Set} → Σ A B → A
fstΣ (x , y) = x

sndΣ : {A : Set}{B : A → Set} → (z : Σ A B) → B (fstΣ z)
sndΣ (x , y) = y

[]’ : {A : Set} → List’ A
[]’ = (zero), []

_::’_ : {A : Set} → A → List’ A → List’ A
x ::’ xs = (suc (fstΣ xs)) , x :: sndΣ xs


length : {A : Set} → List A → Nat
length [] = zero
length (x :: xs) = suc (length xs)

to2 : {A : Set} → List A → List’ A
to2 [] = zero , []
to2 (x :: xs) = suc (fstΣ (to2 xs)) , x :: sndΣ (to2 xs)


from2 : {A : Set} → List’ A → List A
from2 (zero , []) = []
from2 ((suc n) , x :: xs) = x :: from2 (n , xs)

```
