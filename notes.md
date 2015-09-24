###### Notes

Run processes in the background on startup in Cloud 9:
 - http://stackoverflow.com/questions/20439267/how-to-start-automatically-cloud9-ide-on-server-startup

Postgres in Cloud 9:
 - http://stackoverflow.com/questions/28177912/postgres-database-setup-on-cloud9-asks-for-sudo-password
 - http://stackoverflow.com/questions/11919391/postgresql-error-fatal-role-username-does-not-exist
 - `$ sudo -u postgres -i` or `sudo sudo -u postgres psql` <-- use this one in C9
 - `$ sudo -s` then `sudo -u postgres psql` or `sudo su - postgres`
 - `$ createuser -d -P -s starseed`
 - `$ createdb -O starseed starseeddb`
 - Run Postgres Server `$ sudo service postgresql start` 
 - Set Postgres User `pg_hba.conf`: http://stackoverflow.com/a/18664239/1762493
 
PSQL Commands
 - `DROP DATABASE [ IF EXISTS ] name` http://www.postgresql.org/docs/8.2/static/sql-dropdatabase.html
 - `ALTER DATABASE one RENAME TO "one-two";` http://stackoverflow.com/a/3942826/1762493
 - `\l` list databases
 - `\du` list users
 - `\q` quit PSQL

Install psycopg2 for postgres
- http://stackoverflow.com/a/5450183
- `$ sudo apt-get install libpq-dev python-dev`
- `$ sudo pip install psycopg2` http://stackoverflow.com/questions/14391804/e-unable-to-find-a-source-package-for-psycopg2-or-use-pip-with-virtualenv?answertab=votes#tab-top 


Using chromedriver Using PhantomJS in AWS
 - http://selenium-python.readthedocs.org/en/latest/faq.html#how-to-use-chromedriver~~


Django Notes
 - Django AllAuth http://django-allauth.readthedocs.org/en/latest/


C9 Notes
- Running Django in C9
 - `$ ./manage.py runserver $IP:$PORT` 


AWS Notes
- Running Django in AWS:
 - `$ ./manage.py runserver 0.0.0.0` 
- Resizing AWS EC2 Instance: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html


Gunicorn
 - Restarting Unicorn
  - `$ sudo service gunicorn restart` 
  - `$ kill -HUP masterpid` # http://gunicorn-docs.readthedocs.org/en/latest/faq.html#how-do-i-reload-my-application-in-gunicorn
  - Finding the masterpid: `$ pstree -ap|grep gunicorn` # http://stackoverflow.com/a/26926130


