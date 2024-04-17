import itertools
from istr import istr
print(istr)

for s, e, n, d, m, o, r, y in istr(itertools.permutations("0123456789", 8)):
    if (m > 0) and ((s | e | n | d) + (m | o | r | e) == (m | o | n | e | y)):
        print(f" {s|e|n|d}")
        print(f" {m|o|r|e}")
        print("-----")
        print(m | o | n | e | y)

