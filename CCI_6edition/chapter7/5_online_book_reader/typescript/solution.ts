

class User {
    name: string;
    billingInfo: any;
}


class Book {
    title: string;
    author: string;
    price: number;
    pageCount: number;
    chapterCount: number;

}

class BookRecord {
    book: Book;
    user: User;
    currentPage: number;
    bookMarks: number[];

    constructor(book: Book, user: User) {
        this.book = book;
        this.user = user;
        this.currentPage = 0;
        this.bookMarks = [];
    }

    addBookMark(page: number) {
        this.bookMarks.push(page);
    }
}

class CheckoutHandler {
    
    checkout(amount: number, user: User): Promise<boolean> {
        return new Promise(() => {});
    }
}

class BookReader {
    users: User[] = [];
    books: Book[] = [];
    records: BookRecord[] = [];
    checkoutHandler = new CheckoutHandler();

    constructor() {}

    
    addBook(book: Book) { this.books.push(book); }
    addUser(user: User) { this.users.push(user); }
    buyBook(book: Book, user: User) {
        this.checkoutHandler.checkout(book.price, user).then((checkoutSuccessfull) => {
            if( checkoutSuccessfull ) {
                this.records.push(new BookRecord(book, user));
            } else {
                console.log('Checkout failed')
            }
        })
    }

    getRecordsForUser(user: User) {
        let records: BookRecord[] = [];
        for(let record of this.records) {
            if( record.user == user ) {
                records.push(record);
            }
        }
        return records;
    }

    getUsersForBooks(book: Book) {
        let records: BookRecord[] = [];
        for(let record of this.records) {
            if( record.book == book ) {
                records.push(record);
            }
        }
        return records;
    }

    search(name: string) {}
}