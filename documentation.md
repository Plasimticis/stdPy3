# Documentation for stdPy3
The below is a example code of the function `getchar()`

```py
from stdpyt import *
data = getchar() # this will call the getchar() function from stdpyt and return the character it got.
print(data) # and than we will print it.
```

Let's take a look at the getchar().
(viewing: src/stdpyt.py)
```py
import msvcrt as msc

def getchar(capital: bool=False) -> str:
    '''
    Gets input of '1' character.
    Parameters:
    capital (bool): default is set to false | makes the entire character a uppercase character.
    Returns:
    str: the character the user pressed, it will return nothing (a empty string) if the character isnt in the alphabet or isnt a number.
    '''
    try:
        if not capital:
            l = msc.getch()
            l = l.decode()
            return l
        else:
            l = msc.getch()
            l = l.decode()
            l = l.upper()
            return l
    except:
        return ""
```

That's self-explanatory.
But yes, it is a little-bit easier than msvcrt.