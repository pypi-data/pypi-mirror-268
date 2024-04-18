from fastsnake.application.config import contest_config_filename

import json
import os

def start_contest(
    solutions_namespace: str,
    test_cases_namespace: str, 
    test_generators_namespace: str, 
    contest_id: int, 
    problems: list[str]
) -> None:
    """
    Start a contest at the directory.
    """
    config = {
        "solutions_namespace": solutions_namespace,
        "test_cases_namespace": test_cases_namespace,
        "test_generators_namespace": test_generators_namespace,
        "contest_id": contest_id,
        "problems": problems
    }

    # Create folder with Python modules for writting solutions.
    if not os.path.exists(config["solutions_namespace"]):
        os.mkdir(config["solutions_namespace"])

    for filename in os.listdir(config["solutions_namespace"]):
        os.remove(os.path.join(config["solutions_namespace"], filename))

    for problem in config["problems"]:
        with open(os.path.join(config["solutions_namespace"], problem.upper() + ".py"), "w") as file:
            file.write("# Solution for problem " + problem + "\n\n")

    # Create folder with Python modules for writting test case generators.
    if not os.path.exists(config["test_generators_namespace"]):
        os.mkdir(config["test_generators_namespace"])

    for filename in os.listdir(config["test_generators_namespace"]):
        os.remove(os.path.join(config["test_generators_namespace"], filename))

    for problem in config["problems"]:
        with open(os.path.join(config["test_generators_namespace"], "generator_" + problem.upper() + ".py"), "w") as file:
            file.write("# Test case generator for problem " + problem + ". Modify this file.\n\n")
            file.write("import random\n")
            file.write("import string\n")
            file.write("\n\n")
            file.write("def gen_int(start: int, end: int):\n")
            file.write("    return random.randint(start, end)\n")
            file.write("\n\n")
            file.write("def gen_int_array(size: int, start: int, end: int):\n")
            file.write("    return ' '.join(str(gen_int(start, end)) for _ in range(size))\n")
            file.write("\n\n")
            file.write("def gen_string(size: int, letters: str = string.ascii_lowercase):\n")
            file.write("    return ''.join(random.choice(letters) for _ in range(size))\n")
            file.write("\n\n")
            file.write("def gen_string_array(size: int, start: int, end: int, letters: str = string.ascii_lowercase):\n")
            file.write("    return ' '.join(gen_string(gen_int(start, end), letters) for _ in range(size))\n")
            file.write("\n\n")
            file.write("def generate() -> \"Generator\":  # Yield any data type (it will be converted to str later)\n")
            file.write("    # Sample code ...\n")
            file.write("    yield gen_int(0, 100)\n")
            file.write("    yield gen_int_array(10, 0, 100)\n")
            file.write("    yield gen_string(10, string.ascii_uppercase)\n")
            file.write("    yield gen_string_array(10, 1, 20, string.ascii_uppercase + string.ascii_lowercase)\n")
            file.write("\n\n")
            file.write("def test_output(input_: str, output: str) -> bool:\n")
            file.write("    raise NotImplementedError()")
            file.write("\n")

    # Create config file.
    with open(contest_config_filename, "w") as file:
        file.write(json.dumps(config))