import random

def doRandom(t, v):
    match t:
        case 'Choice':
            return randomChoice(v)
        case 'Range':
            return randomRange(v)
        
def randomChoice(v):
    return random.choice(v)
    
def randomRange(v):
    return random.randint(v[0], v[1])    

def handle_escapes(s):
    new_s = ''
    for c in s:
        if c == '\f':
            new_s += '\\f'
        elif c == '\\':
            new_s += '\\'
        elif c == '\'':
            new_s += '\\\''
        elif c == '\n':
            new_s += '\\n'
        elif c == '\r':
            new_s += '\\r'
        elif c == '\t':
            new_s += '\\t'
        elif c == '\b':
            new_s += '\\b'
        else:
            new_s += c

    return new_s

def parse(test):
    type = test.split()[0]
    test = handle_escapes(test)
    match(type):
        case "Choice":
            args = test.split("$")
            args.remove(args[0])
            phrases = []
            for phrase in args:
                newPhrase = '$'+ phrase + '$'
                if phrase != ' ' and phrase != '':
                    phrases.append(newPhrase)
            return(type, phrases, doRandom(type, phrases))

        case "Range":
            args = test.split()
            args.remove(args[0])
            phrases = []
            for phrase in args:
                newPhrase = int(phrase)
                phrases.append(newPhrase)
            return(type, phrases, doRandom(type, phrases))


if __name__ == "__main__":
    tests = ["Choice $x^2 + y^2 = z^2$ $x^3 + y^3 = z^3$ $x^4 + y^4 = z^4$",  
                "Range 5 50",  
                "Choice $3+4$ $5+6$ $7+8$",  
                "Choice $\frac{5\pi}{4}$ $\frac{11\pi}{6}$",  

                "Choice $m^2 - n^2 = p^2$ $2mn = q^2$ $m^2 + n^2 = r^2$",  
                "Range 10 100",  
                "Choice $4+5$ $6+7$ $8+9$",  
                "Choice $\frac{2\pi}{3}$ $\frac{5\pi}{6}$",  

                "Choice $\sqrt{a} + \sqrt{b} = \sqrt{c}$ $\sqrt{x} - \sqrt{y} = \sqrt{z}$",  
                "Range 2 30",  
                "Choice $9+10$ $11+12$",  
                "Choice $\frac{3\pi}{4}$ $\frac{7\pi}{8}$"  
                "Choice $p^3 + q^3 = r^3$ $s^4 + t^4 = u^4$ $v^5 + w^5 = x^5$",  
                "Range 10 200",  
                "Choice $12+13$ $14+15$ $16+17$",  
                "Choice $\frac{11\pi}{8}$ $\frac{13\pi}{9}$",  

                "Choice $a^4 - b^4 = c^4$ $d^5 - e^5 = f^5$ $g^6 - h^6 = i^6$",  
                "Range 1 50",  
                "Choice $18+19$ $20+21$ $22+23$",  
                "Choice $\frac{4\pi}{7}$ $\frac{5\pi}{9}$",  

                "Choice $\log_a b + \log_a c = \log_a d$ $\log_x y - \log_x z = \log_x w$",  
                "Range 5 100",  
                "Choice $24+25$ $26+27$",  
                "Choice $\frac{9\pi}{10}$ $\frac{11\pi}{12}$",  

                "Choice $\sin A + \cos B = \tan C$ $\sec D - \csc E = \cot F$",  
                "Range 2 40",  
                "Choice $28+29$ $30+31$",  
                "Choice $\frac{6\pi}{5}$ $\frac{8\pi}{7}$",  

                "Choice $\frac{1}{a} + \frac{1}{b} = \frac{1}{c}$ $\frac{1}{x} - \frac{1}{y} = \frac{1}{z}$",  
                "Range 3 75",  
                "Choice $32+33$ $34+35$",  
                "Choice $\frac{13\pi}{14}$ $\frac{15\pi}{16}$"  
            ]

    for test in tests:
        type, phrases, rand = parse(test)
        print("Type:", type)
        print("Args:", phrases)
        print("Random: ", doRandom(type, phrases), '\n')
