# Readorithm - Book Recommendation Web App

Hey! This is my Flask project called **Readorithm**.  
It’s a simple **book recommendation web app** where you can see popular books and get recommendations based on the book you search for.

## About the Project
This project is made using **Python** and **Flask**.  
I used `.pkl` files to store:

- Popular books data (`popular.pkl`)  
- Pivot table of book titles (`ptable.pkl`)  
- Book details (`book.pkl`)  
- Cosine similarity table for recommendations (`costable.pkl`)  

The idea is simple: instead of calculating everything every time, I save the data in `.pkl` files and load it when needed.  


## Features
- Home page with a welcome message.  
- Top 60 popular books page with title, author, rating, and image.  
- Search page: type a book name and get **10 similar book recommendations**.  
- Contact page (static page with contact info).  

## Project Structure
readorithm/
│
├── popular.pkl # Popular books data
├── ptable.pkl # Pivot table of books
├── book.pkl # Book details
├── costable.pkl # Cosine similarity matrix
├── app.py # Main Flask app
├── templates/ # HTML templates for pages
│ ├── home.html
│ ├── top60.html
│ ├── search.html
│ └── contact.html
├── static/ # Images, CSS, JS files
├── README.md # This file
└── .gitattributes # Git LFS tracking for large files

## How to Run
1. Make sure **Python** is installed on your system.  
2. Install required packages:
    flask, numpy, pickle pandas
3.Make sure you have Git LFS installed to download .pkl files from GitHub.
4.Run the app


## Why Git LFS?
The .pkl files are large, so I used Git Large File Storage (LFS) to store them on GitHub.
GitHub won’t reject the files.
Anyone cloning the repo will need Git LFS to get the real .pkl files.

## Future Improvements
Add a login system so users can save favorite books.
Improve the UI with Bootstrap or Tailwind CSS.
Add more filters like genre or rating for recommendations.
Compress .pkl files to reduce size and loading time.
