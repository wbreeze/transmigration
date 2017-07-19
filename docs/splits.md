---
---
[back to index](index)
# Splitting passwords

Given a password:

`abcdefghijklmnopqrstuvwxyz`

It is relatively easy to split it in half:

`abcdefghijklm`

`nopqrstuvwxyz`

[The Github project](https://github.com/wbreeze/transmigration)
hosting these documents has two utilities for splitting and joining
a password using every-other character, like a zipper:

* `otro.py` will split a string into two, every-other-character strings

        $ otro.py abcdefghijklmnopqrstuvwxyz
        Given: abcdefghijklmnopqrstuvwxyz
         Even: acegikmoqsuwy
          Odd: bdfhjlnprtvxz

* `intro.py` will join two every-other-character strings into one

        $ intro.py acegikmoqsuwy bdfhjlnprtvxz
          Even: acegikmoqsuwy
           Odd: bdfhjlnprtvxz
        Result: abcdefghijklmnopqrstuvwxyz

(Forget that "even" and "odd" look mixed-up.  It's a counting from zero thing.)
