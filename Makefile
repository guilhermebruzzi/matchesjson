clean:
	@find . -type f -name "*.pyc" -exec rm -rf {} \;

kill_run:
	@ps aux | awk '(make run && $$0 !~ /awk/){ system("kill -9 "$$2) }'

run: clean
	@python app.py

db:
	@mysql -u root -e 'CREATE DATABASE IF NOT EXISTS matches;'

setup: db
	@pip install -r requirements.txt
