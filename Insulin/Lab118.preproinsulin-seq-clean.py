import re

print(re.sub(r"(ORIGIN|\s+|\d+/)", "", "   \n         malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed\n        lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn\n"))


import re

with open("new_file.txt", "w") as f:
    f.write(re.sub(r"(ORIGIN|\s+|\d+/)", "", "   \n        malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed\n        lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn\n"))