[app]
# (list) Title of your application
title = AudioPlayerApp

# (list) Package name
package.name = audioplayerapp

# (list) Package domain (usually a reverse domain, e.g. org.example)
package.domain = org.example

# (list) Source files to include (by default, everything in the directory is included)
source.include_exts = py,png,jpg,kv,atlas

# (string) Directory where source files are located
source.dir = .

# (list) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy,vlc,ftplib,webbrowser,cython

# (list) Permissions (Android specific)
android.permissions = INTERNET

# (list) Supported platforms
platforms = android

# (list) Build target (default is 'apk', can be 'aab' or 'apk')
android.build_target = apk

# (list) Android API version
android.api = 30
android.minapi = 21
android.ndk = 22b

# (list) Android application ID
android.package = com.example.audioplayerapp

# (list) Path to your custom icon (uncomment and specify if needed)
# android.icon = path/to/icon.png

# (list) Path to your custom splash screen (uncomment and specify if needed)
# android.splash = path/to/splash.png

# (list) Path to your custom settings screen (uncomment and specify if needed)
# android.settings = path/to/settings.png
