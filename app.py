import datetime

from dailydigits import today_in_uk, date_to_digits

from flask import Flask
app = Flask(__name__)

TEMPLATE = """<html>
  <head><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
  <body>
    <h1>Daily codes</h2>
    <ul>
    {}
    </ul>
  </body>
</html>"""


@app.route('/<secret>')
def index(secret):
    today = today_in_uk()

    lines = []

    for days in range(0, 10):
        date = today + datetime.timedelta(hours=24*days)

        digits = date_to_digits(date, secret, 8)

        lines.append('<li><code>*{}#</code> - {}</li>'.format(
            ''.join(['{}'.format(d) for d in digits]),
            date.strftime('%A, %d %b %Y')
        ))

    return TEMPLATE.format('\n'.join(lines))
