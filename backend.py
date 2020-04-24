from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

if __name__ == '__main__':
    app.run()
