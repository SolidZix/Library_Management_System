import os

# If running inside Docker, set DOCKER=1
if os.getenv("DOCKER"):
    db_url = os.getenv(
        "db_url",
        "postgresql+psycopg2://postgress:123456789@db:5432/postgres"
    )
else:
    # running on host
    db_url = os.getenv(
        "db_url",
        "postgresql+psycopg2://postgress:123456789@localhost:5432/postgres"
    )
