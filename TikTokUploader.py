from tiktok_uploader.upload import upload_video
from tiktok_uploader.auth import AuthBackend

# Replace 'video.mp4', 'description', and 'cookies.txt' with your actual values
video_path = "Videos/bg.mp4"
description = "This is my video description"
cookies_file = "cookies.txt"

# Upload the video
upload_video(
    "bg.mp4",
    description="this is my description",
    cookies="cookies.txt",
    browser="edge",
)
