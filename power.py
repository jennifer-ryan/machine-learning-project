from flask import Flask, send_from_directory

app = Flask(__name__,
            static_url_path = "", 
            static_folder = "staticpages")


# Index
@app.route('/')
def index():
    index= send_from_directory('staticpages', "index.html")
    return index


# Run main
if __name__ == "__main__":
   app.run(debug=True)