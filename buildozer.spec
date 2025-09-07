[app]
title = CharlesBBQ
package.name = charlesbbq
package.domain = com.charles
source.dir = .
source.include_exts = py,ttf,kv,png,jpg,html
version = 0.1
orientation = portrait
fullscreen = 0
requirements = python3,kivy,pyjnius,android
android.api = 33
android.minapi = 21
android.arch = arm64-v8a
android.debug = 1
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
