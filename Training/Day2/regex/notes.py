"""

regular expressions

.     -> any one character (except \n)
?     -> zero or one (quantifier)
+     -> one or more (quantifier)
*     -> zero or more (quantifier)
^     -> at the begining
$     -> at the end of the string
[abc] -> any one of a,b,c
(abc) -> group of abc
{m}   -> 'm' times (quantifier)
{m,n} -> atleast m time and atmost n times. (quantifier)
|     -> or
\     -> escapesequence character
\s    -> a space
\d    -> a digit character. -> [0-9]
\w    -> a word character. -> [a-zA-Z0-9_]
\b    -> a word boundary.

note:quantifier applies to the character before.
------------------------------------------------

\d+\s[a-zK-U3024]{3,5}
"""
