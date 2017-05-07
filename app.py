from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
	"""Index page"""
	return render_template("index.html")

@app.route('/profile', methods=["GET", "POST"])
def profile():
	"""Render profile according to request"""
	if request.method == "POST":
		#todo
		return render_template("profile.html")
	else:
		return render_template("not_found.html")

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return render_template("404.html"), 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
