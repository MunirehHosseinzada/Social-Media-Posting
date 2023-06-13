from Instagram.InstagramPost import uploadToInsta
import Twitter.TwitterPost as TwitterPost
from Tiktok.Tiktok_uploader import uploadVideo
from moviepy.editor import *

#----------- Variables

postCaption = "Test Post"
photoPath = "Sources/img.jpg"
tiktokSession_id = ""
videoPath = "Sources/my_video.mp4"
tags = ["Funny", "Joke", "fyp"]
instaUsername = ""
instaPassword = ""

#----------- Instagram

uploadToInsta(photoPath=photoPath, postCaption=postCaption, instaUsername=instaUsername, instaPassword=instaPassword)

#----------- Tweeter 

# api = TwitterPost.api()
# TwitterPost.tweet(api=api, message=postCaption)
    
#----------- Tiktok
video = VideoFileClip(videoPath)
bg_color = 'rgba(0,0,0,0.5)'
text = TextClip(postCaption, fontsize=50, color='white', bg_color=bg_color).set_pos('center')
video_with_text = CompositeVideoClip([video, text])
duration = video.duration
video_with_text.duration = duration
new_video_path = 'Sources/new_video.mp4'
video_with_text.write_videofile(new_video_path)

uploadVideo(tiktokSession_id, new_video_path, postCaption, tags, verbose=True)