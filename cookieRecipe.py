# 
# Michael Salzarulo
#
# cookie_recipe.py
#
# A formula machine for creating the perfect portion of ingredients based on desired cookies
#
# A cookie recipe calls for the following ingredients:
# • 1.5 cups of sugar
# • 1 cup of butter
# • 2.75 cups of flour
# The recipe produces 48 cookies with this amount of ingredients. Write a program that asks the user how many cookies they want to make and then displays the number of cups of each ingredient needed for the specified number of cookies.
# When the program asks the user for the number of cookies, it should display the following string as a prompt:
# 'Enter number of cookies:'
# When the program displays the number of cups of ingredients, it should display a message in the following format:
# You need x cups of sugar, y cups of butter, and z cups of flour.
# Where x is the number of cups of sugar, y is the number of cups of butter, and z is the number of cups of flour. Don’t worry about formatting the numbers in the output.
# The following sample run shows an example of the program's output. The user's input is shown in bold.
# Sample Run
# Enter number of cookies:48↵
# You need 1.5 cups of sugar, 1.0 cups of butter, and 2.75 cups of flour. 

def main():

    cookies = int(input('Enter number of cookies:'))
    x = cookies * (1.5 / 48)
    y = cookies * (1 / 48)
    z = cookies * (2.75 / 48)
    print('You need ', x, ' cups of sugar, ', y, 'cups of butter, and')
    print(z, ' cups of flour.') 

main()
