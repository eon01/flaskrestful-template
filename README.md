# Flask Restful Code Template
A code template to start Flask API REST projects using Flask Restful


## Without Docker

```
virtualenv -p python3 my_app
cd my_app
. bin/activate
git clone <my_url> app
cd app
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```


## With Docker

```
git clone <my_url> app
cd app
docker build -t my_app . 
docker run -it --name my_app -p 80:5000 my_app
```

