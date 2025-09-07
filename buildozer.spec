[app]
title = CharlesBBQ
package.name = charlesbbq
package.domain = com.charles

# קבצי המקור בתיקייה הנוכחית
source.dir = .
source.include_exts = py,ttf,kv,png,jpg,html

version = 0.1
orientation = portrait
fullscreen = 0

# תלויות
requirements = python3,kivy,pyjnius,android

# גרסאות אנדרואיד
android.api = 33
android.minapi = 21

# ארכיטקטורה (לבנייה ראשונה נשתמש בארמ32 – תואם לרוב המכשירים)
android.arch = armeabi-v7a
# (אחרי שזה יעבוד אפשר להוסיף גם arm64-v8a בשורת buildozer ולאחד)

# מצב Debug
android.debug = 1

# הרשאות בסיס
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
