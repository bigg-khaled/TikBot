from tiktok_uploader.upload import upload_video
from tiktok_uploader.auth import AuthBackend
import os
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Replace 'ResultClips', 'cookies.txt' with your actual values
video_folder = "ResultClips"
cookies_file = "cookies.txt"

# Get a list of video files in the folder
video_files = [f for f in os.listdir(video_folder) if f.endswith(".mp4")]

# Iterate through each video file and upload using Chrome in headless mode
for video_file in video_files:
    video_path = os.path.join(video_folder, video_file)

    # Get the description from the video file name
    description = (
        video_file.replace(".mp4", "").replace("_", " ")
        + "\n "
        + "#fyp #film #movie #tiktok #foryou #feelinggood"
    )

    # Upload the video using Chrome in headless mode and schedule it
    upload_video(
        video_path,
        description=description,
        cookies=cookies_file,
        browser="edge",
    )

    # Delete the file after successful upload
    # os.remove(video_path)
