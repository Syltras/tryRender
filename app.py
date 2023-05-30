from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
ar=[{"name":"aviel"},{"name":"jacov"}]

@app.route('/')
def index():
    return """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <h1>wow, Poggers</h1>
    <script src="https://unpkg.com/axios@1.1.2/dist/axios.min.js"></script>
    <script>
        axios.get('https://delme.onrender.com/dt').then(function (response) { console.log(response.data); })
    </script>
</body>

</html>"""


@app.route('/dt')
def dt():
    return ar


if __name__ == '__main__':
    app.run(debug=True)
