#[] list
# () Tuples
# {} dict

from Roman import romanToInt
from CommonPrefix import longestCommonPrefix
'''
def main():
    username = input("Enter username:")
    print("Username is: " + username)

    Roman.romanToInt

'''
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



if __name__ == "__main__":
    main()
    commonPrefix()