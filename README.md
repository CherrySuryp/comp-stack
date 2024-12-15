# Comp Stack
## Installation
### Docker
#### Prerequisites
Ensure you have the following installed on your system:
1. Docker (latest stable version recommended)
2. Docker Compose (compatible with the installed Docker version)

#### Steps to Deploy
1. **Clone the Repository**
Clone or download the project repository to your local machine.
``` bash
   git clone <repository_url>
   cd <repository_directory>
```
1. **Prepare the Data File**
Ensure you have your data file ready for the FastAPI application. By default, the configuration expects the file to be at `./sales_data.csv`.
If your data file is named differently or placed in another directory:
    - Place the file in the repository root and name it `sales_data.csv`.
    - Alternatively, mount it to the container during deployment using volumes (explained below).

2. **Review the `docker-compose.yml` Configuration**
The provided `docker-compose.yml` file is already configured to:
    - Use the `cherrysuryp/comp-stack` image.
    - Mount a local file (`./sales_data.csv`) to `/app/sales_data.csv` inside the container.
    - Expose port `8000` for accessing the FastAPI service.
If needed, you can modify the `docker-compose.yml` file to update paths or ports.

3. **Customize Environment Variables (if required)**
The service expects the data file to be located at `/app/sales_data.csv` inside the container. If your data file path differs, you need to override the `DATA_FILE_PATH` environment variable to ensure the application can locate your file.
**To override the environment variable**:
    1. Add the environment variable to the `docker-compose.yml` file under the `fastapi` service. Example:
``` yaml
        environment:
          - DATA_FILE_PATH=/custom/path/to/your_data_file.csv
```
1. Replace `/custom/path/to/your_data_file.csv` with the actual in-container file path.

1. **Run the Service**
Start the service with Docker Compose:
``` bash
   docker-compose up -d
```
- The `-d` flag runs the containers in detached mode.

1. **Access the Service**
Open your browser and navigate to `http://localhost:8000`.
If the service is running properly, the FastAPI application should be accessible.

#### Volumes Configuration for Data File
The application uses Docker volumes to mount the local data file into the container for easy access. By default, the file `./sales_data.csv` is mapped to `/app/sales_data.csv` inside the container using this configuration:
``` yaml
volumes:
  - ./sales_data.csv:/app/sales_data.csv
```
If your data file has:
- A **different name**: Update `./sales_data.csv` in the `docker-compose.yml` file to the correct file name. Example:
``` yaml
   volumes:
     - ./your_file.csv:/app/sales_data.csv
```
- **different directory**: Provide the full path to your file on the host machine. Example:
``` yaml
   volumes:
     - /absolute/path/to/your_file.csv:/app/sales_data.csv
```

#### Troubleshooting
- **File Not Found Error**: Ensure the `sales_data.csv` file is mounted properly using volumes and is accessible at the specified path in the container. Adjust the `DATA_FILE_PATH` variable if necessary.
- **Cannot Access Service at Port 8000**: Verify your firewall settings and ensure the port `8000` is not blocked or used by another process.
- **Restart Issues**: Since the container restarts automatically (`restart: always`), check the logs for debugging:
``` bash
   docker logs comp-stack-fastapi
```
