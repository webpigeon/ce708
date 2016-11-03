# Example

## Our setup
```c
char pass[10]; //10 bytes
int auth; //4 bytes
```

In the below diagrams, each column represents 1 byte, the last
4 represent the int "auth" (that will be important later).

## Entering a valid value
When we enter a valid value, our above memory looks like this:

(the entered value is password).

| Byte    | 0   | 1  | 2   | 3   | 4   | 5   | 6   | 7   | 8  | 9 | a0 | a1 | a2 | a3 |
|---------|-----|----|-----|-----|-----|-----|-----|-----|----|---|----|----|----|----|
| Ascii   | p   | a  | s   | s   | w   |  o  | r   | d   | \0 | ? | 0  | 0  | 0  | 0  |
| Decimal | 112 | 97 | 115 | 155 | 119 | 111 | 114 | 100 | 0  | ? | 0  | 0  | 0  | 0  |

ok, great so we can see that worked correctly. The \0 and the end tells
c where the string ends, that's important because it's how c knows where
the string ends (c doens't keep track of how long strings are).

The c if statement checks auth, which is set as the value 0 - this returns false and therefore
you are not logged in.

## Entering a too long value
What happens when we use the ```gets``` function and the user enters
a value that is too long?

(the entered value is password01234)

| Byte    | 0   | 1  | 2   | 3   | 4   | 5   | 6   | 7   | 8  | 9  | a0 | a1 | a2 | a3 |
|---------|-----|----|-----|-----|-----|-----|-----|-----|----|----|----|----|----|----|
| Ascii   | p   | a  | s   | s   | w   |  o  | r   | d   | 0  | 1  | 2  | 3  | 4  | \0 |
| Decimal | 112 | 97 | 115 | 155 | 119 | 111 | 114 | 100 | 48 | 49 | 50 | 51 | 52 | 0  |

Whoops! now the values which should hold the int now contain our
(text) numbers (c would interperate this as a number).

now, if we try to read the int the value we'll get whatever
the int equalivent of the ascii characters: 842216448 (00110010 00110011 00110100 00000000)

The c if statement returns true if the value is non-zero, therefore, our new value
which is not zero evaluates to true and you get 'logged in'.
