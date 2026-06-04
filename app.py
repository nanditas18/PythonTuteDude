from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    
    print("Received Registration Details:")
    print(f"Username: {username}")
    print(f"Email: {email}")
    
    return f"Thank you, {username}! Registration submitted successfully."

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)