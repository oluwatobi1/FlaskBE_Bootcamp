class User():
    def __init__(self, username, password, email ) -> None:
        super().__init__(username)
        self.username = username
        self.password = password
        self.email = email



user = [
    {
        "username": "freeman",
        "password": 12434,
        "email": "freeman@gmail.com"    
    },
    {
        "username": "freeman",
        "password": 12434,
        "email": "freeman@gmail.com"    
    },
    {
        "username": "freeman",
        "password": 12434,
        "email": "freeman@gmail.com"    
    },
]

user = [
    User("freeman", 1234, "freeman@gmail.com"),
    User("freeman", 1234, "freeman@gmail.com"),
    User("freeman", 1234, "freeman@gmail.com"),
    User("freeman", 1234, "freeman@gmail.com"),
]


# inheritance is -a relationship

class Device:
    def __init__(self, name):
        self.name = name

    def on(self):
        print(f"{self.name} is on")

    def off(self):
        print(f"{self.name} is off")


class Phone(Device):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

    def call(self):
        print(f"{self.name} is calling")
    
    def text(self):
        print(f"{self.name} is texting")

class Television(Device):
    def __init__(self, name, film):
        super().__init__(name)
        self.film = film

    def watch(self):
        print(f"{self.name} is watching {self.film}")

tv = Television()
tv.watch()

# composition HAS-A relationship

class BookShelf:
    def __init__(self, *books) -> None:
        self.books = books


class Book:
    def __init__(self) -> None:
        self.title = "The Great Gatsby"
        self.author = "F. Scott Fitzgerald"



book1 = Book()
book2 = Book()

shelf1 = BookShelf(book1, book2)


#  polymorphism is -a relationship