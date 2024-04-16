import sys
import subprocess
from pathlib import Path

tests: list[str] = [
    "scripts/aor.mcl",
    "scripts/args.mcl",
    "scripts/array.mcl",
    "scripts/array_and_record.mcl",
    "scripts/artest.mcl",
    "scripts/bleed_test.mcl",
    "scripts/break1.mcl",
    "scripts/break2.mcl",
    "scripts/const.mcl",
    "scripts/continue1.mcl",
    "scripts/continue2.mcl",
    "scripts/csv_test.mcl",
    "scripts/debug.mcl",
    "scripts/demo.mcl",
    "scripts/demo_lib.mcl",
    "scripts/fetest.mcl",
    "scripts/fn_def.mcl",
    "scripts/fnfnt.mcl",
    "scripts/foreach1.mcl",
    "scripts/foreach2.mcl",
    "scripts/foreach3.mcl",
    "scripts/function.mcl",
    "scripts/function2.mcl",
    "scripts/function3.mcl",
    "scripts/function4.mcl",
    "scripts/function5.mcl",
    "scripts/function6.mcl",
    "scripts/function7.mcl",
    "scripts/functions.mcl",
    "scripts/functions2.mcl",
    "scripts/glob_tests.mcl",
    "scripts/halt.mcl",
    "scripts/halt_test.mcl",
    "scripts/hello_world.mcl",
    "scripts/helloworld.mcl",
    "scripts/if.mcl",
    "scripts/if2.mcl",
    "scripts/if3.mcl",
    "scripts/if4.mcl",
    "scripts/if5.mcl",
    "scripts/if6.mcl",
    "scripts/iftest.mcl",
    "scripts/include_1.mcl",
    "scripts/include_2.mcl",
    "scripts/index_7.mcl",
    "scripts/indexed_1.mcl",
    "scripts/indexed_2.mcl",
    "scripts/indexed_3.mcl",
    "scripts/indexed_4.mcl",
    "scripts/indexed_5.mcl",
    "scripts/indexed_6.mcl",
    "scripts/indexed_type.mcl",
    "scripts/interpolation.mcl",
    "scripts/interpolation_shorts.mcl",
    "scripts/io_test.mcl",
    "scripts/lextest.mcl",
    "scripts/libvar.mcl",
    "scripts/m3.mcl",
    "scripts/m4.mcl",
    "scripts/meraki_device_info.mcl",
    "scripts/nested.mcl",
    "scripts/none_test.mcl",
    "scripts/null.mcl",
    "scripts/return.mcl",
    "scripts/select.mcl",
    "scripts/select1.mcl",
    "scripts/select2.mcl",
    "scripts/select3.mcl",
    "scripts/select4.mcl",
    "scripts/select5.mcl",
    "scripts/select6.mcl",
    "scripts/select7.mcl",
    "scripts/select8.mcl",
    "scripts/select_1.mcl",
    "scripts/select_2.mcl",
    "scripts/select_3.mcl",
    "scripts/select_4.mcl",
    "scripts/select_5.mcl",
    "scripts/select_6.mcl",
    "scripts/select_7.mcl",
    "scripts/select_8.mcl",
    "scripts/select_9.mcl",
    "scripts/select_a.mcl",
    "scripts/select_b.mcl",
    "scripts/select_bld.mcl",
    "scripts/select_c.mcl",
    "scripts/select_d.mcl",
    "scripts/select_e.mcl",
    "scripts/string_interpolation.mcl",
    "scripts/string_interpolation2.mcl",
    "scripts/strings_test.mcl",
    "scripts/switch_1.mcl",
    "scripts/system_test.mcl",
    "scripts/test.mcl",
    "scripts/test2.mcl",
    "scripts/test3.mcl",
    "scripts/test4.mcl",
    "scripts/time_test.mcl",
    "scripts/usereserved.mcl",
    "scripts/var_not_found_test.mcl",
    "scripts/variable.mcl",
    "scripts/variables.mcl",
    "scripts/vt.mcl",
    "scripts/while.mcl",
    "scripts/whiletest.mcl",
]

APPROVED_TESTS_FILENAME = "tests_approved.txt"
ERRORED_TESTS_FILENAME = "tests_errored.txt"


def load_approved_tests() -> list[str]:
    approved: list[str] = []
    if not Path.exists(Path(APPROVED_TESTS_FILENAME)):
        return approved
    with open(APPROVED_TESTS_FILENAME, "r") as f:
        approved = f.readlines()
    return approved


def save_approved_test(script: str) -> None:
    approved = load_approved_tests()
    with open("tests_approved.txt", "a") as f:
        f.write(f"{script}\n")


def is_in_approved(script: str) -> bool:
    approved = load_approved_tests()
    for a in approved:
        if a.strip() == script.strip():
            return True
    return False


def is_in_errorred(script: str) -> bool:
    errored = load_errored_tests()
    for e in errored:
        if e.strip() == script.strip():
            return True
    return False


def reset() -> None:
    with open(APPROVED_TESTS_FILENAME, "w") as f:
        f.write("")
    with open(ERRORED_TESTS_FILENAME, "w") as f:
        f.write("")


def load_errored_tests() -> list[str]:
    errored: list[str] = []
    if not Path.exists(Path(ERRORED_TESTS_FILENAME)):
        return errored
    with open(ERRORED_TESTS_FILENAME, "r") as f:
        errored = f.readlines()
    return errored


def remove_errored_test(script: str) -> None:
    errored: list[str] = load_errored_tests()
    with open(ERRORED_TESTS_FILENAME, "x") as f:
        for t in errored:
            if t != script:
                f.write(t)
                f.write("\n")


def save_errored_test(script: str) -> None:
    if is_in_errorred(script) is True:
        return
    with open(ERRORED_TESTS_FILENAME, "a") as f:
        f.write(f"{script}\n")


def clear_screen() -> None:
    # clear screen
    command = ["clear"]
    subprocess.run(command, shell=False)


def run_test(tscript: str) -> None:
    command = [
        "mrun",
        "--lib",
        "./lib",
        "-s",
        f"{tscript}",
    ]
    print()
    print("executing test: ", " ".join(command))
    print()
    subprocess.run(command, shell=False)
    print()
    print("ran test")


def user_input(script: str) -> None:
    print()
    app = input("Ran correctly (y/n?) (reset = r, quit = q) > ")
    if app == "y":
        save_approved_test(script)
        errored = load_errored_tests()
        if script in errored:
            remove_errored_test(script)
    if app == "n":
        save_errored_test(script)
    if app == "r":
        reset()
        sys.exit(0)
    if app == "q":
        sys.exit(0)


def run() -> None:
    approved = load_approved_tests()
    print("Approved tests: ", len(approved))
    for tscript in tests:
        if is_in_approved(tscript) is True:
            continue
        clear_screen()
        run_test(tscript)
        user_input(tscript)


if __name__ == "__main__":
    run()
