# r0s.io/shorten Server

## Endpoints

```text
POST /s - creates a new shortened URL
    200 - if title was successfully created
    410 - if title exists in DB

    Body
    {
        "url": string,
        "title": string
    }
    Response
    {
        "title": string
    }

GET /s/<title> - redirects browser to linked URL
    404 - if title does not exist
```

## Setup

```bash
python3 -m venv venv
pip3 install -r requirements.txt
```

## Run

```bash
docker-compose up -d # starts a mongoDB instance and a mongo-express instance
./scripts/run.sh
```
