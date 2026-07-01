import datetime
from utils import add, subtract

def main():
    print("My name is Bidhan Chakraborty")
    print("Today's date : ", datetime.date.today())

    # calculator demo
    print("10+5 = ", add(10,5))
    print("10-5 = ", subtract(10,5))
    


if __name__ == "__main__":
    main()