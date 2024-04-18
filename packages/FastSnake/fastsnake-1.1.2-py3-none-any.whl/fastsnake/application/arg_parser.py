from argparse import ArgumentParser

main_parser = ArgumentParser(
    prog="FastSnake",
    description="CLI Tools for Competitive Programming",
)

main_parser.add_argument("-c", "compile", type=str, default="main.py", nargs=1, help="Compile a python solution that uses fastsnake")
main_parser.add_argument("-l", "list", help="List algorithm or structure modules")

codeforces_parser = main_parser.add_parser("codeforces", help="Tools for Codeforces")
codeforces_parser.add_argument("-l", "load", type=int, nargs=2, help="Download test cases from a problem")

args = parser.parse_args()
result = args.number * 2
print("Result:", result)