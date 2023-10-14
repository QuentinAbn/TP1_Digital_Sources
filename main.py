from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def hello_world():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=G-MJH545RKJV"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-MJH545RKJV');
    </script>
    """
    return prefix_google + "Hello World"

@app.route("/logger")
def logger():
    # Log on the Python server
    app.logger.info("This is a python log")    
    # Log on the browser using JavaScript
    log = """<script>console.log("This is a browserlog");</script>"""
    
    return log

@app.route("/textbox", methods=["GET", "POST"])
def textbox():
    if request.method == "POST":
        message = request.form.get("message")
        return f"Message submitted: {message}"
    
    return """
    <form method="POST">
        <label for="message">Enter message:</label>
        <input type="text" id="message" name="message" required>
        <input type="submit" value="Ok">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)