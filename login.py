from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == 'change-me':
            # Authentication successful, redirect to index-black.html
            return redirect(url_for('index_black'))
        else:
            # Authentication failed, show error message
            error = 'Invalid password'
            return render_template('login.html', error=error)
    else:
        # Show login form
        return render_template('login.html')

@app.route('/index-black')
def index_black():
    # User is authenticated, show index-black.html
    return render_template('index-black.html')

if __name__ == '__main__':
    app.run(debug=True)