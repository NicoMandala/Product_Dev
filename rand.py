import string

# List of cocktail names
cocktails = [
    "Hawaiian Cocktail", "A.D.M. (After Dinner Mint)", "Wine Cooler", "Midnight Cowboy", 
    "Castillian Hot Chocolate", "Swedish Coffee", "Valencia Cocktail", "Tequila Slammer", 
    "Kiwi Papaya Smoothie", "Kill the cold Smoothie", "Acapulco", "Gin Rickey", 
    "Chocolate Beverage", "Aquamarine", "Balmoral", "Midnight Cowboy", 
    "Quaker's Cocktail", "Lemon Elderflower Spritzer", "Almeria", "Old Fashioned", 
    "A Furlong Too Late", "Manhattan", "Queen Bee", "Orgasm", "Pink Panty Pulldowns", 
    "Lassi Raita", "Afternoon", "Japanese Fizz", "Big Red", "Mother's Milk", 
    "Dark and Stormy", "Iced Coffee Fillip", "Bruised Heart", "Vodka Fizz", 
    "Kioki Coffee", "Blue Lagoon", "Tennesee Mud", "Artillery", "Orange Crush", 
    "Aviation", "Bahama Mama", "Russian Spring Punch", "Homemade Kahlua", "Jelly Bean", 
    "Thai Iced Tea", "Ruby Tuesday", "Cream Soda", "Alabama Slammer", "Vesper", 
    "Grand Blue", "Happy Skipper", "Jamaican Coffee", "Irish Russian", "Paradise", 
    "Zippy's Revenge", "Cherry Electric Lemonade", "Irish Spring", "Old Fashioned", 
    "Jackhammer", "Orangeade", "Sol Y Sombra", "Planter's Punch", "Alabama Slammer", 
    "Frosé", "Whisky Mac", "Amaretto Stone Sour", "Frosé", "Balmoral", 
    "Lone Tree Cooler", "Auburn Headbanger", "Spritz Veneziano", "Smut", "Godmother", 
    "Auburn Headbanger", "Frozen Pineapple Daiquiri", "Port And Starboard", 
    "Tequila Sour", "Oreo Mudslide", "Fuzzy Asshole", "Sangria The Best", 
    "Tequila Sour", "Vodka Fizz", "Bobby Burns Cocktail", "Death in the Afternoon", 
    "Iced Coffee Fillip", "Veteran", "Thai Iced Tea", "Texas Rattlesnake", 
    "Salted Toffee Martini", "Space Odyssey", "Pineapple Paloma", "Miami Vice", 
    "9 1/2 Weeks", "Avalon", "Abbey Cocktail", "The Philosopher", 
    "A.D.M. (After Dinner Mint)", "Vampiro", "Turf Cocktail"
]


cocktails_extended = [
    "Artillery Punch", "Mauresque", "Brainteaser", "The Jimmy Conway", "Loch Lomond", 
    "Lone Tree Cooler", "Ice Pick", "Irish Cream", "Apello", "GG", "Casa Blanca", 
    "Margarita", "Daiquiri", "Vodka Fizz", "White Wine Sangria", "Chocolate Black Russian", 
    "Karsk", "Alice in Wonderland", "Allegheny", "24k nightmare", 
    "Empellón Cocina's Fat-Washed Mezcal", "Cherry Electric Lemonade", "Old Cuban", 
    "Yellow Bird", "Applejack", "A. J.", "Mimosa", "Paradise", "Bermuda Highball", 
    "Coffee Liqueur", "Artillery", "Rum Punch", "Tequila Sunrise", "Autodafé", 
    "Shanghai Cocktail", "Halloween Punch", "Butter Baby", "Chocolate Milk", 
    "Algonquin", "Paradise", "Freddy Kruger", "Egg-Nog - Classic Cooked", "Stone Sour", 
    "ABC", "Casa Blanca", "Kentucky B And B", "Pink Gin", "Butterfly Effect", 
    "Snakebite and Black", "Yellow Bird", "Cosmopolitan Martini", "Champagne Cocktail", 
    "Strawberry Margarita", "Blueberry Mojito", "Lassi Raita", "Chocolate Monkey", 
    "Lemon Drop", "Fahrenheit 5000", "After Five", "Apple Cider Punch", "Paloma", 
    "Pineapple Paloma", "Sherry Flip", "Raspberry Cooler", "Mocha-Berry", "Downshift", 
    "Frappé", "The Jimmy Conway", "Happy Skipper", "Chocolate Milk", "B-53", 
    "Flander's Flake-Out", "Queen Bee", "Butter Baby", "Monkey Wrench", "Casino", 
    "Hemingway Special", "Spiking coffee", "Blue Hurricane", "Banana Cream Pi", 
    "Amaretto Mist", "Sherry Eggnog", "Bluebird", "151 Florida Bushwacker", 
    "Sidecar Cocktail", "Alice Cocktail", "Tomato Tang", "Cuba Libra", "Hunter's Moon", 
    "Banana Strawberry Shake Daiquiri", "Japanese Fizz", "Blue Hurricane", 
    "Corpse Reviver", "Bluebird", "Black and Brown", "Strawberry Daiquiri", 
    "Apple Karate", "Boston Sour", "Lazy Coconut Paloma", "Amaretto Stinger", 
    "Irish Cream", "Zipperhead", "Jewel Of The Nile", "Blueberry Mojito", "Brigadier", 
    "Apello", "Creme de Menthe", "Nuked Hot Chocolate", "Harvey Wallbanger", 
    "Quentin", "Adam & Eve", "Apple Karate", "Long Island Iced Tea", "Jamaican Coffee", 
    "Fuzzy Asshole", "Banana Cantaloupe Smoothie", "Baby Guinness", "Egg Cream", 
    "Arthur Tompkins"
]


new_cocktails = [
    "Lone Tree Cocktail", "Orange Scented Hot Chocolate", "Tia-Maria", "Margarita", "Martinez Cocktail",
    "Masala Chai", "Blue Mountain", "Chocolate Milk", "John Collins", "A Piece of Ass", "Gin Lemon",
    "National Aquarium", "Slippery Nipple", "Thai Iced Coffee", "Chocolate Black Russian", "Arctic Fish",
    "Hawaiian Cocktail", "Apello", "White Russian", "Lemouroudji", "After Dinner Cocktail", "Orange Crush",
    "A1", "Hemingway Special", "Dragonfly", "Ipamena", "Apello", "Casino", "Alexander", 
    "Scottish Highland Liqueur", "155 Belmont", "Zorro", "Corn n Oil", "Pina Colada", "ACID", 
    "Imperial Fizz", "Planter's Punch", "Microwave Hot Cocoa", "Chocolate Milk", "Tuxedo Cocktail", 
    "Sidecar", "After sex", "The Galah", "Port And Starboard", "Gluehwein", "A midsummernight dream", 
    "Paradise", "Rosemary Blue", "Amaretto Mist", "Oatmeal Cookie", "151 Florida Bushwacker", "Bijou", 
    "Kurant Tea", "Pina Colada", "Planter’s Punch", "Imperial Cocktail", "Lemouroudji", "Buccaneer", 
    "Whiskey Sour", "Figgy Thyme", "Tequila Sunrise", "Apricot Lady", "Gagliardo", "Egg Nog #4", 
    "Chocolate Drink", "Black Russian", "Orangeade", "The Strange Weaver", "Lady Love Fizz", 
    "Absolutely Fabulous", "Gin Toddy", "Brandy Sour", "Jitterbug", "Shark Attack", "Atlantic Sun", 
    "Bramble", "Zorbatini", "Strawberry Daiquiri", "Absolutely Fabulous", "Martinez Cocktail", 
    "Waikiki Beachcomber", "Lord And Lady", "Shot-gun", "Between The Sheets", "Irish Russian", 
    "California Root Beer", "Campari Beer", "Waikiki Beachcomber", "Alice in Wonderland", 
    "Blue Margarita", "B-52", "Dubonnet Cocktail", "Amaretto fizz", "Bellini Martini", "Cosmopolitan", 
    "After Dinner Cocktail", "Monkey Wrench", "Rum Cooler", "Lord And Lady", "Quaker's Cocktail", 
    "Chocolate Drink", "Shanghai Cocktail", "Blackthorn", "Apple Pie with A Crust", "Shanghai Cocktail", 
    "Flander's Flake-Out", "Blue Mountain", "Ace", "Texas Rattlesnake", "Absinthe #2", "Amaretto Sour", 
    "Gin Squirt", "Arise My Love", "Creme de Menthe", "London Town", "Paloma", "Brandy Cobbler", 
    "Amaretto Sunset", "Arthur Tompkins", "French Martini", "Golden dream", "A. J.", "Happy Skipper", 
    "Old Cuban", "Lemouroudji", "Oreo Mudslide", "Shot-gun", "Ace", "Applecar", "Iced Coffee", 
    "Lemon Shot", "Grizzly Bear", "Egg Nog #4", "Strawberry Margarita", "Midnight Manx", "Slippery Nipple", 
    "Miami Vice", "London Town", "Algonquin", "Lassi - Mango", "Salty Dog", "Masala Chai", 
    "Lone Tree Cooler", "Rail Splitter", "Classic Old-Fashioned", "Mississippi Planters Punch", 
    "Autodafé", "Gin Squirt", "Egg Nog - Healthy"
]

# Extract the first letter of each cocktail name
first_letters = {cocktail[0].upper() for cocktail in new_cocktails}

# Create a set of all letters in the English alphabet
alphabet = set(string.ascii_uppercase)

# Find the difference between the two sets
missing_letters = alphabet - first_letters

# Output the result
print(f"Letters without associated cocktails: {missing_letters}")
print(f"Number of letters without associated cocktails: {len(missing_letters)}")