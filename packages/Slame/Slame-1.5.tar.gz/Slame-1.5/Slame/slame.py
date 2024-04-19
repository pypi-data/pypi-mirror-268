import socket
import os
import secrets
import time
import sqlite3
import hashlib
import requests
from urllib.parse import parse_qs
import importlib.util



"""
(c) ZHRXXgroup 
https://zhrxxgroup.com

Version: 1.0

"""
class ZHRXX:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.routes = {}
        self.middlewares = []

    def route(self, path, methods=['GET']):
        def decorator(func):
            self.routes[path] = {
                'methods': methods,
                'handler': func
            }
            return func
        return decorator

    def use(self, middleware):
        self.middlewares.append(middleware)

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Server is listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = server_socket.accept()
            request_data = client_socket.recv(1024).decode('utf-8')

            if request_data:
                request_lines = request_data.split('\n')
                request_line = request_lines[0]
                method, path, _ = request_line.split()
                response = self.handle_request(method, path, request_data)
                client_socket.send(response.encode('utf-8'))
                client_socket.close()

    def handle_request(self, method, path, request_data):
        # Execute middleware functions
        for middleware in self.middlewares:
            middleware()

        # Check if the requested path matches any defined route
        if path in self.routes:
            route = self.routes[path]
            # Check if the requested HTTP method is allowed for the route
            if method in route['methods']:
                if method == 'POST':
                    # Parse request data for POST requests
                    content_length = self.get_content_length(request_data)
                    data = self.parse_post_data(request_data, content_length)
                    # Execute the handler function for the matched route with provided data
                    response = route['handler'](data)
                else:
                    # Execute the handler function for the matched route
                    response = route['handler']()
                # Return a successful HTTP response with the response content
                return f"HTTP/1.1 200 OK\n\n{response}"
            else:
                # Return a "Method Not Allowed" response if the method is not allowed for the route
                return "HTTP/1.1 405 Method Not Allowed\n\n405 Method Not Allowed"
        # Check if the requested path starts with '/static/', indicating a static file request
        elif path.startswith('/static/'):
            # Serve the requested static file
            return self.serve_static_file(path)
        else:
            # Return a "Not Found" response for paths that don't match any route or static file
            return "HTTP/1.1 404 Not Found\n\n404 Not Found"

    def serve_static_file(self, path):
        # Get the absolute path to the file based on the script's directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        abs_file_path = os.path.join(script_dir, path[1:])

        try:
            with open(abs_file_path, 'rb') as file:
                content = file.read()
            return content.decode('utf-8')
        except FileNotFoundError:
            return "HTTP/1.1 404 Not Found\n\n404 Not Found"

    def get_content_length(self, request_data):
        # Parse Content-Length header to determine data size
        for line in request_data.split('\n'):
            if line.startswith('Content-Length:'):
                return int(line.split(':')[1])
        return 0

    def parse_post_data(self, request_data, content_length):
        # Parse POST data from request body
        body = request_data.split('\n\n')[-1]
        post_data = parse_qs(body)
        return post_data



"""
(c) ZHRXXgroup
https://zhrxxgroup.com/+

Version: 1.0.5
"""

class Work_with_Database:
    

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        # Create the 'users' table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT UNIQUE NOT NULL,
                                password TEXT NOT NULL)''')
        self.conn.commit()

    def close(self):
        self.conn.close()

    def add_user(self, username, password):
        # Hash the password before storing it in the database
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False  # Username is already taken

    def verify_user(self, username, password):
        # Verify user credentials and return user ID if successful
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, hashed_password))
        user_data = self.cursor.fetchone()
        if user_data:
            return user_data[0]
        return None

    def get_all_users(self):
        # Retrieve all users from the database
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        return users

    def delete_user(self, user_id):
        # Delete a user from the database by ID
        self.cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        self.conn.commit()

    '''
    (c) ZHRXXgroup
    https://zhrxxgroup.com

    Version 1.4

    added in Version 1.4 in Work_with_Database:
    custom_command()
    '''
    def custom_command(self, command, option1=None, option2=None, option3=None, option4=None, option5=None):
        # Create a list of options
        options = [option1, option2, option3, option4, option5]

        # Filter out None values
        options = [opt for opt in options if opt is not None]

        # Execute the command with optional parameters
        self.cursor.execute(command, options)

        # Commit the transaction
        self.conn.commit()

"""
(c) ZHRXXgroup
https://zhrxxgroup.com/

Version: 1.1

"""
class Sessions:
    '''
    (c) ZHRXXgroup
    https://zhrxxgroup.com

    Version 1.4

    added in Version 1.4 in Sessions:
    custom session_timeout(default: 1 hour)
    '''
    session_data = {}  # Dictionary to store session data
    def __init__(self, session_timeout=3600):
        self.session_timeout = session_timeout  # Session timeout in seconds (default: 1 hour)

    @staticmethod
    def create_session():
        session_id = secrets.token_hex(16)  # Generate a random session ID
        Sessions.session_data[session_id] = {'timestamp': time.time(), 'data': {}}  # Store creation timestamp and session data
        return session_id

    @staticmethod
    def get_session(session_id):
        session = Sessions.session_data.get(session_id)
        if session:
            # Check if the session has expired
            if time.time() - session['timestamp'] > Sessions.session_timeout:
                del Sessions.session_data[session_id]
                return None
            return session
        return None

    @staticmethod
    def update_session(session_id, data):
        session = Sessions.get_session(session_id)
        if session:
            session['data'].update(data)

    @staticmethod
    def end_session(session_id):
        if session_id in Sessions.session_data:
            del Sessions.session_data[session_id]

    @staticmethod
    def set_session_data(session_id, key, value):
        session = Sessions.get_session(session_id)
        if session:
            session['data'][key] = value
            Sessions.update_session(session_id, session['data'])

    @staticmethod
    def get_session_data(session_id, key):
        session = Sessions.get_session(session_id)
        if session:
            return session['data'].get(key)
        return None

"""
(c) ZHRXXgroup
https://zhrxxgroup.com/

Version: 1.2
"""
class Plugins:
    def __init__(self):
        self.plugin_manager = PluginManager()

    def load_plugin_from_file(self, file_path):
        spec = importlib.util.spec_from_file_location("plugin_module", file_path)
        plugin_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin_module)
        
        # Assuming the plugin class is defined within the module with the same name as the file: import Plugin_Name 
        plugin_class = getattr(plugin_module, "MyPlugin")
        plugin_instance = plugin_class()
        
        return plugin_instance

    def register_plugin_from_file(self, file_path):
        plugin_instance = self.load_plugin_from_file(file_path)
        self.register_plugin(plugin_instance)

    def register_plugin(self, plugin_instance):
        self.plugin_manager.register_plugin(plugin_instance)

    def use_plugin(self):
        plugin = self.plugin_manager.get_plugin()
        if plugin:
            plugin.use_plugin()
        else:
            print("No plugin registered.")

    def configure_plugin(self, **config):
        plugin = self.plugin_manager.get_plugin()
        if plugin:
            plugin.plugin_config(**config)
        else:
            print("No plugin registered.")


'''# Usage

if __name__ == "__main__":
    plugins_manager = Plugins()
    plugins_manager.register_plugin_from_file("my_plugin.py")

    plugins_manager.use_plugin()
    plugins_manager.configure_plugin(option1='value1', option2='value2')

'''

'''
(c) ZHRXXgroup
https://zhrxxgroup.com

Version 1.3

(update) Version 1.3.5
We fixed packages Sistem

(update) Version 1.3.8
We fixed the __init__.py file

(update) Version 1.4.2
debugger added
'''


'''
What we added?

Now u can use other packages(from other users) and upload own packages:
https://zhrxxgroup.com/slame/spm/ 


first:
terminal: pip install spmZX

at the start of file use:

from spmZX.packages import packages_import

to download a package use:

import spmZX
spmZX.download(PACKAGE_NAME, VERSION)
'''

"""
class Debugger(folder="static/debugger"):
    def launch(folder):
        if os.path.exists(folder):  
            start_debugger(folder)
        else:
            download_debugger()  

    def start_debugger(folder):
        server = ZHRXX("localhost", 5657)
        @server.route("/logs")
        def logs():
            return server.serve_static_file("/debugger/logs.html")
        
        @server.route("/console")
        def console():
            return server.serve_static_file("/debugger/console.html")
        
        server.start()
    
    def get_console() 
        ...
        
    def download_debugger():
        # Create the folder if it doesn't exist
        folder_path = os.path.join(os.getcwd(), "debugger")
        os.makedirs(folder_path, exist_ok=True)
    
        # Make a request to get the list of files in the folder
        response = requests.get("https://zhrxxgroup.com/slame/debugger")
        if response.status_code != 200:
            print("Failed to retrieve folder contents")
            return

        # Extract the file URLs
        file_urls = response.text.splitlines()
    
        # Download each file
        for file_url in file_urls:
            file_name = file_url.split('/')[-1]
            file_path = os.path.join(folder_path, file_name)
        
            # Download the file
            print(f"Downloading {file_name}...")
            r = requests.get(file_url, stream=True)
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                    f.write(chunk)
            print(f"{file_name} downloaded successfully")



"""







































