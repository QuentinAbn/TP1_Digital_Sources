from flask import Flask, request
import logging
import requests
import streamlit as st

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
    app.logger.info("This is a python log")    
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
@app.route("/google_request")
def google_request():
    req = requests.get("https://www.google.com/")
    return f"The Google request status code is: {req.status_code}"

@app.route("/display_cookies")
def display_cookies():
    req = requests.get("https://www.google.com/")
    st.markdown(req.cookies._cookies)
    return "Cookies displayed"

@app.route("/ganalytics_url")
def ganalytics_url():
    req2 = requests.get("https://analytics.google.com/analytics/web/#/p407502992/reports/intelligenthome")
    return f"The Ganalytics request status code is: {req2.status_code}"


if __name__ == "__main__":
    app.run(debug=True)