#!/usr/bin/env python


def run_script(script, stdin=None):
    """Returns (stdout, stderr), raises error on non-zero return code"""
    import subprocess
    proc = subprocess.Popen(['psql', '-d', 'news', '-c', script],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if proc.returncode:
        raise ScriptException(proc.returncode, stdout, stderr, script)
    return stdout, stderr


class ScriptException(Exception):
    def __init__(self, returncode, stdout, stderr, script):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr
        Exception.__init__('Error in script')


def print_menu():
    print(15 * "-" + "Logs Analysis" + 15 * "-")
    print("1. Top 3 articles")
    print("2. Authors ranking")
    print("3. Days of many errors")
    print("4. Print menu again")
    print("5. Exit")
    print(43 * "-")

if __name__ == '__main__':
    loop = True

    print_menu()
    while loop:
        try:
            choice = input("Enter your choice [1-5]: ")
            if choice == 1:
                print("Result of question 1")
                print(run_script("select title, access \
                from articles_ranking limit 3")[0])
            elif choice == 2:
                print("Result of question 2")
                print(run_script("select * \
                from authors_ranking")[0])
            elif choice == 3:
                print("Result of question 3")
                print(run_script("select * \
                from daily_error_rates")[0])
            elif choice == 4:
                print_menu()
            elif choice == 5:
                print("Done")
                loop = False
            else:
                input("Wrong option selection. Enter any key to try again..")
        except NameError as e:
            print(e)
            continue
else:
    print("Unable to be used as imported module.")
