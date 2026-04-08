# 📚 Readorithm – Book Recommendation Web App  

Readorithm is a Flask-based web application that recommends books based on user preferences and rating patterns. It combines **popularity-based filtering** and **collaborative filtering** to help users discover their next read.

🔗 **Live Demo:** https://readorithm.onrender.com/  

---

## 🚀 Features  

- View **Top 60 popular books** with ratings and details  
- Search for a book and get **similar recommendations**  
- Clean and simple UI built with HTML, CSS, and Bootstrap  
- Fast performance using precomputed data (`.pkl` files)  

---

## 🧠 How It Works  

The recommendation system is based on **item-based collaborative filtering**:

- User-book interactions are converted into a **pivot table**  
- Missing values are handled for matrix operations  
- **Cosine similarity** is applied to measure similarity between books  
- Top similar books are recommended based on similarity scores  

---

## 📊 Data Processing  

To improve recommendation quality:  

- Filtered users with very few ratings (reduces noise)  
- Selected books with sufficient ratings (ensures reliability)  
- Precomputed matrices stored using `.pkl` files for faster performance  

---

## 🛠 Tech Stack  

- **Backend:** Flask (Python)  
- **Data Processing:** Pandas, NumPy  
- **Frontend:** HTML, CSS, Bootstrap  
- **Model Storage:** Pickle  
- **Deployment:** Render  

---

## 📁 Project Structure  

```
readorithm/
│
├── popular.pkl        # Popular books data
├── ptable.pkl         # Pivot table
├── book.pkl           # Book metadata
├── costable.pkl       # Cosine similarity matrix
├── app.py             # Flask backend
│
├── templates/
│   ├── home.html
│   ├── top60.html
│   ├── search.html
│   └── contact.html
│
├── static/            # CSS, images
├── README.md
└── .gitattributes     # Git LFS tracking
```

---

## ⚙️ How to Run Locally  

1. Clone the repository  
```bash
git clone https://github.com/anikagoell/Readorithm.git
cd Readorithm
```

2. Install dependencies  
```bash
pip install flask pandas numpy
```

3. Install Git LFS and pull large files  
```bash
git lfs install
git lfs pull
```

4. Run the app  
```bash
python app.py
```

5. Open in browser  
```
http://127.0.0.1:5000/
```

---

## 📦 Why Git LFS?  

- `.pkl` files are large and exceed normal GitHub limits  
- Git LFS ensures proper storage and download  
- Required for running the project locally  

---

## 🔧 Future Improvements  

- Add fuzzy search for better user experience  
- Improve UI/UX design  
- Add user authentication and saved preferences  
- Implement hybrid recommendation system (content + collaborative)  
- Optimize model storage and loading time  

---

## 📸 Screenshots  

<img width="1919" height="906" alt="image" src="https://github.com/user-attachments/assets/927e66ce-37d5-431a-ba5b-7edce243e320" />

<img width="1919" height="901" alt="image" src="https://github.com/user-attachments/assets/5d01fe99-fc53-4a21-93c8-3a793d91dcbd" />

<img width="1918" height="905" alt="image" src="https://github.com/user-attachments/assets/2e8da97e-4240-4c6b-8d51-b0d767b470c8" />



---

⭐ If you like this project, consider giving it a star!
