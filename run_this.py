import os
from moviepy.editor import *
from moviepy.video.fx.all import crop

# Get the system user's directory
user_directory = os.path.expanduser("~")

# Load the two videos
video1 = VideoFileClip(os.path.join(user_directory, "Desktop/tiktok Splitter/Tiktok Video/t.mp4"))
video2 = VideoFileClip(os.path.join(user_directory, "Desktop/tiktok Splitter/gameplay Videos/video1.mp4"))
(w, h) = video1.size
if w > h:
    # The video is landscape
    crop_size = h
    x1, y1 = (w - crop_size) // 2, 0
else:
    # The video is portrait or square
    crop_size = w
    x1, y1 = 0, (h - crop_size) // 2
x2, y2 = x1 + crop_size, y1 + crop_size
bg_video = crop(video1, width=crop_size, height=crop_size, x_center=w/2, y_center=h/2)
bg_video = bg_video.resize((1080, 960))
(w, h) = video2.size
if w > h:
    # The video is landscape
    crop_size = h
    x1, y1 = (w - crop_size) // 2, 0
else:
    # The video is portrait or square
    crop_size = w
    x1, y1 = 0, (h - crop_size) // 2
x2, y2 = x1 + crop_size, y1 + crop_size
bg_video2 = crop(video2, width=crop_size, height=crop_size, x1=x1, y1=y1, x2=x2, y2=y2)
bg_video2 = bg_video2.resize((1080, 960))
bg_video2 = bg_video2.set_duration(bg_video.duration)
# Resize the videos to fit TikTok's resolution
# Set the position of the videos in the final video
video1_pos = (0,0)
video2_pos = (0,960)
# Create the final video by concatenating the two videos
final_video = CompositeVideoClip([bg_video.set_pos(video1_pos), 
                                  bg_video2.set_pos(video2_pos)], 
                                  size=(1080  , 1920))

# Write the final video to disk
final_video.write_videofile("split_screen_video.mp4", fps=30)