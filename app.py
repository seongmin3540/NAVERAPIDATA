from flask import Flask, render_template, request
import urllib.request
import json

app = Flask(__name__)

CLIENT_ID = "xJtY68GUcSlPzE3vtPZM"
CLIENT_SECRET = "qqU295F_Ba"

def get_naver_search_results_book(query):

    enc_text = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/book?query={enc_text}"# 네이버 책 검색 API 사용

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", CLIENT_SECRET)

    try:
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            response_body = response.read()
            return json.loads(response_body.decode("utf-8"))["items"]
        else:
            return []
    except Exception as e:
        print("Error:", e)
        return []
    
def get_naver_search_results_image(query):

    encText = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/image?query={encText}&display=30"  # display=30 추가

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",CLIENT_ID)
    request.add_header("X-Naver-Client-Secret",CLIENT_SECRET)

    try:
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            response_body = response.read()
            return json.loads(response_body.decode("utf-8"))["items"]
        else:
            return []
    except Exception as e:
        print("Error:", e)
        return []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/book")
def book():
    query = request.args.get("query", "") 
    results = get_naver_search_results_book(query)
    return render_template("book.html", results=results, query=query)

@app.route("/image")
def image():
    query = request.args.get("query", "") 
    results = get_naver_search_results_image(query)
    return render_template("image.html", results=results, query=query)

if __name__ == "__main__":
    app.run(debug=True)
