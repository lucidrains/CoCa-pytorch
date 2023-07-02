# Database

This application still hasn't a database (DB). Nevertheless, we created a Docker Container that may be used when (or if) it is created, as the code owner(s) demands.

### Running

It's simple to run: just follow the same steps provided in other docs.

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

After all the requirements are installed...

```
docker-compose up -d
```