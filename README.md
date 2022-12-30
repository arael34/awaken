# awaken

an app to track daily habits.

## features

user authentication(login, logout, signup)

task creation, editing, and deletion

statistics, tracking from two weeks ago until the present

## to run locally
you must have python 3.10 downloaded.

make a directory and clone into it
```Shell
mkdir awaken
cd awaken
git clone https://github.com/arael34/awaken.git .
```
spawn a venv shell and download deps
```Shell
pip install pipenv # if you don't have pipenv installed
pipenv shell
pipenv update
```
finally, cd into app and run
```
cd app
python3 manage.py runserver
```
navigate to the local link shown and you'll see the app.
