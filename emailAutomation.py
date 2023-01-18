from email.message import EmailMessage
import smtplib
from datetime import datetime
import pyodbc as odbc
import textwrap

# ESTABLISHING CONNECTION TO MICROSOFT AZURE SQL SERVER DATABASE
DRIVER = "ODBC Driver 18 for SQL Server"
SERVER_NAME = "anjin.database.windows.net,1433"
DATABASE_NAME = "RecommenderSystem"
DB_USER = str(input("SQL Server username: "))
DB_PASSWORD = str(input("SQL Server password: "))

connection_string = textwrap.dedent(f"""
    Driver={{{DRIVER}}};
    Server={SERVER_NAME};
    Database={DATABASE_NAME};
    Uid={DB_USER};
    Pwd={DB_PASSWORD};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;""")
db = odbc.connect(connection_string)
cursor = db.cursor()

sender = "fred@anjin.app"
password = #add password
receiver = "fredt1797@gmail.com"

now = datetime.now()
subject = f"[Anjin] Your Startup Recommendations Are Ready"

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = f"Anjin <test@anjin.app>"
msg['To'] = receiver



msg.add_alternative(f"""
    <!DOCTYPE html>
    <html lang="en">
        <head></head>
        <body>
            <h3>Testing embedded HTML form for Recommendation Delivery {now.strftime('%m-%d-%Y %H:%M:%S')}</h3>
            <form method="post">
                Username: <br>
                <input type="text" name="username"><br><br>
                Password: <br>
                <input type="password" name="password"><br><br>
                Role: <br>
                <select name="role">
                <option value="administrator">Administrator</option>
                <option value="customer">Customer</option>
                </select> <br>
            </form>
            <p>Should you have any question, do not hesitate to contact fred@anjin.app</p>
        </body>
    </html>
""", subtype="html")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)
