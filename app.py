from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def Homepage():
    conn = sqlite3.connect('growly.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from crops")
    rows = cur.fetchall()
    return render_template("index.html", crops=rows)

def checkbox(crop):
    selected_options = request.form.getlist('checkbox')
    return f'Selected options: {", ".join(selected_options)}'
       
if __name__ == "__main__":
    app.run(port = 8000, debug=True)