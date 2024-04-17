# level: NONE
import nntplib
import ssl


s = nntplib.NNTP("news.gmane.io")
s.starttls(context=ssl.create_default_context())
s.login("user", "password")
f = open("article.txt", "rb")
s.post(f)
s.quit()
