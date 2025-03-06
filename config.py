# Don't Remove Credit Tg - @Zuyc_tg
# Subscribe Telegram Channel For Amazing Bot https://t.me/+9yL5kNBFRyZhOWI1
# Ask Doubt on telegram @Zuyc_tg


import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
      
# Bot Information
API_ID = int(environ.get("API_ID", "27102419"))
API_HASH = environ.get("API_HASH", "acfe18a4b529e19f51cc488f694cd33b")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

PICS = (environ.get('PICS', 'https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22IMG_20250306_185642_979.jpg%22%2C%22type%22%3A%22image%2Fjpeg%22%2C%22signedurl_expire%22%3A%222028-03-05T13%3A28%3A48.325Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F%2Fe136721881c04419%2FIMG_20250306_185642_979.jpg%3FExpires%3D1835875728%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DYLccvUWxe9TGheyzlLb1l2wG53JHA3qslYps7fu~x-ox99T9v-cPfgsQwdHNzfcpt1W3uCULMgwXZmBGwmkvAp1htOUzMdXF1duWkLl7TRffINaFsEpsVY39ipZVHD~01qxOKayFTloIa4Co7yoBtUaf1SC-KbhTPMF~mVuYHjyLtD-B~2cEFInxdro1ZY~riFlH8DAokOuYbuzM2HU9gYOMfDetnFLXm-zSR-x8UA2Yej-OFBtbSnedSwc51675iYyVMMNMM7zGtaTNx1W6hGITMs10DQdVR2J~lbC2jMurS6JByD8DoxZn0XSOBsLq9j9Qr6wUtfbGTFWwgzPT5Q__%22%7D')).split() # Bot Start Picture
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '8157903366').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "Suzeeebot") # without @
PORT = environ.get("PORT", "8080")

# Clone Info :-
CLONE_MODE = bool(environ.get('CLONE_MODE', False)) # Set True or False

# If Clone Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
CLONE_DB_URI = environ.get("CLONE_DB_URI", "")
CDB_NAME = environ.get("CDB_NAME", "clonetechvj")

# Database Information
DB_URI = environ.get("DB_URI", "mongodb+srv://mikeykun0087:wRV48P27VLKrxs8O@cluster0.l6ijh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "techvjbotz")

# Auto Delete Information
AUTO_DELETE_MODE = bool(environ.get('AUTO_DELETE_MODE', True)) # Set True or False

# If Auto Delete Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002462615555"))

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Verify Info :-
VERIFY_MODE = bool(environ.get('VERIFY_MODE', True)) # Set True or False

# If Verify Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
SHORTLINK_URL = environ.get("SHORTLINK_URL", "smallshorts.com") # shortlink domain without https://
SHORTLINK_API = environ.get("SHORTLINK_API", "2bcba7086cdb75b069aef9311aab39639477eeee") # shortlink api
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/tutorial_7383/2") # how to open link 

# Website Info:
WEBSITE_URL_MODE = bool(environ.get('WEBSITE_URL_MODE', True)) # Set True or False

# If Website Url Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
WEBSITE_URL = environ.get("WEBSITE_URL", "https://anonymous7772.blogspot.com/2025/03/suzee.html") # For More Information Check Video On Yt - @Tech_VJ

# File Stream Config
STREAM_MODE = bool(environ.get('STREAM_MODE', False)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://testofvjfilter-1fa60b1b8498.herokuapp.com/")


# Don't Remove Credit Tg - @Zuyc_tg
# Subscribe Telegram Channel For Amazing Bot https://t.me/+9yL5kNBFRyZhOWI1
# Ask Doubt on telegram @Zuyc_tg
    
