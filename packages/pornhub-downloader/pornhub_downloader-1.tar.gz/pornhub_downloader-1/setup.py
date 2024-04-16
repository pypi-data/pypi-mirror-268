import setuptools

des = open('./des.md').read()

setuptools.setup(
    name= 'pornhub-downloader',
    version= '1',
    author= 'm3ghos',
    description= 'This Package For Download Videoas From PornHub and Xnxx',
    long_description=des,
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: MIT License"
    ]
)