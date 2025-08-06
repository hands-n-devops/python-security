import os

def get_user_input():
    # Command injection vulnerability
    user_input = input("Enter a filename to list: ")
    os.system("ls " + user_input)

def insecure_compare(password, user_input):
    # Insecure comparison (timing attack)
    return password == user_input

def sql_injection(cursor, user_id):
    # SQL injection vulnerability
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    cursor.execute(query)

def main():
    get_user_input()
    # Simulate insecure password check
    print(insecure_compare("secret", input("Password: ")))
    # Simulate SQL injection
    class DummyCursor:
        def execute(self, q): print("Executing:", q)
    sql_injection(DummyCursor(), input("User ID: "))

if __name__ == "__main__":
    main()
 
