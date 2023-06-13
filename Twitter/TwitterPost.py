import tweepy
import Twitter.TwitterKeys as TwitterKeys

def api():
    auth = tweepy.OAuthHandler(TwitterKeys.api_key, TwitterKeys.api_secret)
    auth.set_access_token(TwitterKeys.access_token, TwitterKeys.access_token_secret)

    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print("Tweeted successfully!")
