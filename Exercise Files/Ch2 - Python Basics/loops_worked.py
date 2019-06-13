#
# Example file for working with loops
#

def main():
    x = 0

    # define a while loop
    while x < 5:
        print(x)
        x = x + 1

    # define a for loop
    for i in range(5, 10):
        print(i)

    # use a for loop over a collection
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in days:
        print(day)

    # use the break and continue statements
    for x in range(1,11):
        if x % 2 == 0:
            if x % 3 == 0:
                break
            continue
        print(x)

    # using the enumerate() function to get index
    for i, day in enumerate(days):
        print(i, day, sep=": ")


if __name__ == "__main__":
  main()
