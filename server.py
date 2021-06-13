
from flask import Flask, render_template, request, redirect, url_for
import csv
app = Flask(__name__)



@app.route('/<string:page_name>')
def dynamic(page_name):
    return render_template(page_name)


def write_to_csv(data):
	# writing user data into a csv file
	with open('CSV FILE LOCATION', 'a', newline='') as csvfile:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		writer = csv.writer(csvfile, delimiter=',')
		writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return render_template('/thankyou.html', email =  data["email"])  # thanking the user by his email
		except:
			return "Cannot save to database"
	else:
		return "Something went wrong Try Again"


