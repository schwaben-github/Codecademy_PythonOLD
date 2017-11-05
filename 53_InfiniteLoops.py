#53. Infinite loops
while True:
    age = raw_input("Enter your age: ")
    age.isdigit()
    if not age.isdigit():
        break
