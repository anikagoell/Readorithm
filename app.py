from flask import Flask, render_template, request
import pickle
import numpy as np

popularBooks = pickle.load(open('popular.pkl', 'rb'))
ptable = pickle.load(open('ptable.pkl', 'rb'))
book=pickle.load(open('book.pkl', 'rb'))
costable=pickle.load(open('costable.pkl', 'rb'))


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/top60")
def top60():
    return render_template(
        "top60.html",
        book_name=list(popularBooks['Title'].values),
        author=list(popularBooks['Author'].values),
        image=list(popularBooks['URL-M'].values),
        votes=list(popularBooks['Rating Count'].values),
        rating=[round(r, 1) for r in popularBooks['Rating Avg'].values]
    )
    
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/search")
def search():
    return render_template("search.html", data=None)

@app.route("/searchbook", methods=["POST"])
def searchbook():
    userinput = request.form.get("bookname")
    
    if not userinput:
        return render_template("search.html", data=None)

    userinput = userinput.strip().lower()
    matches = [title for title in ptable.index if title.lower() == userinput]

    if not matches:
        return render_template("search.html", data=None)

    index = np.where(ptable.index == matches[0])[0][0]
    
    similiar = sorted(
        list(enumerate(costable[index])),
        key=lambda x: x[1],
        reverse=True)[1:11]

    data = []

    for i in similiar:
        item = []
        temp = book[book["Title"] == ptable.index[i[0]]]
        item.extend(list(temp.drop_duplicates('Title')['Title'].values))
        item.extend(list(temp.drop_duplicates('Title')['Author'].values))
        item.extend(list(temp.drop_duplicates('Title')['URL-L'].values))
        item.extend(list(temp.drop_duplicates('Title')['Published-Year'].values))
        data.append(item)

    return render_template("search.html", data=data)

if __name__ == '__main__':
    app.run()