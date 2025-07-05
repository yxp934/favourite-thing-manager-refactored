import json
import os
import re

def load_favorites(filename="favorites.json"):
    """Load favorites data from file, return default data if file doesn't exist"""
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Cannot read file {filename}, using default data. Error: {e}")
    return {"color": "blue", "food": "pizza", "movie": "Interstellar"}

def save_favorites(favorites, filename="favorites.json"):
    """Save favorites data to file"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(favorites, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"Warning: Cannot save to file {filename}. Error: {e}")

def validate_input(text, max_length=50):
    """Validate input, ensure not empty and reasonable length"""
    if not text or not text.strip():
        return False, "Input cannot be empty"
    if len(text) > max_length:
        return False, f"Input length cannot exceed {max_length} characters"
    # Check for special characters
    if re.search(r'[<>:"|?*]', text):
        return False, "Input cannot contain special characters < > : \" | ? *"
    return True, ""

def display_favorites(favorites):
    """Display all favorites"""
    if not favorites:
        print("\nYou don't have any favorites yet.\n")
        return
    
    print("\nHere are all your favorites:")
    for category, value in favorites.items():
        print(f"{category}: {value}")
    print()

def lookup_favorite(favorites):
    """Look up a specific category favorite"""
    category = input("Enter a category to look up: ").strip()
    
    # Input validation
    is_valid, error_msg = validate_input(category)
    if not is_valid:
        print(f"Error: {error_msg}\n")
        return
    
    if category in favorites:
        print(f"My favorite {category} is {favorites[category]}!\n")
    else:
        print(f"No favorite found for category '{category}'.\n")

def add_favorite(favorites):
    """Add a new favorite"""
    category = input("Enter new category: ").strip()
    
    # Input validation
    is_valid, error_msg = validate_input(category)
    if not is_valid:
        print(f"Error: {error_msg}\n")
        return
    
    if category in favorites:
        print(f"Category '{category}' already exists. Use update instead.\n")
        return
    
    value = input(f"Enter your favorite for {category}: ").strip()
    
    # Input validation
    is_valid, error_msg = validate_input(value)
    if not is_valid:
        print(f"Error: {error_msg}\n")
        return
    
    favorites[category] = value
    print(f"Added favorite: {category}: {value}\n")
    save_favorites(favorites)

def update_favorite(favorites):
    """Update an existing favorite"""
    category = input("Enter category to update: ").strip()
    
    # Input validation
    is_valid, error_msg = validate_input(category)
    if not is_valid:
        print(f"Error: {error_msg}\n")
        return
    
    if category not in favorites:
        print(f"Category '{category}' does not exist. Use add instead.\n")
        return
    
    value = input(f"Enter your new favorite for {category}: ").strip()
    
    # Input validation
    is_valid, error_msg = validate_input(value)
    if not is_valid:
        print(f"Error: {error_msg}\n")
        return
    
    favorites[category] = value
    print(f"Updated favorite: {category}: {value}\n")
    save_favorites(favorites)

def delete_favorite(favorites):
    """Delete a favorite"""
    category = input("Enter category to delete: ").strip()
    
    # Input validation
    is_valid, error_msg = validate_input(category)
    if not is_valid:
        print(f"Error: {error_msg}\n")
        return
    
    if category in favorites:
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete '{category}: {favorites[category]}'? (y/n): ").strip().lower()
        if confirm in ['y', 'yes']:
            del favorites[category]
            print(f"Deleted favorite for category '{category}'.\n")
            save_favorites(favorites)
        else:
            print("Deletion cancelled.\n")
    else:
        print(f"Category '{category}' not found.\n")

def show_help():
    """Show help information"""
    print("\n=== Help Information ===")
    print("lookup - Look up a specific category favorite")
    print("add    - Add a new favorite")
    print("update - Update an existing favorite")
    print("delete - Delete a favorite")
    print("help   - Show this help information")
    print("quit   - Exit the program")
    print("=======================\n")

def main():
    """Main program"""
    favorites = load_favorites()
    print("Available categories: " + ", ".join(favorites.keys()))
    
    while True:
        action = input("What would you like to do? (lookup/add/update/delete/help/quit): ").strip().lower()
        
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
        elif action == "help":
            show_help()
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose lookup/add/update/delete/help/quit.\n")

if __name__ == "__main__":
    main() 