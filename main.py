def display_favorites(favorites):
    print("\nHere are all your favorites:")
    for category, value in favorites.items():
        print(f"{category}: {value}")
    print()

def lookup_favorite(favorites):
    category = input("Enter a category to look up: ").strip()
    if category in favorites:
        print(f"My favorite {category} is {favorites[category]}!\n")
    else:
        print(f"No favorite found for category '{category}'.\n")

def add_favorite(favorites):
    category = input("Enter new category: ").strip()
    if category in favorites:
        print(f"Category '{category}' already exists. Use update instead.\n")
        return
    value = input(f"Enter your favorite for {category}: ").strip()
    favorites[category] = value
    print(f"Added favorite: {category}: {value}\n")

def update_favorite(favorites):
    category = input("Enter category to update: ").strip()
    if category not in favorites:
        print(f"Category '{category}' does not exist. Use add instead.\n")
        return
    value = input(f"Enter your new favorite for {category}: ").strip()
    favorites[category] = value
    print(f"Updated favorite: {category}: {value}\n")

def delete_favorite(favorites):
    category = input("Enter category to delete: ").strip()
    if category in favorites:
        del favorites[category]
        print(f"Deleted favorite for category '{category}'.\n")
    else:
        print(f"Category '{category}' not found.\n")

def main():
    favorites = {"color": "blue", "food": "pizza", "movie": "Interstellar"}
    print("Available categories: " + ", ".join(favorites.keys()))
    while True:
        action = input("What would you like to do? (lookup/add/update/delete/quit): ").strip().lower()
        if action == "lookup":
            lookup_favorite(favorites)
        elif action == "add":
            add_favorite(favorites)
            display_favorites(favorites)
        elif action == "update":
            update_favorite(favorites)
            display_favorites(favorites)
        elif action == "delete":
            delete_favorite(favorites)
            display_favorites(favorites)
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose lookup/add/update/delete/quit.\n")

if __name__ == "__main__":
    main() 