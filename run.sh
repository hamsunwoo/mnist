service cron start;uvicorn src.mnist.main:app --host 0.0.0.0 --port 8080 --reload
