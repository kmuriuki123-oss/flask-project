from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = 'secure_chat_routing_key'

CHAT_HISTORY = [
    {"user": "Bravin", "text": "Hey Meridian! Is the new Flask server working for you?", "time": "03:00 AM"},
    {"user": "Meridian", "text": "Yes! Running perfectly on port 8080 now. 🚀", "time": "03:01 AM"}
]

@app.route('/')
def home():
    return render_template('index.html', history=CHAT_HISTORY)

@app.route('/api/send', methods=['POST'])
def send_message():
    username = request.json.get('username', 'Guest').strip()
    message_text = request.json.get('text', '').strip()
    
    if not username or not message_text:
        return jsonify({"status": "error", "message": "Fields cannot be empty"}), 400
        
    new_msg = {
        "user": username,
        "text": message_text,
        "time": "Just now"
    }
    CHAT_HISTORY.append(new_msg)
    return jsonify({"status": "success", "message": new_msg, "all_messages": CHAT_HISTORY})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
