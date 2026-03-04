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
├── popular.pkl # Popular books data<br>
├── ptable.pkl # Pivot table of books<br>
├── book.pkl # Book details<br>
├── costable.pkl # Cosine similarity matrix<br>
├── app.py # Main Flask app<br>
├── templates/ # HTML templates for pages<br>
│ ├── home.html<br>
│ ├── top60.html<br>
│ ├── search.html<br>
│ └── contact.html<br>
├── static/ # Images, CSS, JS files<br>
├── README.md # This file<br>
└── .gitattributes # Git LFS tracking for large files<br>

## How to Run
1. Make sure **Python** is installed on your system.  <br>
2. Install required packages:<br>
    flask, numpy, pickle pandas<br>
3.Make sure you have Git LFS installed to download .pkl files from GitHub.<br>
4.Run the app<br>


## Why Git LFS?
-The .pkl files are large, so I used Git Large File Storage (LFS) to store them on GitHub.<br>
-GitHub won’t reject the files.<br>
-Anyone cloning the repo will need Git LFS to get the real .pkl files.<br>

## Future Improvements
-Add a login system so users can save favorite books.<br>
-Improve the UI with Bootstrap or Tailwind CSS.<br>
-Add more filters like genre or rating for recommendations.<br>
-Compress .pkl files to reduce size and loading time.<br>
