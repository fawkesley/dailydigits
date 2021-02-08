run_demo:
	pipenv run python main.py

run_dev_server:
	FLASK_APP=app.py pipenv run python -m flask run
