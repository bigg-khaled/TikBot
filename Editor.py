import os
from moviepy.editor import VideoFileClip, clips_array
from moviepy.video import fx as vfx

# Input folders containing video clips
input_folder1 = "TopVideo"
input_folder2 = "BottomVideo"
# Output folder for result clips
output_folder = "ResultClips"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get a list of all video files in the first input folder
video_files1 = [
    f for f in os.listdir(input_folder1) if f.endswith((".mp4", ".avi", ".mkv"))
]

# Loop over each video file in the first folder
for video_file1 in video_files1:
    # Get the full path of the input video file in the first folder
    input_video_path1 = os.path.join(input_folder1, video_file1)

    # Get the user input for the number of parts to divide the video into
    p = int(input(f"How many parts would you like {video_file1} to be divided into? "))

    # Get the duration of the input video file in the first folder
    length1 = VideoFileClip(input_video_path1).duration

    # Create the video clip for the current input file in the first folder
    clip1 = VideoFileClip(input_video_path1).subclip(0, 0 + length1)

    # Get the list of all video files in the second input folder
    video_files2 = [
        f for f in os.listdir(input_folder2) if f.endswith((".mp4", ".avi", ".mkv"))
    ]

    # Loop over each video file in the second folder
    for video_file2 in video_files2:
        # Get the full path of the input video file in the second folder
        input_video_path2 = os.path.join(input_folder2, video_file2)

        # Get the duration of the input video file in the second folder
        length2 = VideoFileClip(input_video_path2).duration

        # Create the video clip for the current input file in the second folder
        clip2 = VideoFileClip(input_video_path2).subclip(0, 0 + length2)

        # get the number of times clip2 should be repeated to match the length of clip1
        n = int(length1 / length2) + 1

        # make clip2 loop with duration of clip1
        clip2 = vfx.all.loop(clip2, duration=length1)

        # Mute the audio of clip2
        clip2 = clip2.set_audio(None)

        # Combine clips1 and clip2 into a single video array
        combined = clips_array([[clip1], [clip2]])

        # Write the combined clips to a temporary video file
        temp_output_path = os.path.join(output_folder, "temp.mp4")
        combined.write_videofile(temp_output_path)

        current_duration = VideoFileClip(temp_output_path).duration
        single_duration = current_duration / p

        # Loop to create separate video files for each part
        for part_number in range(1, p + 1):
            clip = VideoFileClip(temp_output_path).subclip(
                current_duration - single_duration, current_duration
            )

            current_video = f"{video_file1.replace('.', f'_Part{part_number}.')}"
            output_path = os.path.join(output_folder, current_video)

            # Write the subclip to the output file, specifying codec and audio settings
            clip.to_videofile(
                output_path,
                codec="libx264",
                temp_audiofile="temp-audio.m4a",
                remove_temp=True,
                audio_codec="aac",
            )

            print(f"Result saved to: {output_path}")
            print("-----------------###-----------------")

            current_duration -= single_duration
