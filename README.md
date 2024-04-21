# String Permutations

### The Problem

Given a word, print all permutations of all its letters.
For example, for the word: `ABC`, you should print:

```
A
B
C
AB
AC
BA
BC
CA
CB
ABC
ACB
BCA
BAC
CAB
CBA
```

### Considerations

It is unclear whether the order of output values in the example statement is essential. The order is alphabetical, with string length being the secondary sorting criterion. Assuming this is the sorting criteria, the outputs `"BCA"` and `"BAC"` have their positions swapped. I have made this assumption and used the sorted function in Python to sort by string length `(key=length)`.

The statement does not clarify whether duplicate items are allowed, such as when the string is "AA", which would generate the items: `"A"`, `"A"`, `"AA"`, and `"AA"`. Therefore, I have assumed the behavior of `itertools.permutations` function.

I have changed the function's return from None to a list of strings to enable testing.

I have used the Hypothesis library in Python to create property tests.

Due to the solution's asymptotic complexity, some tests had to be limited in the number of results given by the solution. For instance, generating permutations of strings with a maximum length of 8 characters.

If you would like to test with examples of strings with larger sizes, you will need to adjust the configuration of the Hypothesis by increasing its maximum execution time for the desired test. You can do this by specifying `@settings(deadline=X)`, where `X` is a number greater than 200 (default value).
