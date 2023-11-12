from pytube import YouTube


def download_video(url, output_path="."):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Download the video to the specified output path
        video_stream.download(output_path)

        print("Download completed successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Example usage
video_url = "https://www.youtube.com/watch?v=5KnSKS9S0AQ"
download_video(video_url)
