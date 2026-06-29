import time
import os

lyrics = [
    ("✨ yeah, i miss you", 3.5),
    ("🥀 you know it's true", 4.2),
    ("📞 so what if i call,", 4.3),
    ("📱 and you pick up the phone?", 4.0),
    ("❄️ and i use this holiday", 3.5),
    ("🕊️ to make my way to your ghost", 6.5),
    ("🌧️ oh, what if you're lonely", 4.0),
    ("🖤 and you know i am too?", 4.0),
    ("⌛ and i get the chance to say", 4.0),
    ("🎄 merry christmas, i miss you", 6.0),
    ("💔 i miss you.", 3.5)
]

for text, delay in lyrics:
    os.system('cls')
    
    print("\n" * 6)
    print(f"{text}".center(60))
    print("\n" * 6)
        
    time.sleep(delay)
  
# Warning, Credit My tiktok if u use my code for content
#tiktok :
# @nullthemanwhocantbemoved
# @marz_official11

#github :
# @NulllNotDev
