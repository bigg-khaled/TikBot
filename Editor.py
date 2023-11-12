from moviepy.editor import VideoFileClip, clips_array

i = 1

p = int(input("How many parts would you like the video to be divided into? "))

length = VideoFileClip("Videos/vid.mp4").duration

clip1 = VideoFileClip("Videos/vid.mp4").subclip(0, 0 + length)
clip2 = VideoFileClip("Videos/bg.mp4").subclip(0, 0 + length)

combined = clips_array([[clip1], [clip2]])
combined.write_videofile("temp.mp4")
full_video = "temp.mp4"

current_duration = VideoFileClip(full_video).duration

single_duration = current_duration / p
current_video = f"{current_duration}.mp4"

while current_duration >= single_duration:
    if p == 1:
        current_duration = single_duration
    clip = VideoFileClip(full_video).subclip(
        current_duration - single_duration, current_duration
    )
    current_duration -= single_duration
    if p == 2:
        current_duration = single_duration
    current_video = f"Part{p}.mp4"
    clip.to_videofile(
        current_video,
        codec="libx264",
        temp_audiofile="temp-audio.m4a",
        remove_temp=True,
        audio_codec="aac",
    )
    p -= 1

    print("-----------------###-----------------")
