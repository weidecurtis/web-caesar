from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            <label>Rotate by:</label>
            <input type="text" name="rot" value="0" />
            <br>
            <textarea name="text">{0}</textarea>
            <br>
            <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    rot_by = request.form['rot']
    text_cipher = request.form['text']
    text_cipher = rotate_string(text_cipher, rot_by)
    return "<h1> " + text_cipher + "</h1>"
app.run()