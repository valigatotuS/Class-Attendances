from my_app import create_app
from config import Config

def main():
    app = create_app(Config)
    app.run(port=5050)

if __name__ == '__main__':
    main()