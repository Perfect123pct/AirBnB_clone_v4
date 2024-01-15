import os
import uuid
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/0-hbnb/')
def hbnb():
    cache_id = str(uuid.uuid4())
    template_path = '0-hbnb.html' if os.path.exists('web_dynamic/templates/0-hbnb.html') else '8-hbnb.html'
    return render_template(template_path, cache_id=cache_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
