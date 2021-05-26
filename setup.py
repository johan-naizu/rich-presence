from setuptools import setup

APP = ['presence.py']
DATA_FILES = ['icon.icns']
OPTIONS = {
 'iconfile':'icon.icns',
    'packages':['certifi','rumps'],
 'plist': {
        'CFBundleName': 'Johan Naizu',
        'CFBundleDisplayName': 'Johan Naizu',
        'CFBundleGetInfoString': "Johan Naizu",

        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Copyright © 2021, Johan Naizu, All Rights Reserved"
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
