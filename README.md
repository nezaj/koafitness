### Quickstart
Because sometimes you just want to see it work
```
git clone git@github.com:nezaj/koafitness.git
cd koafitness
sudo pip install virtualenv
make virtualenv
source ~/.virtualenvs/koafitness/bin/activate
./manage.py db upgrade
python -c 'import os; print "APP_KEY={}".format(os.urandom(24))' > .env  # Generates random secret key for the app
./manage.py runserver
```

Now go to [http://localhost:5000/][localhost] in your favorite browser. Huzzah!

[localhost]: http://localhost:5000/
