
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)cccccc
# Your Google Custom Search API Key and Search Engine ID
API_KEY = 'YOUR_GOOGLE_API_KEY'
SEARCH_ENGINE_ID = 'YOUR_SEARCH_ENGINE_ID'

def google_search(query):
    search_url = f"https://www.googleapis.com/customsearch/v1?q={}&key={}&cx="
    response = requests.get(search_url)
    search_results = response.json()

    if 'items' in search_results:
        first_result = search_results['items'][0]
        title = first_result['title']
        snippet = first_result['snippet']
        link = first_result['link']
        return f"{title}\n{snippet}\nRead more: {}"
    else:
        return "Sorry, I couldn't find any information on that."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_message = request.form['msg'
if __name__ == "__main__":
    app.run(debug=True)
