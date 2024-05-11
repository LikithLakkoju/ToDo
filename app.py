from flask import Flask, render_template, request, redirect
import psycopg2
app=Flask(__name__)

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="Postgres",
                        port="5432")

@app.route("/", methods=["GET"])
def home():
     cursor=conn.cursor()
     cursor.execute(f"select * from tasks order by id")
     row=cursor.fetchall()
     return render_template("home.html",data=row)


@app.route("/addtask", methods=["POST"])
def addtask():
    data=request.form
    task=data.get("task")
    cursor=conn.cursor()
    cursor.execute(f"insert into tasks(task) values('{task}')")
    conn.commit()
    return redirect("/")

@app.route("/update", methods=["GET"])
def updatetask():
    id=request.args.get("id")
    value=request.args.get("value")
    cursor=conn.cursor()
    cursor.execute(f"update tasks set task='{value}' where id={id}")
    conn.commit()
    return redirect("/")

@app.route("/delte", methods=["GET"])
def deletetask():
    id=request.args.get("id")
    cursor=conn.cursor()
    cursor.execute(f"delete from tasks where id={id}")
    conn.commit()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)