from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

def split_video(input_path, chunk_length=180):
    # Load the video
    video = VideoFileClip(input_path)
    video_duration = int(video.duration)
    
    # Create output directory if it doesn't exist
    output_dir = "output_chunks"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Calculate the number of chunks
    num_chunks = video_duration // chunk_length + (1 if video_duration % chunk_length > 0 else 0)

    for i in range(num_chunks):
        start_time = i * chunk_length
        end_time = min((i + 1) * chunk_length, video_duration)
        output_file = os.path.join(output_dir, f"chunk_{i + 1}.mp4")
        
        ffmpeg_extract_subclip(input_path, start_time, end_time, targetname=output_file)
        print(f"Created {output_file}")

if __name__ == "__main__":
    input_video_path = "your_video.mp4"
    split_video(input_video_path)
