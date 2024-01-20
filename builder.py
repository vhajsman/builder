import argparse
import json
import os

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
parser.add_argument("--timestamp-format", help="Specify timestamp format", type=str)
parser.add_argument("--timestamp-time", help="Specify timestamp (ignores --timestamp-format)", type=str)
parser.add_argument("-c", help="Use C", action="store_true", default=True)
parser.add_argument("-cpp", help="Use C++", action="store_true", default=False)

args = parser.parse_args()
print(args)


def makeQuery():
    queries = ["", "", "", ""]

    a = "any" if args.arch == None else args.arch
    t = "any" if args.target == None else args.target

    queries[0] = "any-any"
    queries[1] = f"{a}-{t}"
    queries[2] = f"{a}-any"
    queries[3] = f"any-{t}"

    print(queries)
    return queries

queries = makeQuery()

#def makeTimestamp(format: str):
    

def callCompiler(isCpp: bool, file: str, arch: str, target: str, optionalDefs: str, optionalParams: str, prefix: str):
    compiler = {"g++" if isCpp else "gcc"}
    if prefix != None:
        compiler = f"{prefix}-{compiler}"

    command = f"{compiler} {file}"

    # Target and architecture
    command.join(f"-D __ARCH_{arch}_"   if not arch in      ["any", None] else "-D __ARCH_UNKNOWN_ -D __ARCH_x86_")
    command.join(f"-D __TARGET_{arch}_" if not target in    ["any", None] else "_D __TARGET_UNKNOWN_ -D __ARCH_x86_")

def build():
    print("Starting build...")
