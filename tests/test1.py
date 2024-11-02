'''
(note)
THIS IS A TEST FILE.
'''
import msvcrt as msc

def getchar(capital: bool=False) -> str:
    '''
    Gets input of '1' (a single character) character.
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

test = getchar(capital=True)
print(test)
test2 = getchar()
print(test2)