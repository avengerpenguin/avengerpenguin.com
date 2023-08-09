Exercises from section 1 of https://raw.githubusercontent.com/jespercockx/agda-lecture-notes/master/agda.pdf

```agda
data Nat : Set where
  zero : Nat
  suc : Nat → Nat
```

```agda
halve : Nat → Nat
halve zero = zero
halve (suc zero) = zero
halve (suc (suc n)) = suc (halve n)

{-# BUILTIN NATURAL Nat #-}


_+_ : Nat → Nat → Nat
zero + y = y
(suc x) + y = suc (x + y)

```

Multiplication:

```agda
_*_ : Nat → Nat → Nat
zero * _ = zero
(suc x) * y = y + (x * y)

```

Logic:

```agda
data Bool : Set where
  false : Bool
  true : Bool

not : Bool → Bool
not false = true
not true = false

_&&_ : Bool → Bool → Bool
false && y = false
true && y = y

_||_ : Bool → Bool → Bool
false || y = y
true || y = true

```

Lists:

```agda
data List (A : Set) : Set where
  [] : List A
  _::_ : A → List A → List A


length : {A : Set} → List A → Nat
length [] = zero
length (x :: xs) = suc (length xs)

_++_ : {A : Set} → List A → List A → List A
[] ++ ys = ys
(x :: xs) ++ ys = x :: (xs ++ ys)

map : {A B : Set} → (A → B) → List A → List B
map _ [] = []
map f (x :: xs) = (f x) :: map f xs
```

Maybe:

```agda
data Maybe (A : Set) : Set where
  nothing : Maybe A
  just : A -> Maybe A

lookup : {A : Set} → List A → Nat → Maybe A
lookup [] _ =  nothing
lookup (x :: xs) zero = just x
lookup (x :: xs) (suc n) = lookup xs n

```
