import json

PERSONAL_FILE = "personal.json"

def load_personalfile():
    try:
        with open(PERSONAL_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_personalfile(personaldata):
    with open(PERSONAL_FILE, "w") as file:
        json.dump(personaldata, file, indent=4)

def add_book(personaldata):
    title = input(" Title: ").strip()
    author = input(" Author: ").strip()
    
    try:
        year = int(input("Publication Year: ").strip())
    except ValueError:
        print("❌ Invalid year! Book not added.")
        return
    
    genre = input(" Genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower()
    read = read_status == "yes"

    personaldata.append({"Title": title, "Author": author, "Year": year, "Genre": genre, "Read": read})
    save_personalfile(personaldata)
    print("✅ Book added successfully!")

def remove_book(personaldata):
    title = input("Title to remove: ").strip()
    for book in personaldata:
        if book["Title"].lower() == title.lower():
            personaldata.remove(book)
            save_personalfile(personaldata)
            print("✅ Book removed!")
            return
    print("Book not found.")

def search_books(personaldata):
    keyword = input("Search by Title or Author: ").strip().lower()
    results = [book for book in personaldata if keyword in book["Title"].lower() or keyword in book["Author"].lower()]
    
    if results:
        print("\n Search Results:")
        for book in results:
            status = "✅ Read" if book["Read"] else "❌ Not Read"
            print(f"- {book['Title']} by {book['Author']} ({book['Year']}, {book['Genre']}) - {status}")
    else:
        print(" No books found.")

def list_books(personaldata):
    if not personaldata:
        print(" No books in the library.")
        return
    
    print("\n Your Library:")
    for book in personaldata:
        status = "✅ Read" if book["Read"] else "❌ Not Read"
        print(f"- {book['Title']} by {book['Author']} ({book['Year']}, {book['Genre']}) - {status}")

def display_statistics(personaldata):
    total_books = len(personaldata)
    if total_books == 0:
        print("  No books in the library.")
        return
    
    read_books = sum(1 for book in personaldata if book["Read"])
    percentage_read = (read_books / total_books) * 100

    print("\n Library Statistics:")
    print(f"  Total books: {total_books}")
    print(f"  Books read: {read_books} ({percentage_read:.2f}% read)")

def main():
    personaldata = load_personalfile()
    while True:
        print("\n PERSONAL LIBRARY MANAGER")
        print("1 Add Book")
        print("2 Remove Book")
        print("3 Search Book")
        print("4 List Books")
        print("5 Display Statistics")
        print("6 Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_book(personaldata)
        elif choice == "2":
            remove_book(personaldata)
        elif choice == "3":
            search_books(personaldata)
        elif choice == "4":
            list_books(personaldata)
        elif choice == "5":
            display_statistics(personaldata)
        elif choice == "6":
            print("Library saved. Exiting...")
            save_personalfile(personaldata)  
            break
        else:
            print("⚠ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

