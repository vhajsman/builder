import argparse
import json

ext_c =     ["c"]
ext_cpp =   ["cpp", "cc", "c++"]
ext_asm =   ["asm", "s", "inc"]
ext_head =  ["h", "hpp", "hh", "h++"]
ext_obj =   ["o", "obj", "out"]
ext_bin =   ["exe", "com", "elf", "bin", "hex"]

# --- ARGUMENTS PARSING ---

parser = argparse.ArgumentParser(
    prog = "C/C++ Builder",
    description = "By Vaclav Hajsman (CZ)",
    epilog = "https://github.com/vhajsman/builder"
)

parser.add_argument("--version", action="version")
parser.add_argument("-r", "--run", help="Runs executable automatically if supported.")

parser.add_argument("-s", "--script", help="Builds using a script", type=str)
parser.add_argument("-a", "--arch", help="Specify target architecture (__ARCH_XXX_)", type=str)
parser.add_argument("-t", "--target", help="Specify target machine (__TARGET_XXX_)", type=str)

parser.add_argument("c", help="Use C", action="store_true")
parser.add_argument("cpp", help="Use C++", action="store_true")

args = parser.parse_args()


def makeQuery():
    queries = []

    a = "any" if args.arch == None else parser.arch
    t = "any" if args.target == None else parser.target

    queries[0] = "any-any"
    queries[1] = f"{a}-{t}"
    queries[2] = f"{a}-any"
    queries[3] = f"any-{t}"

    return queries;

queries = makeQuery()

