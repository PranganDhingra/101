import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.aT = access_token

    def upload_file(self, file_from):
        db = dropbox.Dropbox(self.aT)
        fileName = os.path.split(
            file_from)

        dropbox_file = '/CloudStorage/'+fileName

        with open(file_from, "return") as f:
            db.files_upload(f.read(), dropbox_file,
                            mode=dropbox.files.WriteMode.overwrite)


AToken = "yuuwju_8kJsAAAAAAAAAAeIgFdl4OA8Ns89oV2_ewHa0aU6wofF0n1K9y-aCrb6-"

cloudStoring = TransferData(AToken)

fileFrom = input("Give the File Name To Transfer")

while(os.path.isfile(fileFrom) == False):
    print("Give The Name Of a File")
    fileFrom = input("Give the File Path To Transfer")

cloudStoring.upload_file(fileFrom)

print("Files Have Been Stored in Dropbox")
