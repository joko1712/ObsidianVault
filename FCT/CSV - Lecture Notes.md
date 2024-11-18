
## Lecture - 4:

### 1. **Historical Context and Foundations**

- **Turing (1949)**: Proposed that program correctness could be assured by attaching assertions that could be checked individually, leading to overall correctness through "routine checking"​.
- **Floyd (1967)**: Introduced assigning logical meanings to programs by attaching "tags" or **assertions** to program statements, which describe expected state transformations​.
- **Hoare (1969)**: Formulated **Hoare Logic**, establishing an **axiomatic basis** for programming and program verification using **Hoare Triples**.

### 2. **Hoare Logic and Hoare Triples**

- **Hoare Triple Notation**: `{P} e {Q}`
    - `P`: **Precondition** before executing `e`.
    - `e`: Program **Expression** or statement.
    - `Q`: **Postcondition** ensuring what must hold after `e` executes.
- **Partial Correctness**: `{P} e {Q}` does not imply termination but asserts that if `e` terminates, `Q` will hold given `P`.
    - Example Hoare Triples:
        - `{x = 1} x := x + 2 {x = 3}`
        - `{x = y} x + y {result = 2y}`
- **Consequences**: Hoare Logic also handles reasoning about complex expressions with logical connectives and conditional constructs​.

### 3. **Rules of Hoare Logic**

- **Basic Rules**:
    - **Skip Rule**: `{P} skip {P}`
    - **Assignment Rule**: `{P[x ↦ t]} x := t {P}`
    - **Sequence Rule**: `{P} e1 {Q} ∧ {Q} e2 {R} ⇒ {P} e1; e2 {R}`
- **Consequence Rule**: ⊢P⇒P′{P′}e{Q′}⊢Q′⇒Q⇒{P}e{Q}\vdash P \Rightarrow P' \quad \{P'\} e \{Q'\} \quad \vdash Q' \Rightarrow Q \Rightarrow \{P\} e \{Q\}⊢P⇒P′{P′}e{Q′}⊢Q′⇒Q⇒{P}e{Q}
    - Enables transforming the pre- and postconditions to derive valid Hoare triples.

### 4. **Loop Invariants and Verification with Loops**

- **Loop Rule**: For loop `{J ∧ t} e {J}`:
    - `J`: **Invariant** that holds before and after each loop iteration.
    - **Verification Condition**:
        - `{J} while t do e {J ∧ ¬t}` ensures that `J` holds upon loop entry, during execution, and after exiting with `¬t`.
    - **Example Proof**:
        - A simple loop incrementing `i` with invariant `0 ≤ i ≤ n` shows how `J` remains true throughout execution and ensures postcondition `i = n` upon termination.

### 5. **Procedures and Method Verification**

- **Procedure Verification**:
    - Each procedure has:
        - **Precondition** (`requires`): Condition that must be true before calling.
        - **Postcondition** (`ensures`): Condition guaranteed after execution.
    - **Verification of Method Calls**:
        - Calls verify **modularly** by assuming the precondition, executing, and ensuring the postcondition.

### 6. **Proof Example: Integer Square Root (ISQRT)**

- **Program**:

		var sum := 1; 
		var count := 0; 
		while sum <= n 
		{ 
			count := count + 1; 
			sum := sum + 2 * count + 1; 
		} 
		return count;
		
- **Specification**:
    - **Goal**: Prove `count` holds the truncated integer square root of `n`.
        - **Postcondition**: `count^2 ≤ n < (count + 1)^2`
- **Loop Invariant**:
    - `sum = (count)^2` and `count^2 ≤ n`
        - **Initialization**: Holds at the start (`count = 0`, `sum = 1`).
        - **Maintenance**: After each increment and update, `sum` and `count` maintain the invariant.
        - **Termination**: When `sum > n`, `count` meets the final condition of a truncated square root.

### 7. **State Transformers in Imperative Programming**

- **State**: A mapping of variables to their values.
- **State Transformation**:
    - A program transforms an initial state to a final state by updating variable mappings through statements.
    - Example: `σ = {x ↦ 1, y ↦ 2, w ↦ 3}`, where execution of `P ≜ x := y + x; w := w - x` results in `σ' = {x ↦ 3, y ↦ 2, w ↦ 0}`.

### 8. **Conditional Constructs and Sequential Composition**

- **Conditionals**:
    - `{P ∧ t} e1 {Q} ∧ {P ∧ ¬t} e2 {Q} ⇒ {P} if t then e1 else e2 {Q}`
- **Loop Rule for While**:
    - `{J ∧ t} e {J} ⇒ {J} while t do e {J ∧ ¬t}`
- These constructs allow reasoning about program flow, preserving invariants within conditional branches and loop bodies.

### 9. **Modular Verification with Dafny Tool**

- **Dafny**:
    - Provides syntax for specifying `requires` (preconditions) and `ensures` (postconditions) for modular program verification.
- **Procedural Verification Example**:
    - For method calls, Dafny checks:
        1. The precondition holds before the call.
        2. The postcondition after the method executes.


## Lecture - 5:

### 1. **Hoare Logic and Loop Verification**

- **Floyd-Hoare Logic Basics**:
    
    - **Hoare Triple**: `{P} e {Q}`, where:
        - `P` (precondition) must hold before executing `e` (program).
        - `Q` (postcondition) must hold after `e` executes.
    - **Consequence Rule**: Allows refining preconditions and postconditions: ⊢P⇒P′{P′}e{Q′}⊢Q′⇒Q⇒{P}e{Q}\vdash P \Rightarrow P' \quad \{P'\} e \{Q'\} \quad \vdash Q' \Rightarrow Q \Rightarrow \{P\} e \{Q\}⊢P⇒P′{P′}e{Q′}⊢Q′⇒Q⇒{P}e{Q}
        - Enables deducing `{P} e {Q}` when intermediate conditions (`P'`, `Q'`) help simplify the proof.
- **Loop Verification with Invariants**:
    
    - **Loop Invariant**: A condition `J` that must hold true:
        1. **Initially**: When entering the loop.
        2. **After Each Iteration**: Maintained after the loop body executes.
        3. **Upon Exit**: Combined with the negated loop condition to imply the postcondition.
    - **Rule for Loops**:
        - Given a loop invariant `J`, the loop `{J ∧ t} e {J}` can be summarized as: {J}while t do e{J∧¬t}\{J\} \text{while } t \text{ do } e \{J \land \neg t\}{J}while t do e{J∧¬t}
        - **Example**:
            - For a simple loop incrementing `i` until `i = n`, we have:
                - **Invariant**: `0 ≤ i ≤ n`
                - **Postcondition**: `i = n` when `i` reaches `n` at loop termination.

### 2. **Detailed Proof Example: Summing First `n` Integers**

- **Program `P`**:

		s := 0; 
		i := 0; 
		while i < n do 
			i := i + 1; 
			s := s + i;
- **Specification**:
    - **Goal**: Verify that `s` computes the sum of the first `n` integers: {0≤n}  P  {s=∑j=1nj}\{0 \leq n\} \; P \; \{s = \sum_{j=1}^{n} j\}{0≤n}P{s=j=1∑n​j}
- **Loop Invariant Construction**:
    - Identify an invariant `J` such that `J` is preserved and implies the final result.
        - **Invariant**: s=∑j=1ij∧0≤i≤ns = \sum_{j=1}^{i} j \land 0 \leq i \leq ns=∑j=1i​j∧0≤i≤n
    - **Proof by Hoare Logic**:
        1. **Initialization**: Before loop:
            - `s = 0`, `i = 0`, which satisfies `J` since `\sum_{j=1}^{0} j = 0`.
        2. **Maintenance**: In the loop body:
            - Increment `i`, then update `s` by adding `i`.
            - Prove the invariant holds after each increment and sum update.
        3. **Termination**: When `i = n`, the invariant implies `s = \sum_{j=1}^{n} j`, thus proving correctness.

### 3. **Weakest Precondition Calculus (WP)**

- **Definition**: For an expression `e` and postcondition `Q`, `WP(e, Q)` finds the weakest precondition `P` such that `{P} e {Q}` holds.
    - **Purpose**: Allows systematic, backward construction of conditions that ensure `Q`.
- **Rules for WP**:
    - **Skip**: `WP(skip, Q) ≡ Q`
    - **Assignment**: `WP(x := t, Q) ≡ Q[x ↦ t]`
    - **Sequence**: `WP(e1; e2, Q) ≡ WP(e1, WP(e2, Q))`
    - **Conditional**: WP(if t then e1 else e2,Q)≡(t⇒WP(e1,Q))∧(¬t⇒WP(e2,Q))WP(\text{if } t \text{ then } e1 \text{ else } e2, Q) ≡ (t \Rightarrow WP(e1, Q)) \land (\neg t \Rightarrow WP(e2, Q))WP(if t then e1 else e2,Q)≡(t⇒WP(e1,Q))∧(¬t⇒WP(e2,Q))
- **Loop Rule with WP**:
    - **Annotated Loop**: Using invariant `J`: WP(while t do e,Q)≡∃J.J∧∀xk.((J∧t⇒WP(e,J))∧(J∧¬t⇒Q))WP(\text{while } t \text{ do } e, Q) ≡ \exists J. J \land \forall x_k. \left( (J \land t \Rightarrow WP(e, J)) \land (J \land \neg t \Rightarrow Q) \right)WP(while t do e,Q)≡∃J.J∧∀xk​.((J∧t⇒WP(e,J))∧(J∧¬t⇒Q))
    - **Example of WP Calculation**:
        - For assignment `x := y;` with `Q = (x > 0)`, the weakest precondition is `P ≡ (y > 0)`.

### 4. **Example Application: Russian Peasant Multiplication**

- **Program**:

		let ref p = a in 
		let ref q = b in 
		let ref r = 0 in 
		while q > 0 invariant J[p, q, r] do 
			if odd(q) then r := r + p; 
			p := p + p; 
			q := q / 2; 
		done;
		
- **Goal**: Prove that the program computes `r = a * b`.
- **Constructing the Invariant `J[p, q, r]`**:
    - **Invariant**: `r + p * q == a * b`
        - **Explanation**: The invariant represents the partial product of `a` and `b` in terms of the updated values `p`, `q`, and `r`.
    - **Proof**:
        1. **Initialization**: Before the loop, `p = a`, `q = b`, and `r = 0`, so `J[p, q, r]` holds as `a * b == r + p * q`.
        2. **Loop Body**:
            - If `q` is odd, `r := r + p` adjusts `r` to account for one instance of `p`.
            - Update `p` and halve `q`, keeping `r + p * q == a * b` intact.
        3. **Termination**: When `q = 0`, `r = a * b`, fulfilling the specification.
### 5. **Practical Verification with Weakest Precondition (WP) Calculus**

- **Example**:
    - Program `P`:

		`if (x > y) then z := x; else z := y;`
- **Postcondition**: `z == max(x, y)`
- **WP Calculation**:
    - If `x > y`, then the postcondition implies `z := x` is correct, so `WP(if x > y then z := x else z := y, z == max(x, y))` simplifies to: 
    - (x>y⇒z==x)∧(¬(x>y)⇒z==y)(x > y \Rightarrow z == x) \land (\neg(x > y) \Rightarrow z == y)(x>y⇒z==x)∧(¬(x>y)⇒z==y)
    - **Verification**: Ensures correctness by proving that `z` holds the maximum of `x` and `y`.


## Lecture - 6:

### 1. **Loop Invariants and Verification**

- **Loop Invariants**: Conditions that hold before and after each iteration of a loop, and help in proving correctness.
    
    - **Proof Structure**:
        1. **Initialization**: The invariant holds true initially.
        2. **Maintenance**: If the invariant is true before an iteration, it remains true after.
        3. **Termination**: When the loop ends, the invariant provides useful properties for the postcondition.
- **Example**: Finding the Maximum Element in an Array
    
    - **Method**: `MaxArray`
    - **Loop Invariants**:
        - `1 ≤ i ≤ a.Length` — ensures `i` stays within bounds.
        - `∀ k: 0 ≤ k < i ⇒ a[k] ≤ m` — maintains that `m` is the max of elements scanned so far.
    - **Proof of Termination**: `i` increases each iteration until it reaches `a.Length`, proving the loop terminates.

### 2. **Binary Search Proof with Loop Invariants**

- **Goal**: Verify that `BinarySearch` correctly finds a target element or confirms its absence.
- **Invariants**:
    - `0 ≤ low ≤ high ≤ n` — bounds for `low` and `high`.
    - `∀ i: (0 ≤ i < low ∨ high ≤ i < n) ⇒ a[i] ≠ value` — ensures value is either found or not present in scanned range.
- **Termination**:
    - Loop decreases `high - low` each time, thus guaranteeing termination.
- **Edge Case**: Overflow in `(high + low) / 2` addressed with `low + (high - low) / 2`.

### 3. **Fast Exponentiation**

- **Objective**: Compute xnx^nxn with fewer multiplications using repeated squaring.
- **Key Properties**:
    - **Odd `n`**: xn=x⋅(x2)(n−1)/2x^n = x \cdot (x^2)^{(n-1)/2}xn=x⋅(x2)(n−1)/2
    - **Even `n`**: xn=(x2)n/2x^n = (x^2)^{n/2}xn=(x2)n/2
- **Loop Invariant for `FastExp`**:
    - `r * exp(c, i) == exp(x, n)` — ensures `r` holds intermediate result.
    - **Auxiliary Lemma**:
        - Used to establish the properties for odd/even `n`.
        - **Proof**: Inductive proof with lemma for odd/even cases ensures that invariant holds for each iteration.

### 4. **McCarthy 91 Function Proof**

- **Definition**: M(n)={n−10if n>100M(M(n+11))if n≤100M(n) = \begin{cases} n - 10 & \text{if } n > 100 \\ M(M(n + 11)) & \text{if } n \leq 100 \end{cases}M(n)={n−10M(M(n+11))​if n>100if n≤100​
- **Key Properties**:
    - For n≤100n \leq 100n≤100, M(n)=91M(n) = 91M(n)=91.
    - For n>100n > 100n>100, M(n)=n−10M(n) = n - 10M(n)=n−10.
- **Termination**:
    - **Proof**: `decreases 101 - n`, ensuring the function reaches M(91)M(91)M(91) through recursive calls until it stabilizes.

### 5. **Sorting and Verification of Selection Sort**

- **Selection Sort Verification**:
    - **Loop Invariants** for `selectionSort`:
        - `sorted(a, i)` — array is sorted up to index `i`.
        - `partitioned(a, i, a.Length)` — elements are correctly partitioned.
    - **Specification Enhancement**:
        - Initially, sorting correctness was verified, but this allowed for trivial solutions.
        - Enhanced specification includes permutation checks using `multiset`:
            - **Ensures**: Final array is a sorted permutation of the initial array.
    - **Proof**: Uses ghost variables to maintain `multiset(a[..]) == multiset(old(a[..]))`, guaranteeing elements are unchanged in value but rearranged in order.

### 6. **Handling Bounded Integer Overflow in Verification**

- **Problem**: Binary search and arithmetic operations (e.g., `(high + low) / 2`) can overflow with bounded integers.
- **Verification Solution for Overflow**:
    - **Method Replacement**: Replace operations with bounded integer checks:
        - Example: `int32_add` function ensures result stays within range.
        - Alternative: **Refined Types** such as `int32` in Dafny with constraints.
    - **Example**:
	    - `newtype int32 = x : int | -2_147_483_648 ≤ x ≤ 2_147_483_647`
- **Binary Search Fix**:
	- Avoids overflow by computing `mid` as `low + (high - low) / 2`, ensuring no wrap-around at upper limits.


## Lecture - 7:

#### 1. **Abstract Data Types (ADTs) and Verification**

- **Key Proof Requirements**:
    
    - **Representation Invariants**: Invariants ensure that the internal representation (concrete state) of an ADT is consistent with the abstract state.
        - **Proof Structure**: Each method within the ADT must:
            1. Assume the invariant holds at the method's start.
            2. Maintain the invariant by method's end, ensuring state soundness.
    - **Abstraction Function**: Maps each concrete state to an abstract state, guaranteeing that clients can only observe the abstract state.
        - **Proof Structure**:
            1. Show that each method correctly updates the abstract state through changes to the concrete state.
            2. Define an **abstraction mapping** that specifies the abstract state representation and verifies its soundness after each operation.
- **Example**: Verification of a `Bank Account ADT`
    
    - **Invariant**: `bal >= 0`
    - **Proof for `withdraw` Method**:
        - **Precondition**: `0 ≤ v ≤ getBal()`
        - **Postcondition**: `bal >= 0` (ensures that balance cannot be negative)
        - **Verification**: Check that any call to `withdraw` respects these preconditions and postconditions:



## Lecture - 8: 
#### 1. **Hoare Logic and Frame Rule**

- **Derived Frame Rule**:
    - Captures the concept of limiting proofs to only those state elements modified by an operation.
    - Frame rule expression: {A}  e  {B}⇒{A∧C}  e  {B∧C}if M(e)∩V(C)=∅\{A\} \; e \; \{B\} \Rightarrow \{A \land C\} \; e \; \{B \land C\} \quad \text{if } M(e) \cap V(C) = \emptyset{A}e{B}⇒{A∧C}e{B∧C}if M(e)∩V(C)=∅
        - M(e)M(e)M(e): Variables modified by `e`.
        - V(C)V(C)V(C): Variables mentioned in `C`.
    - **Example Proof**: `y := x` when `{x > 0} y := x {y > 0 ∧ x = y}`
        - Expanded with additional state `{x > 0 ∧ w < 0} y := x {y > 0 ∧ x = y ∧ w < 0}`, demonstrating that `w` remains unaffected.

#### 2. **Dynamic Frames and ADT Verification**

- **Dynamic Frames**:
    - Extends the Frame Rule by representing which parts of memory (objects) are affected dynamically.
    - **Ghost Set `Repr`**: Captures the set of objects relevant to the memory representation of an ADT.
        - **Verification Goal**: Prove that any modifications adhere to `Repr`, allowing safe encapsulation of dynamic changes.
    - **Example**: `CounterDynamicFrames` Class
        - **Predicate `Valid`**: Ensures `incs` and `decs` are tracked in `Repr`.
        - **Proof Structure**:
            1. Define `Repr` at initialization (`incs`, `decs`, and `this`).
            2. Update `Repr` as necessary in each method while maintaining `Valid`.

#### 3. **Typestates for Protocol Assurance**

- **Typestate**:
    - Represents an ADT’s legal state transitions as formalized pre-/post-conditions.
    - **Verification Strategy**:
        - Methods enforce typestate transitions (e.g., opening, using, and closing a resource).
        - Each method is constrained to ensure that the object state moves from one valid typestate to another without violation.
    - **Example Proof**: `Resource` class with `OpenState` and `ClosedState`
        - **Predicate Definitions**:
            - `OpenState()`: `h != null ∧ size == h.Length`
            - `ClosedState()`: `size == 0`
        - **Verification for `Open` Method**:

			method Open(N : int)
			    modifies Repr
			    requires Valid() && ClosedState() && N > 0
			    ensures Valid() && OpenState() && fresh(Repr - old(Repr))
			{
			    h, size := new int[N], N;
			    Repr := Repr + {h};
			}
			
		- **Proof Strategy**: Ensure method preconditions enforce typestate, moving the resource to a defined open state without accessing closed-only properties.



## Lecture - 9:


## Lecture - 10:

Write Logic in 'Verifast'.

