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
requirements = python3,kivy,vlc,ftplib,webbrowser

# (list) Permissions (Android specific)
android.permissions = INTERNET

# (list) Supported platforms
platforms = android

# (list) Build target (default is 'apk', can be 'aab' or 'apk')
android.build_target = apk

# (list) Android API version
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 22b

# (list) Android application ID
android.package = com.example.audioplayerapp

# (list) Path to your custom icon (uncomment and specify if needed)
# android.icon = path/to/icon.png

# (list) Path to your custom splash screen (uncomment and specify if needed)
# android.splash = path/to/splash.png

# (list) Path to your custom settings screen (uncomment and specify if needed)
# android.settings = path/to/settings.png

# (list) Add any additional options here
# e.g. versioning, signing, etc.
# Note: If your application uses additional libraries or tools, you may need to include them here.

# (list) Android extra libraries (e.g. for additional features)
# android.libs = path/to/libs

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
