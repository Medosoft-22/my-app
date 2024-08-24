[app]
# (list) Title of your application
title = AudioPlayerApp

# (list) Package name
package.name = audioplayerapp

# (list) Package domain (usually a reverse domain, e.g. org.example)
package.domain = org.example

# (list) Source files to include (by default, everything in the directory is included)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy,vlc,ftplib,webbrowser

# (list) Permissions (Android specific)
android.permissions = INTERNET

# (list) Supported platforms
# e.g. android, ios, windows, linux
platforms = android

# (list) Build target (default is 'apk', can be 'aab' or 'apk')
android.build_target = apk

# (list) Android API version
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 22b

# (list) Android application ID
# It must be a fully qualified package name, like com.example.app
android.package = com.example.audioplayerapp

# (list) Path to your custom icon
# Note: The icon should be a square PNG image (e.g. 512x512 pixels)
# android.icon = %(source.dir)s/icon.png

# (list) Path to your custom splash screen
# android.splash = %(source.dir)s/splash.png

# (list) Path to your custom settings screen
# android.settings = %(source.dir)s/settings.png

# (list) Add any additional options here
# e.g. versioning, signing, etc.
# Note: If your application uses additional libraries or tools, you may need to include them here.

# (list) Android extra libraries (e.g. for additional features)
# android.libs = <path_to_your_libs>

# (list) The application’s package, example: com.example.myapp
# This should be a fully qualified domain name
# android.package = com.example.myapp

# (list) Custom environment variables
# e.g. environment = VAR1=value1,VAR2=value2

[buildozer]
# (list) Buildozer version
# buildozer_version = stable

# (list) Log level (e.g. debug, info, warning, error)
# log_level = info

# (list) Directory to store build artifacts
# build_dir = /path/to/build/dir

# (list) Directory for custom build scripts
# custom_build_scripts = /path/to/scripts

# (list) Buildozer configuration file
# buildozer_config_file = buildozer.spec
