from tiktok_uploader.upload import upload_video
from tiktok_uploader.auth import AuthBackend
import os
import datetime

# Replace 'ResultClips', 'cookies.txt' with your actual values
video_folder = "ResultClips"
cookies_file = "cookies.txt"

# Get a list of video files in the folder
video_files = [f for f in os.listdir(video_folder) if f.endswith(".mp4")]

# Schedule uploads for 10 minutes from now
scheduled_time = datetime.datetime.now() + datetime.timedelta(minutes=20)

upload_video(
    "BottomVideo/bg.mp4", description="bg", cookies=cookies_file, browser="edge"
)

# # Iterate through each video file and upload using Chrome in headless mode
# for video_file in video_files:
#     video_path = os.path.join(video_folder, video_file)

#     # Get the description from the video file name
#     description = (
#         video_file.replace(".mp4", "").replace("_", " ")
#         + "\n "
#         + "#fyp #film #movie #tiktok #foryou #feelinggood"
#     )

#     # Upload the video using Chrome in headless mode and schedule it
#     upload_video(
#         video_path,
#         description=description,
#         cookies=cookies_file,
#         browser="edge",
#         # headless=True,
#         schedule=scheduled_time,
#     )

#     # Increment the scheduled time for the next upload
#     scheduled_time += datetime.timedelta(minutes=20)

#     # Delete the file after successful upload
#     # os.remove(video_path)
