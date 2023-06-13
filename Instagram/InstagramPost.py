from instabot import Bot

def uploadToInsta(photoPath, postCaption, instaUsername, instaPassword):

    my_bot = Bot()

    my_bot.login(username= instaUsername, password= instaPassword)

    my_bot.upload_photo(photoPath, caption = postCaption)
