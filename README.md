# Back-End-Development-Pictures

Flask REST API for the band website, created from the IBM Skills Network template.

## Environment Setup
- Repository created from the provided template.
- Environment initialized using `bash bin/setup.sh` in Skills Network Cloud IDE.
- Dependencies installed in the lab Python virtual environment (`/home/theia/venv`).
- The legacy setup script reports unavailable Postgres/Docker commands; this in-memory service does not require either database.

## Run
```sh
python -m pip install -r requirements.txt
FLASK_APP=app flask run --host 0.0.0.0 --port 5000
```

## API
- GET /health: service health
- GET /count: number of pictures
- GET /picture: all pictures
- GET /picture/<id>: one picture (404 when absent)
- POST /picture: create a picture (201); duplicate id returns 302 as required by the supplied contract
- PUT /picture/<id>: replace a picture
- DELETE /picture/<id>: delete a picture (204)

Data is initialized from backend/data/pictures.json and changes remain in memory for the lifetime of the process.

## Validation
The original, unmodified test suite passes: **11 passed** with `python -m pytest -v`.

## Container
Build with `docker build -t pictures .` and run with `docker run -p 5000:5000 pictures`.
