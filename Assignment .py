class Library_management:
    def __init__(self):
        self.books = []
        self.book_set = set()
        self.genre_dict = {}

    def add_to_library(self, title, author, genre):
        book = (title, author, genre)
        if book not in self.book_set:
            self.books.append(book)
            self.book_set.add(book)
            print(f"\nBook '{title}' added to the library.")
        else:
            print(f"Book '{title}' is already in the library.")

    def remove_from_book(self, title):
        for book in self.books:
            if book[0] == title:
                self.books.remove(book)
                self.book_set.remove(book)
                print(f"\nBook '{title}' removed from the library.")
                return
        print(f"Book '{title}' is not in the library.")

    def search_books(self, search_term):
        found_books = []
        for book in self.books:
            if search_term in book[0]:
                found_books.append(book)
        return found_books

    def list_books(self):
     print("Books in the library:",self.book_set )
    

    def categorize_books(self):
        self.genre_dict.clear()
        for book in self.books:
            genre = book[2]
            if genre not in self.genre_dict:
                self.genre_dict[genre] = [book]
            else:
                self.genre_dict[genre].append(book)
        return self.genre_dict


library = Library_management()


library.add_to_library("Cars", "John lasseter", "Animated")
library.add_to_library("Avengers", "Stan lee", "Action")
library.add_to_library("Ms Dhoni the untold story", "Ms Dhoni", "Biography")


library.remove_from_book("Cars")


search_results = library.search_books("Lord")
print("\nSearch Results:")
for book in search_results:
    print(f"\nTitle: {book[0]}, Author: {book[1]}, Genre: {book[2]}")


library.list_books()


categorized_books = library.categorize_books()
print("\nCategorized Books:")
for genre, books in categorized_books.items():
    print(f"\nGenre: {genre}")
    for book in books:
        print(f"Title: {book[0]}, Author: {book[1]}")

