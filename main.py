from flask import Flask, request, render_template
import logging
import requests


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
@app.route('/google_request', methods=['GET'])
def google_request():
    #create buttons to choose the request
    return """
    <form method="GET" action="/Ganalytics_request">
        <input type="submit" value="Google Analytics dashboard of the App">
    </form>
    <form method="GET" action="/request_cookies">
        <input type="submit" value="Google Analytics request cookie">
    </form>
    """

@app.route('/Ganalytics_request', methods=['GET'])
def Ganalytics_request():
    google_analytics_url = "https://analytics.google.com/analytics/web/#/p407502992/reports/intelligenthome"
    
    try:
        response = requests.get(google_analytics_url)
        response.raise_for_status()

        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error making Ganalytics request: {str(e)}"

@app.route('/request_cookies', methods=['GET'])
def request_cookies():
    google_analytics_url = "https://analytics.google.com/analytics/web/#/p407502992/reports/intelligenthome"
    
    try:
        response = requests.get(google_analytics_url)
        response.raise_for_status()

        # get the cookies
        cookies = response.cookies
        # return the cookies
        return render_template('cookies.html', cookies=cookies)
    except requests.exceptions.RequestException as e:
        return f"Error making cookies request: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)