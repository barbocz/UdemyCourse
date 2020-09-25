import re


def find_all(string):
    worker_string=string.upper()
    vowel={'A', 'E', 'I', 'O', 'U'}
    consonants={'Q', 'W', 'R', 'T', 'Y', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'}
    open_separators= ()
    for ci in consonants:
        for vi in vowel:
            open_separators+=(ci+vi,)

    close_separators= ()
    for vi in vowel:
        for ci in consonants:
            close_separators+=(vi+ci,)

    for sep in open_separators:
        matches=re.finditer(sep,worker_string)
        for match in matches:
            pattern=worker_string[match.start():]

            # print("PATTERN "+pattern)
            for close_sep in close_separators:
                if (pattern.rfind(close_sep)>-1):
                    sub_pattern=pattern[1:pattern.rfind(close_sep)+1];
                    consist_cons=False
                    for ci in consonants:
                        if (sub_pattern.rfind(ci)>-1):
                            consist_cons = True
                            break
                    if (not consist_cons and len(pattern[1:pattern.rfind(close_sep)+1])>1):
                        # print("SUB PATTERN " + pattern[1:pattern.rfind(close_sep)+1])
                        l=len(pattern[1:pattern.rfind(close_sep)+1])
                        print(string[match.start()+1:match.start()+1+l])




# s=input()
s="rabcdeefgyYhFjkIoomnpOeorteeeeet"
find_all(s)

