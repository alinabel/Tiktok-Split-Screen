# tiktok-Splitter
 This script allows you to create split screen TikTok videos by combining two separate video clips into one.

# How-To-Use
First, make sure you have MoviePy installed. If you don't, you can install it by running `!pip install moviepy`.

Next, put your two videos in your system user's Desctop. One should be a TikTok video, and the other should be a gameplay video.

tiktok Splitter/Tiktok Video/t.mp4 -  tiktok video
tiktok Splitter/gameplay Videos/video1.mp4 - Gameplay or whatever video 

Once you have your videos ready, open up the code and update the file paths to point to your videos. You'll find these variables near the beginning of the code:

```
video1 = VideoFileClip(os.path.join(user_directory, "Desktop/tiktok Splitter/Tiktok Video/t.mp4"))
video2 = VideoFileClip(os.path.join(user_directory, "Desktop/tiktok Splitter/gameplay Videos/video1.mp4"))
```

Make sure the file paths match the locations of your videos.

You can also adjust the position and size of the videos in the final output by updating the `video1_pos` and `video2_pos` variables.

Once you're ready, run the code run_this.py and wait for the output video to be generated. It will be saved as `split_screen_video.mp4` in the same directory as the code.

Thats it, enjoy.
