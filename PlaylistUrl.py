import youtube_dl


def get_playlist_urls(playlist_url):
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(playlist_url, download=False)
        if "entries" in result:
            return [entry["url"] for entry in result["entries"]]
        else:
            return []


# Replace 'YOUR_PLAYLIST_URL' with the actual URL of the YouTube playlist
playlist_url = (
    "https://www.youtube.com/playlist?list=PL86SiVwkw_oeZZp9j14U5F-BIVIAUI6Lb"
)
output_file_path = "playlist_urls.txt"

urls = get_playlist_urls(playlist_url)

with open(output_file_path, "w") as file:
    for url in urls:
        file.write(url + "\n")

print(f"URLs saved to {output_file_path}")
