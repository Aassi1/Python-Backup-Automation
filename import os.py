import os
import shutil
import datetime
import schedule
import time

source_dir = "C:\Users\Assi\Pictures\CameraRoll"
destination_dir = "C:\Users\Assi\Pictures\chimieprojet12"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    destination_dir = os.path.join(dest,str(today))
    
    try:
        shutil.copytree(source,destination_dir)
        print(f"folder copied to : {destination_dir}")
    except FileExistsError:
        print(f"folder already exists in : {dest}")

schedule.every.day.at("11:00").do(lambda:copy_folder_to_directory(source_dir,destination_dir))

copy_folder_to_directory(source_dir,destination_dir)

while True:
    schedule.run_pending()
    time.sleep(60)

