# Recursive Descent Parser for arithmetic expressions

## Formal Explanation

### Grammar:
$expression  \rightarrow expression + term ~ | ~ term - expression ~ | ~ term$ <br />
$term \rightarrow factor \times term ~ | ~ factor / term ~ | ~ factor$ <br />
$factor \rightarrow ( expression ) ~ | ~ number$ <br />

### Problems that prevent the use of recursive descent parsing:

The most significant issue with recursive descent parsers is their inability to handle left-recursive productions. A grammar is said to be left-recursive if it has a non-terminal symbol that can eventually derive itself in one or more steps in such a way that the recursive derivation appears as the leftmost symbol in a sequence. Essentially, a rule in the grammar is left-recursive if it can be rewritten (through one or more substitutions) to begin with itself. <br />

Example: $A \Rightarrow A\alpha$ <br />
This is a problem because the parser will read the production rule $A$ infinitely and never end. <br />

#### Left factorization:

A method to remove left recursion <br />
$E \rightarrow TE'$ <br />
$E' \rightarrow +TE' ~ | ~ -TE' ~ | ~ \epsilon$ <br />
$T \rightarrow FT'$ <br />
$T' \rightarrow *FT' ~ | ~ /FT' ~ | ~ \epsilon$ <br />
$F \rightarrow (E) ~ | ~ num$ <br />

