recipe_finder


The Recipe Finder is a Python application designed to help users search for recipes based on an ingredient. It fetches data from the Edamam API and allows users to apply filters like cuisine type, meal type, and dish type. The results, including recipe names and URLs, are saved to a text file.

Project Structure

Main Functionalities

Search Recipes: Users input an ingredient, and the app fetches matching recipes.
Filter Options: Users can filter recipes by cuisine type, meal type, or dish type.
Pagination: Recipes are retrieved in batches of 10, and users can choose to load more results.
Save Results: Recipe names and URLs are written to a recipes.txt file.

User Interaction

Ingredient Input: The user is prompted to input an ingredient.
Filter Parameters: The user is prompted for optional filters like:
Cuisine (e.g., American, Asian, Italian)
Meal Type (e.g., Breakfast, Dinner, Snack)
Dish Type (e.g., Main course, Side dish, Dessert)
Load More Recipes: Users can load additional recipes as needed.


API Integration

The project integrates with the Edamam API for recipe data:

API URL: https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}
API Parameters: Includes filters like cuisineType, mealType, dishType, and pagination (from, to).


Functions and Procedures
Main Functions

get_ingredient_from_user: Asks the user for an ingredient and validates input.
get_filter_parameters: Gathers optional filter preferences from the user.
get_data_by_ingredient_and_filters_from_api: Sends an API request based on the provided ingredient and filters.
find_all_recipes: Extracts recipes from the API response.

Helper Functions

want_to_filter_by_cuisine/meal/dish: Prompts the user to filter by cuisine, meal, or dish.
ask_user_for_which_cuisine/meal/dish: Gets the user's specific filter choice.

Files and Output
recipes.txt: Stores the recipe names and URLs retrieved during the search.
Edamam API Credentials: Ensure to add your App ID and App Key to the script before running the program.


Conclusion
This Recipe Finder application provides a user-friendly way to search, filter, and save recipes. It allows seamless integration with the Edamam API, supports pagination, and offers flexible filtering options to help users find exactly what they are looking for.
