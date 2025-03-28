import random

def doRandom(type, values):
    """
    Selects a random value based on the given type.
    Parameters:
        t (str): The type of problem ("Range" or "Choice").
        v (list or tuple): The values associated with the type.
            - If "Range": A tuple or list with min and max values.
            - If "Choice": A list of possible equations.
    Returns:
        int or str: A random integer (for "Range") or a random equation (for "Choice").
    """
    match type:
        case 'Choice':
            return randomChoice(values)
        case 'Range':
            return randomRange(values)

def randomChoice(values):
    """
    Selects a random equation from a list of equations.
    Parameters:
        v (list): A list of possible equations.
    Returns:
        str: A randomly selected equation from the list.
    """
    return random.choice(values)

def randomRange(values):
    """
    Generates a random value between two integers.
    Parameters:
        v (tuple or list): A pair of integers representing the min and max values.
    Returns:
        int: A random integer between the min and max values (inclusive).
    """
    return random.randint(int(values[0]), int(values[1]))    

def handle_escapes(text):
    """
    Ignores escape cases in a given string.
    Parameters:
        s (str): The string with escape cases to be ignored.
    Returns:
        new_string (str): A new string without escape cases.
    """
    new_string = ''
    for c in text:
        if c == '\f':
            new_string += '\\f'
        elif c == '\\':
            new_string += '\\'
        elif c == '\'':
            new_string += '\\\''
        elif c == '\n':
            new_string += '\\n'
        elif c == '\r':
            new_string += '\\r'
        elif c == '\t':
            new_string += '\\t'
        elif c == '\b':
            new_string += '\\b'
        else:
            new_string += c

    return new_string


def parse(input):
    """
    Parses a string to return the variable type, possible outcomes, and a desired random value.
    Parameters:
        s (str): The initial string to be parsed.
                 Should be structured like "Range min max" or "Choice $equation1$ $equation2$".
    Returns:
        tuple: (type, phrases, random_value)
    """
    type = input.split()[0]
    input = handle_escapes(input)
    match(type):
        case "Choice":
            args = input.split("$")
            args.remove(args[0])
            print(args)
            if args == []:
                raise ValueError(f'Did not include $ with equations')
            equations = []
            for equation in args:
                new_equation = '$'+ equation + '$'
                if equation != ' ' and equation != '':
                    equations.append(new_equation)
            return(type, equations, doRandom(type, equations))

        case "Range":
            args = input.split()
            args.remove(args[0])
            args = [int(x) for x in args]
            return(type, args, doRandom(type, args))
        
        case _:
            raise ValueError(f'Unaccepted Type: {type} (Expected Values: \'Choice\' and \'Range\')')
            