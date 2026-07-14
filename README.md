# 📚 Library Management System

A simple **Library Management System** built in **Python** using **Object-Oriented Programming (OOP)** and a modular project structure. The application allows users to manage books, issue and return them, and store data persistently using JSON.

## ✨ Features

- Add new books
- View all books
- Issue books
- Return books
- Persistent storage using JSON
- Modular code organization
- Object-Oriented Programming (OOP)

## 📂 Project Structure

```text
library_management/
│── main.py          # Entry point
│── book.py          # Book class
│── member.py        # Member class
│── library.py       # Library operations
│── utils.py         # Utility functions and menu
│── data.py          # JSON read/write functions
│── books.json       # Generated automatically
│── README.md
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or later

### Installation

1. Clone the repository:

```bash
git clone https://github.com/aryan6002261/library-management-system.git
```

2. Navigate to the project directory:

```bash
cd library-management-system
```

3. Run the application:

```bash
python main.py
```

## 🛠 Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- File Handling

## 📖 How It Works

- Add books to the library.
- View all available books.
- Issue books to mark them as unavailable.
- Return books to make them available again.
- Book data is automatically saved in `books.json`.

## 🔮 Future Enhancements

- Search books by title or author
- User authentication
- Fine calculation for overdue books
- SQLite/MySQL database support
- Tkinter GUI
- Book reservation system

## 📄 License

This project is licensed under the MIT License.
