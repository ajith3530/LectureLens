from flask import Flask, render_template

def create_flask_app(student_summary_filepath, admin_summary_filepath):
    app_main = Flask(__name__)
    @app_main.route('/')
    def index():

        if student_summary_filepath is None or admin_summary_filepath is None:
            raise FileNotFoundError

        with open(student_summary_filepath, 'r') as file:
            content1 = file.read()

        return render_template('index.html', content1=content1)
    @app_main.route('/admin')
    def admin():
        with open(admin_summary_filepath, 'r') as file:
            content2 = file.read()
        return render_template('admin.html', content2=content2)

    app_main.run(debug=True)

    return app_main
