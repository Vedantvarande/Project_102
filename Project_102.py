import cv2
import dropbox
import time
import random
start_time = time.time()


def take_snapshot():
    number = random.randint(0, 100)
    # initializating cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        # read the frames while camera is on
        ret, frame = videoCaptureObject.read()

        img_name = "image"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("pic taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows


def upload_file(img_name):
    access_token = 'xRytBY4BPVoAAAAAAAAAAZKTHD4mBRXfWFdxF1eO709KCdvRkDEV8pYhgTuURLTr'
    file = img_name
    file_from = file
    file_to = "/testfolder"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,
                         mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)


main()
# take_snapshot()
