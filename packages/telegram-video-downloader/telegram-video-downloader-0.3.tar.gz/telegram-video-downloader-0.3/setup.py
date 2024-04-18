from setuptools import setup, find_packages

setup(
    name='telegram-video-downloader',
    version='0.3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'quart',
        'telethon',
    ],
    author='David Grau Martínez',
    author_email='fe80grau@gmail.com',
    description='Command to download a video published on Telegram',
    keywords='telegram video download',
    entry_points={
        'console_scripts': [
            'telegram-video-downloader=telegram_video_downloader.main:main',
        ],
    },
)
