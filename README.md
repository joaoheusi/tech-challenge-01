# tech-challenge-01

## To run using Docker Compose:
Run:
```
docker compose up
```
## To run for development:
Run:
```
uvicorn src.server.index:app --host 0.0.0.0 --port 8000 --reload
```



find src -type d -exec sh -c '[ ! -f "{}/__init__.py" ] && touch "{}/__init__.py"' \; 