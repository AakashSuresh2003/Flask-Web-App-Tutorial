from website import create_app
import socket

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    ip_address = socket.gethostbyname(socket.gethostname())
    
    app.run(host='0.0.0.0', port=5000, debug=True)
