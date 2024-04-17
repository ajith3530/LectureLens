from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    student_summary_filepath = STUDENT_SUMMARY_FILEPATH
    admin_summary_filelpath = ADMIN_SUMMARY_FILEPATH

    with open(student_summary_filepath, 'r') as file:
        content1 = file.read()
    with open(student_summary_filepath, 'r') as file:
        content2 = file.read()

    return render_template('index.html', content1=content1, content2=content2)


if __name__ == '__main__':
    app.run(debug=True)
