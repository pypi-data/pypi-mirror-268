from setuptools import setup, find_packages

setup(
    name='yandex_music_utilities',
    version='1.0.0',
    author='Dmitry Polulyakh',
    author_email='dmitry_korj@icloud.com',
    description='This package allows you to download music asynchronously and check playlists for deleted music',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
