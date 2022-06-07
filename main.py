# [] list
# () Tuples
# {} dict

from Roman import romanToInt
from CommonPrefix import longestCommonPrefix
from converters import celsuis
from converters import hours
from validparentheses import isValid



def main():
    romanNumber = input("Enter the Roman Number: ")
    print("Roman Number is: " + romanNumber)
    modified_data = romanToInt(romanNumber)
    print(modified_data)

def commonPrefix():
    input_string = input('Enter elements of a list separated by space ')
    print("\n")
    user_list = input_string.split()
    # print list
    print('list: ', user_list)
    modified_data = longestCommonPrefix(user_list)
    print(modified_data)


def converterscel():
    cel = int(input("Enter the temperature in Celcuis: "))
    print("Temperature in Celcuis is: ", cel)
    farenite = celsuis(cel)
    print("The temperature in farenite is: ", farenite)


def convertershours():
    min = int(input("Enter minutes: "))
    sec = int(input("Enter seconds: "))

    print("Minutes: ", min)
    print("Seconds: ", sec)

    hour = hours(min, sec)
    print("The total hours are: ", hour)


def parentheses():
    para = input("Enter the parentheses string: ")
    print("The paratheses string is: ", para)
    validation = isValid(para)
    print("The parenthese string is:", validation)


if __name__ == "__main__":
    main()
    commonPrefix()
    converterscel()
    convertershours()
    parentheses()
