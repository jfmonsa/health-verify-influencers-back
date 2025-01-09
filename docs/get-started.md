# Get Started

```
docker ps up -d
```

# Getting Started

## Prerequisites

Make sure you have the following programs installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.13+](https://www.python.org/downloads/)
- [uv](https://github.com/uv-org/uv)

## Installation

1. Clone the repository:

   ```sh
   git clone <REPO_URL>
   cd health-verify-influencers-back
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install project dependencies using `uv`:
   ```sh
   pip install uv
   uv install
   ```

## Configuration

1. Create a [.env](http://_vscodecontentref_/0) file in the root of the project with the following content:
   ```properties
   DB_CONNECTION_STRING="postgresql+asyncpg://postgres:password@localhost:5433/health-influencers-db"
   PERPLEXITY_API_KEY="your-api-key"
   ```

## Database

1. Start the Docker containers (Only a continer is used to launch postgres):

   ```sh
   docker-compose up -d
   ```

2. Apply the database migrations:
   ```sh
   poe migration_upgrade
   ```

## Running the Project

1. Start the server in development mode:

   ```sh
   poe start_dev
   ```

2. The server should be running at `http://localhost:8000`.

## Running Tests

1. Run the tests:
   ```sh
   poe test
   ```

And that's it! You should now have the project running on your local machine.
