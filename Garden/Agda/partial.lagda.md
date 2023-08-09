Proof of associativity of partial functions:

```agda
open import Data.Maybe using (Maybe ; just ; nothing)
import Data.Maybe as Maybe

open import Level renaming (zero to lzero)

open import Function using (const) renaming (_∘_ to _∘ᶠ_)

open import Data.Fin using (Fin) renaming (zero to fz ; suc to fs)
open import Data.Empty
open import Relation.Nullary
open import Data.Unit using (⊤ ; tt)
open import Data.Bool
open import Data.Sum as Sum

open import Data.Maybe using (Maybe ; just ; nothing)
import Data.Maybe as Maybe

open import Category.Monad

open import Relation.Binary
open import Relation.Binary.Core
open import Relation.Binary.PropositionalEquality using ([_] ; inspect ; sym ; cong)

_⇀_ : ∀ {ℓ} → Set ℓ → Set ℓ → Set ℓ
A ⇀ B = A → Maybe B
```

```agda
Subset : ∀ {ℓ} → Set ℓ -> Set ℓ
Subset A = A → Maybe A

dom : ∀ {ℓ} → {A B : Set ℓ} → (A ⇀ B) → Subset A
dom f a with f a
... | just x = just a
... | nothing = nothing

_∙_ : ∀ {ℓ} → {A B C : Set ℓ} → (B ⇀ C) → (A ⇀ B) → (A ⇀ C)
(g ∙ f) a with f a
... | just b = g b
... | nothing = nothing
infixr 9 _∙_


data _≡_ {A : Set} : A → A → Set where
  refl : {x : A} → x ≡ x
infix 4 _≡_

_≈_ : {A B : Set} → Rel (A ⇀ B) lzero
f ≈ g = ∀ a → f a ≡ g a

infix 0 _≈_


∙-assoc : {A B C D : Set} (f : A ⇀ B) (g : B ⇀ C) (h : C ⇀ D) → (h ∙ g) ∙ f ≈ h ∙ (g ∙ f)
∙-assoc f g _ a with f a
... | nothing = refl
... | just b with g b
... | nothing = refl
... | just x = refl

```
