-- Create Database
CREATE DATABASE IF NOT EXISTS LibraryDB;
USE LibraryDB;

-- Create Tables
CREATE TABLE Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    published_year INT,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    CONSTRAINT fk_author FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

CREATE TABLE Members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    membership_date DATE NOT NULL
);

CREATE TABLE Loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    issue_date DATE NOT NULL,
    return_date DATE,
    CONSTRAINT fk_book FOREIGN KEY (book_id) REFERENCES Books(book_id),
    CONSTRAINT fk_member FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

-- Sample Data
INSERT INTO Authors (name, email) VALUES
('George Orwell', 'george.orwell@example.com'),
('J.K. Rowling', 'jk.rowling@example.com');

INSERT INTO Books (title, author_id, published_year, isbn) VALUES
('1984', 1, 1949, '9780451524935'),
('Harry Potter and the Sorcerer''s Stone', 2, 1997, '9780439554930');

INSERT INTO Members (full_name, email, membership_date) VALUES
('Alice Johnson', 'alice@example.com', '2023-01-10'),
('Bob Smith', 'bob@example.com', '2023-02-15');

INSERT INTO Loans (book_id, member_id, issue_date, return_date) VALUES
(1, 1, '2024-04-01', '2024-04-15'),
(2, 2, '2024-04-10', NULL);
