# how2curry

## What is this?
This is a an introduction to the technique of currying in programming. The examples are written in both Python and JavaScript.

## What is currying?
Currying is the technique of breaking down functions that take multiple arguments into functions that take a single argument (monads).

Take the following definition of a function that takes two arguments:

```haskell
f(A, B) → C
```

If we were to curry the above function we would describe it in the following way:

```haskell
f(A) → g(B) → C
```

Where the functions f and g are now monads.
