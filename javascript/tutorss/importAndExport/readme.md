this is a folder to explain how to reuse other files, by exporting and importing them.

1. export can be used in any type of var, function, OOP. simply put it in before the declaring syntax.
2. import is used in the file that'll reuse the code.
    2.1 import should bring the var by "import { var1, var2 } from ./thisfile" (file handling looks like html, or regular file navigation)
    2.2 to import all the containings, use "import * as 'fancyUtilityName' from ./thisfile": the vars and functions will be stored in a object(after 'as')