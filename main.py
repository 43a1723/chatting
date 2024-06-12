from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    # Lấy tên người dùng từ dữ liệu gửi đi
    user_name = data['name']
    message = f"{user_name}: {data['message']}"
    
    print(f"Received message: {message}")
    
    # Phát đi tin nhắn đã thêm tên người dùng
    emit('receive_message', {'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
