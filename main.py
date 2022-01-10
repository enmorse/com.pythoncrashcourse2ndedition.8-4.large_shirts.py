# Modify the make_shirt function so that shirts are
# large by default with a message that reads "I love
# Python". Make a large shirt and a medium shirt
# with the default message, and a shirt of any size
# with a different message.

def make_shirt(size="l", msg="\"i love python\""):
    print(f"\nThe size of the shirt is {size.title()} and the "
          f"message printed on the shirt is {msg.title()}.")


make_shirt()
make_shirt("m")
make_shirt(size="xl", msg="\"nothing but the glove\"")
