from app import create_app

app = create_app('APP_CONFIG_DEV_FILE')

if __name__ == '__main__':
    app.run(debug=True)
