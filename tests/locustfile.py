from locust import HttpUser, task, between
import uuid

class FileServerUser(HttpUser):
    wait_time = between(0.1, 0.5)

    # @task
    # def list_files(self):
    #     self.client.get("/list")

    # @task
    # def download_file(self):
    #     file_name = "cli/src/Touch Bar Shot.png"
    #     self.client.get("/download", params={"filename": file_name})

    # @task
    # def upload_file(self):
    #     file_path = "Touch Bar Shot.png"
    #     with open(file_path, "rb") as f:
    #         files = {"file": (file_path, f)}
    #         self.client.post("/upload", files=files)

    # @task
    # def delete_file(self):
    #     file_name = "cli/src/image.png"
    #     self.client.delete(f"/delete/{file_name}")

    @task
    def file_operation_cycle(self):
        # upload file
        unique_name = f"test_{uuid.uuid4().hex[:8]}.txt"
        file_content = b"Hello from Locust!"
        files = {"file": (unique_name, file_content)}
        upload_res = self.client.post("/upload", files=files)
        if upload_res.status_code != 200:
            print(f"Upload failed: {upload_res.text}")
            return

        # list files
        list_res = self.client.get("/list")
        if list_res.status_code == 200:
            file_list = list_res.json()
            if unique_name not in file_list:
                print(f"Uploaded file not in list: {unique_name}")

        # download file
        download_res = self.client.get("/download", params={"filename": unique_name})
        if download_res.status_code != 200:
            print(f"Download failed: {download_res.text}")

        # delete file
        delete_res = self.client.delete(f"/delete/{unique_name}")
        if delete_res.status_code != 200:
            print(f"Delete failed: {delete_res.text}")
