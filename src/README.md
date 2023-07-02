# Application

This is the installation guide for the app using docker.

### Running

It's simple to run: just follow the same steps provided in other docs.

clone the repository

```
git clone https://github.com/lucidrains/CoCa-pytorch.git
```
Then create an isolated virtual environment and install project dependencies. This helps ensure that the project runs with the correct versions of Python libraries and packages and prevents conflicts with other globally installed versions. Use the following commands:

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

After all the requirements are installed...

```
docker build -f ./Dockerfile.app .
```