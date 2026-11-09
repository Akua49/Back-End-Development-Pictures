# Back-End-Development-Pictures

Created from the IBM Skills Network template ibm-developer-skills-network/luggb-Back-End-Development-Pictures.

## Environment Setup

Run `bash bin/setup.sh` from the repository. The supplied setup installs Python 3.9.x and creates the virtual environment named `venv` at `~/venv` (`/home/theia/venv` in the original lab). Activate it with `source ~/venv/bin/activate`. Confirm the interpreter using `python --version`.

The setup script reached its Capstone Environment Setup Complete message in the lab. Its legacy Postgres/Docker checks reported unavailable commands; this in-memory Pictures service requires neither database. Dependencies were installed and all eleven unmodified pytest tests passed using the Python 3.9 virtual environment.

```sh
source ~/venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
FLASK_APP=app flask run --host 0.0.0.0 --port 5000
```

## API

GET /health, /count, /picture and /picture/<id>; POST /picture; PUT and DELETE /picture/<id>. POST returns 201, a duplicate returns 302 per the supplied tests, DELETE returns 204, and missing records return 404. Data starts from backend/data/pictures.json and changes persist for the process lifetime.

## Container

The Dockerfile uses Python 3.9.16-slim and exposes port 3000. Build with `docker build -t pictures .` and run with `docker run -p 3000:3000 pictures`. The deployed Code Engine endpoint is https://pictures.2gykk5wm4vy1.us-south.codeengine.appdomain.cloud.
