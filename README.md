
# Azure Blob File Server with FastAPI & CLI

This project is a file server implemented with **FastAPI** and **Azure Blob Storage**, offering endpoints to upload, download, list, and delete files. It also includes an interactive **CLI tool** to interact with the server.

---

## Features

- Upload, download, list, and delete files via REST API
- Store files in **Azure Blob Storage**
- Interactive command-line interface (CLI)
- Fully containerized using Docker & Docker Compose

---

## Project Structure

```
├── app/ # FastAPI backend (main.py, routes, crud, api tests)
├── cli/ # CLI tool (interactive shell)
├── tests/ # stress test
├── .env # Environment file (Azure connection string)
├── Dockerfile # Backend Dockerfile
├── Dockerfile.cli # CLI Dockerfile
├── docker-compose.yml # Compose file to run both services
├── requirements.txt # Python dependencies
└── README.md
```

---

## Environment Setup

Create a `.env` file at the root:
* prerequisite: create an AZURE storage account and a container for file storage. (doc: https://learn.microsoft.com/zh-tw/azure/storage/common/storage-account-create?tabs=azure-portal)

```env
AZURE_STORAGE_CONNECTION_STRING=your-azure-connection-string
AZURE_CONTAINER_NAME=your_container_name
FILE_SERVER_URL=http://file-server:8000/attachments
```
* The FILE_SERVER_URL is used by the CLI inside Docker. If you run the CLI locally, set it to `http://localhost:8000/attachments`.

## Docker: Build & Run

Build Everything: `docker-compose up --build`

This will:

* Build and run the FastAPI server on http://localhost:8000
* Launch the interactive CLI in the same terminal

## Using the CLI

### Command
```
upload <file_path>: Upload a file to the server.
download <file_name>: Download a file from the server. • list: List all files stored on the server.
delete <file_name>: Delete a file from the server.
help: List the avaliable commands.
exit: Exit the current interface.
```


### CLI in Docker 
After running `docker-compose up`, attach the cli container shell and run `python -m cli.main` in the container 
Example commands:
```
(file-server) upload sample.txt
(file-server) list
(file-server) download sample.txt
(file-server) delete sample.txt
(file-server) exit
```
### CLI Locally
After the server is running, run `python -m cli.main`


## Tests

* `app/tests`: file server unit tests, run `pytest app/tests` in `file_server/` directory.
* `tests`: stress test with Locust, run `locust` in `file_server/tests/` directory.