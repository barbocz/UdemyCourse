import re


def find_all(string):
    worker_string=string.upper()
    found=False
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

    for i in range(0,len(worker_string)):
        if (worker_string[i:i+2] in open_separators):
            print("WORK: "+worker_string[i:i+2])
            pattern=worker_string[i:]
            for close_sep in close_separators:
                if (pattern.rfind(close_sep)>-1):
                    sub_pattern=pattern[1:pattern.rfind(close_sep)+1];
                    print(sub_pattern+" with close sep "+close_sep)
                    consist_cons=False
                    for ci in consonants:
                        if (sub_pattern.rfind(ci)>-1):
                            consist_cons = True
                            break
                    if (not consist_cons and len(pattern[1:pattern.rfind(close_sep)+1])>1):
                        # print("SUB PATTERN " + pattern[1:pattern.rfind(close_sep)+1])
                        l=len(pattern[1:pattern.rfind(close_sep)+1])
                        print(string[i+1:i+1+l])
                        found=True

    if (not found):
        print("-1")
    # for sep in open_separators:
    #     matches=re.finditer(sep,worker_string)
    #     for match in matches:
    #         pattern=worker_string[match.start():]
    #
    #         # print("PATTERN "+pattern)
    #         for close_sep in close_separators:
    #             if (pattern.rfind(close_sep)>-1):
    #                 sub_pattern=pattern[1:pattern.rfind(close_sep)+1];
    #                 consist_cons=False
    #                 for ci in consonants:
    #                     if (sub_pattern.rfind(ci)>-1):
    #                         consist_cons = True
    #                         break
    #                 if (not consist_cons and len(pattern[1:pattern.rfind(close_sep)+1])>1):
    #                     # print("SUB PATTERN " + pattern[1:pattern.rfind(close_sep)+1])
    #                     l=len(pattern[1:pattern.rfind(close_sep)+1])
    #                     print(string[match.start()+1:match.start()+1+l])




# s=input()
# s="rabcdeefgyYhFjkIoomnpOeorteeeeet"
s="abaabaabaabaae"
find_all(s)

