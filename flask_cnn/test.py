from flask import Flask, render_template 
 
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template('img.html', image_file="uploads/test.png")
 
if __name__ == "__main__":
    app.run()