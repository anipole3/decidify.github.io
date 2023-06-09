from flask import Flask, render_template, url_for, request, redirect
import csv
import time

app = Flask(__name__)

print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# @app.route('/al/<string:page_name>')
# def al_html_page(page_name):
#     return render_template("al_"+page_name)

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         name = data['name']
#         message = data['message']
#         file = database.write(f"\n{name},{email},{message}")

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database_csv:
        email = data['email']
        name = data['name']
        message = data['message']
        ts = time.time()
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email,message, ts])

#redirect after submitting form 
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return "something went wrong. try again."
    

@app.route('/al_submit_form', methods=['POST', 'GET'])
def submit_form_al():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/faleminderit.html')
        except:
            return 'Diçka shkoi gabim. Ju lutem provojeni përsëri.'
    else:
        return 'Diçka shkoi gabim. Ju lutem provojeni përsëri.'