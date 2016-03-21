import random
import sys

random.seed()
if len(sys.argv) > 1:
    an = "NO INFO"
    roll = random.randint(0, 2)
    an = bd[roll]
    if (sys.argv[1] == "1"):
        an = a * c
    if (sys.argv[1] == "0"):
        an = b * c
    print("{} is {}".format(sys.argv[1], an))
else:
    print("NO ARGS")
