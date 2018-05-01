from flask import Flask, render_template, request, redirect, url_for
from helpers import *
import emoji;

app = Flask(__name__)

@app.route('/')
def index():
	"""Index page"""
	return render_template("index.html")

@app.route('/about')
def about():
	"""About page"""
	return render_template("about.html")

@app.route('/profile', methods=["GET", "POST"])
def profile():
	"""Render profile according to request"""

	# Get username from post method
	user = request.form.get("username")
	#print user
	if not user:
		return redirect(url_for('index'))

	# Check if the request is given from post method or not
	if request.method == "POST":
		# Get all the data from github api
		basic = basic_retrive(user)
		# Check if anything is missing or not
		if not basic:
			return render_template("not_found.html")

		watch = watch_list(user)
		org = organizations(user)


		# If everything goes fine
		return render_template("profile.html", basic=basic, watch=watch, org=org, emoji=emoji)

	# If request method is get then redirect to
	else:
		return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return render_template("404.html"), 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


if __name__ == '__main__':
    app.run()
