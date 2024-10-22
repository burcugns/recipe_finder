import requests  # Import the requests library to make HTTP requests


def main():
    pagination_start = 0  # pagination-start index (default is 0)
    pagination_end = 10  # pagination-end index (default is 10)

    ingredient = get_ingredient_from_user()  # Get ingredient from user input

    filters_str = get_filter_parameters()  # Get filter parameters from user input
    #9
    show_more_recipes = 'yes'  # controls the show more recipes
    with open('recipes.txt', 'w') as f:  # Open a file to write the recipes
        while show_more_recipes == 'yes':  # Continue looping while user wants more recipes
            # fetch data from the API based on ingredient, filters, and pagination
            api_response = get_data_by_ingredient_and_filters_from_api(ingredient, filters_str, pagination_start,
                                                                       pagination_end)
            recipes = find_all_recipes(api_response)  # Recipes from the API response

            #7) Print and write each recipe's label and URL
            for recipe in recipes:
                line_seperator()
                print(recipe['label'])  # Print recipe label
                print(recipe['url'])  # Print recipe URL
                f.write(recipe['label'] + '\n')  # Write recipe label to recipes.txt
                f.write(recipe['url'] + '\n')  # Write recipe URL to recipes.txt

            # 8) Check if there are more recipes to bring
            if pagination_end + 1 < int(api_response['count']):
                show_more_recipes = input(
                    "Do you want more recipes? Yes/No: ").lower()  # Ask user if they want more recipes
                pagination_start = pagination_start + 10  # Update pagination-start index
                pagination_end = pagination_end + 10  # Update pagination-end index
            else:
                show_more_recipes = 'no'  # No more recipes to bring
    f.close()  # Close the file


# 1) Ask the user to enter an ingredient that they want to search for
def get_ingredient_from_user():
    ingredient = input("Please enter ingredient you would like to search for: ").lower()  # Get ingredient from user
    while ingredient == "" or ingredient.isspace():  # if user enter empty or space /ask again to user
        ingredient = input("Invalid response. Please try again: ").lower()
    return ingredient  # Return user's  ingredient choice


# 3) Get filter parameters from user
def get_filter_parameters():
    filters_str = ''  # filter string to be used in the API call(default is empty)

    want_cuisine_filter = want_to_filter_by_cuisine()  # Ask user if user wants to filter by cuisine
    if want_cuisine_filter is True:
        cuisines = ["American", "Asian", "British", "Caribbean", "Chinese", "French", "Indian", "Italian", "Japanese",
                    "Kosher", "Mediterranean", "Mexican", "Nordic"]
        selected_cuisine = ask_user_for_which_cuisine(cuisines)  # get user cuisine choice
        filters_str = filters_str + '&cuisineType=' + selected_cuisine  # Add cuisineType filter to the filters_str

    want_meal_filter = want_to_filter_by_meal()  #Ask user if user wants to filter by meal
    if want_meal_filter is True:
        meals = ["Breakfast", "Dinner", "Lunch", "Snack", "Teatime"]
        selected_meal = ask_user_for_which_meal(meals)  # Ask user for specific meal type
        filters_str = filters_str + '&mealType=' + selected_meal  # Add mealType filter to the filters_str

    want_dish_filter = want_to_filter_by_dish()  # Ask user if user wants to filter by dish
    if want_dish_filter is True:
        dishes = ["Main course", "Side dish", "Soup", "Starter", "Desserts"]
        selected_dish = ask_user_for_which_dish(dishes)  # Ask user for specific dish type
        filters_str = filters_str + '&dishType=' + selected_dish  # Add dishType filter to the filters_str

    return filters_str  # Return the combined filters


# 5) Create a function that makes a request to the Edamam API with the required ingredient
def get_data_by_ingredient_and_filters_from_api(ingredient, filters_str, pagination_start, pagination_end):
    app_id = ''  # API app ID
    app_key = ''  # API app key
    # set the API URL with parameters
    result = requests.get(
        f'https://api.edamam.com/search?q={ingredient}{filters_str}&app_id={app_id}&app_key={app_key}&from={pagination_start}&to={pagination_end}')

    if result.status_code == 200:  # HTTP successfully connected
        line_seperator()
        print("Your request was successful")  # Print success message
    else:
        line_seperator()
        print("Error: " + str(result))  # Print error message

    return result.json()  # Return API response in json format


# 6) Get all the returned recipes from the API response for entered ingredient
def find_all_recipes(response):
    hits = (response['hits'])  # hits from API response
    all_recipes = []  # list to store recipes
    for hit in hits:
        all_recipes.append(hit['recipe'])  # Append each recipe to the list
    return all_recipes  # Return the list of recipes


#2) Give user the option to filter by cuisine
def want_to_filter_by_cuisine():
    line_seperator()
    cuisine_y_n = input(
        "Do you want to filter by cuisine? Type 'Yes' for yes or 'No' for no.").lower()  # Ask user if they want to filter by cuisine
    if cuisine_y_n == 'yes':
        return True  # Return True if yes
    else:
        return False  # Return False if no


def want_to_filter_by_meal():
    line_seperator()
    meal_y_n = input(
        "Do you want to filter by meal? Type 'Yes' for yes or 'No' for no.").lower()  # Ask user if they want to filter by meal
    if meal_y_n == 'yes':
        return True  # Return True if yes
    else:
        return False  # Return False if no


def want_to_filter_by_dish():
    line_seperator()
    dish_y_n = input(
        "Do you want to filter by dish? Type 'Yes' for yes or 'No' for no.").lower()  # Ask user if they want to filter by dish
    if dish_y_n == 'yes':
        return True  # Return True if yes
    else:
        return False  # Return False if no


# 4) Ask user for cuisine choice
def ask_user_for_which_cuisine(cuisines):
    return input(
        f"""Please select your preferred cuisine from the following options - \n{cuisines}: """).lower()


def ask_user_for_which_meal(meals):
    return input(
        f"""Please select your preferred meal from the following options - \n{meals}: """).lower()


def ask_user_for_which_dish(dishes):
    return input(
        f"""Please select your preferred dish from the following options - \n{dishes}: """).lower()


def line_seperator():
    print("=" * 120)  # Print a line separator for better readability


main()  # Call the main function to execute the program
