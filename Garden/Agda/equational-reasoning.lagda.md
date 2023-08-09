1:

```agda
data _≡_ {A : Set} : A → A → Set where
  refl : {x : A} → x ≡ x
infix 4 _≡_

-- symmetry of equality
sym : {A : Set} {x y : A} → x ≡ y → y ≡ x
sym refl = refl
-- transitivity of equality
trans : {A : Set} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans refl refl = refl
-- congruence of equality
cong : {A B : Set} {x y : A} → (f : A → B) → x ≡ y → f x ≡ f y
cong f refl = refl
```

```agda
data Nat : Set where
  zero : Nat
  suc : Nat → Nat

_+_ : Nat → Nat → Nat
zero + y = y
(suc x) + y = suc (x + y)



begin_ : {A : Set} → {x y : A} → x ≡ y → x ≡ y
begin p = p
_end : {A : Set} → (x : A) → x ≡ x
x end = refl
_=⟨_⟩_ : {A : Set} → (x : A) → {y z : A} → x ≡ y → y ≡ z → x ≡ z
x =⟨ p ⟩ q = trans p q
_=⟨⟩_ : {A : Set} → (x : A) → {y : A} → x ≡ y → x ≡ y
x =⟨⟩ q = x =⟨ refl ⟩ q
infix 1 begin_
infix 3 _end
infixr 2 _=⟨_⟩_
infixr 2 _=⟨⟩_




proof1 : (m n : Nat) → m + suc n ≡ suc (m + n)
proof1 zero zero = refl
proof1 zero (suc n) = refl
proof1 (suc k) n =
  begin
    (suc k + suc n)
  =⟨ cong suc (proof1 k n) ⟩
    suc (suc k + n)
  end
```

```agda
data List (A : Set) : Set where
  [] : List A
  _::_ : A → List A → List A


length : {A : Set} → List A → Nat
length [] = zero
length (x :: xs) = suc (length xs)


replicate : {A : Set} → Nat → A → List A
replicate zero x = []
replicate (suc n) x = x :: replicate n x


proof2 : {A : Set} → (n : Nat) → (x : List A) → length (replicate n x) ≡ n
proof2 zero x = refl
proof2 (suc n) [] =
  begin
    suc (length (replicate n []))
  =⟨ cong suc (proof2 n []) ⟩
    suc n
  end
proof2 (suc n) (x :: xs) =
  begin
    length (replicate (suc n) (x :: xs))
  =⟨ cong suc (proof2 n (x :: xs)) ⟩
    suc n
  end
```
