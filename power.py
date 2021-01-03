from flask import Flask

app = Flask(__name__,
            static_url_path = "", 
            static_folder = "staticpages")


# Index
@app.route('/')
def index():
    return index.html
    #content = send_from_directory('staticpages', "index.html")
    #return content