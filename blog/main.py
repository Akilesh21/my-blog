from flask import Flask,render_template,request
import requests
import smtplib
app = Flask(__name__)


@app.route('/')
def home_page():
    response = requests.get(url="https://api.npoint.io/108de17d02a9cd8b5af7")
    get_posts = response.json()
    return render_template("index.html",posts = get_posts)

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/about')
def about_page():
    return render_template("about.html")
@app.route('/post1')    
def post_1():
    response = requests.get(url="https://api.npoint.io/108de17d02a9cd8b5af7")
    get_post = response.json()
    return render_template("post.html",posts = get_post)  
@app.route('/post2')    
def post_2():
    response = requests.get(url="https://api.npoint.io/108de17d02a9cd8b5af7")
    get_post = response.json()
    return render_template("post1.html",posts = get_post)  
@app.route('/post3')    
def post_3():
    response = requests.get(url="https://api.npoint.io/108de17d02a9cd8b5af7")
    get_post = response.json()
    return render_template("post2.html",posts = get_post)    
@app.route("/contact", methods=["GET", "POST"])
def contact():
    my_mail ="YOUR EMAIL"
    password = "YOUR PASSWORD"
    if request.method == "POST":
        data = request.form
        name=data["name"]
        email=data["email"]
        phone=data["phone"]
        msg=data["message"]
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_mail,password=password)
        connection.sendmail(from_addr=my_mail,to_addrs="akhilesh.soni@somaiya.edu",msg=f"Subject:Website email\n\nName:{name}\nEmail:{email}\nPhone_Number:{phone}\nMessage:{msg}")
        connection.close()
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)        
if __name__ == "__main__":
    app.run(debug=True)

