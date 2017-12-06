#!/usr/bin/env python
from pprint import pprint

def run_script(script, stdin=None):
    """Returns (stdout, stderr), raises error on non-zero return code"""
    import subprocess
    # Note: by using a list here (['bash', ...]) you avoid quoting issues, as the
    # arguments are passed in exactly this order (spaces, quotes, and newlines won't
    # cause problems):
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
    print(15 * "-" + "Logs Analysis"+ 15 * "-")
    print("1. Top 3 articles")
    print("2. Authors ranking")
    print("3. Days of many errors")
    print("4. Print menu again")
    print("5. Exit")
    print(43 * "-")

loop=True      

print_menu()
while loop:
    try:
        choice = input("Enter your choice [1-5]: ")
        if choice == 1:
            print("Result of question 1")
            ## You can add your code or functions here
            print(run_script("select title, access from articles_ranking limit 3")[0])
        elif choice == 2:
            print("Result of question 2")
            ## You can add your code or functions here
            print(run_script("select * from authors_ranking")[0])
        elif choice == 3:
            print("Result of question 3")
            ## You can add your code or functions here
            print(run_script("select * from daily_error_rates where percentage >= 1.0;")[0])
        elif choice == 4:
            print_menu()
        elif choice == 5:
            print("Done")
            ## You can add your code or functions here
            loop = False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again..")
    except NameError as e:
        print(e)
        continue
