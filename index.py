from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_video_status():
    url = "https://hubcloud.foo/video/1xxtacinokkkihn"
    
    # Adding headers helps avoid being blocked by the host
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        rx = requests.get(url, headers=headers, timeout=10)
        return {
            "status_code": rx.status_code,
            "url": url,
            "content_preview": rx.text[:500]  # Shows first 500 characters of the page
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(debug=True)
