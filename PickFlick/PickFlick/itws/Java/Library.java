import java.util.*;
import java.io.*;

class Book {
    private String title;
    private String author;
    private final String isbn;
    private boolean isAvailable;

    public Book(String title, String author, String isbn) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.isAvailable = true;
    }

    public String getIsbn() {
        return isbn;
    }

    public void borrowBook() {
        if (isAvailable) {
            isAvailable = false;
        } else {
            System.out.println("Borrow book not possible");
        }
    }

    public void returnBook() {
        if (!isAvailable) {
            isAvailable = true;
        } else {
            System.out.println("Return book not possible");
        }
    }

    public void display() {
        System.out.print(title + " " + author + " " + isbn + " ");
        if (isAvailable) {
            System.out.println("Available");
        } else {
            System.out.println("Not Available");
        }
    }
}

public class Library {
    private Book[] books;
    private int count;

    public Library(int n) {
        books = new Book[n];
        count = 0;
    }

    public void addBook(Book book) {
        if (count < books.length) {
            books[count++] = book;
        }
    }

    public Book findByIsbn(String isbn) {
        for (int i = 0; i < count; i++) {
            if (books[i].getIsbn().equals(isbn)) {
                return books[i];
            }
        }
        return null;
    }

    public void displayBooks() {
        for (int i = 0; i < count; i++) {
            books[i].display();
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // Reading the size of the library
        int size = in.nextInt();
        in.nextLine(); // Consume the newline character after nextInt()

        Library library = new Library(size);

        // Adding books to the library
        while (true) {
            String title = in.nextLine();
            if (title.equals("0")) break; // Exit loop when "0" is entered
            
            String author = in.nextLine();
            String isbn = in.nextLine();

            Book newBook = new Book(title, author, isbn);
            library.addBook(newBook);
        }

        // Display the books in the library
        library.displayBooks();

        // Perform borrow or return operations
        while (true) {
            System.out.print("Enter operation (1 to borrow, 2 to return, 0 to exit): ");
            int choice = in.nextInt();
            in.nextLine(); // Consume the newline after nextInt()

            if (choice == 0) break; // Exit if user chooses 0

            System.out.print("Enter ISBN: ");
            String isbn = in.nextLine();  // ISBN input

            Book book = library.findByIsbn(isbn);
            if (book == null) {
                System.out.println("Book not found with ISBN: " + isbn);
                continue;
            }

            if (choice == 1) {
                book.borrowBook();
            } else if (choice == 2) {
                book.returnBook();
            }

            // Display the books after the action
            System.out.println("\nBooks in the library after action:");
            library.displayBooks();
        }

        in.close();
    }
}
