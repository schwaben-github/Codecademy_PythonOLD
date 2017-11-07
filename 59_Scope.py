#59. Scope
def test_scope():
    num = 5
    
num = 6
test_scope()

while True:
    answer = raw_input("What number is in num?")
    if answer == str(num):
        print "Yes!"
        break
    else:
        print "Sorry, that's incorrect."
