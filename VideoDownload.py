from pytube import YouTube
import os


def download_video(url, output_path="."):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Create the "TopVideo" folder if it doesn't exist
        output_folder = os.path.join(output_path, "TopVideo")
        os.makedirs(output_folder, exist_ok=True)

        # Download the video to the "TopVideo" folder
        video_stream.download(output_folder)

        print(f"Download completed successfully for {yt.title}!")

    except Exception as e:
        print(f"An error occurred for {url}: {str(e)}")


# Read URLs from playlist_urls.txt and download each video to the "TopVideo" folder
with open("playlist_urls.txt", "r") as file:
    urls = file.readlines()

for url in urls:
    # Remove any leading or trailing whitespace
    url = url.strip()

    # Check if the line is not empty
    if url:
        # Assume that the URL is complete, otherwise, modify as needed
        video_url = "https://www.youtube.com/watch?v=" + url
        download_video(video_url, output_path=".")
