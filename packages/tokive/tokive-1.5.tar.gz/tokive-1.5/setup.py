import setuptools

setuptools.setup(
    name='tokive',
    version='1.5',
    author="Thanh Hoa",
    author_email="thanhhoakhmt1@gmail.com",
    description="A Des of tokive",
    long_description="Des",
    long_description_content_type="text/markdown",
    url="https://github.com/AutoWinTeam/tokive",
    packages=setuptools.find_packages(),
    scripts=['tokive'],
    py_modules=['tokhelper'],
    package_data={
        'tokive': ['data/*.proto'],
    },
    install_requires=[
        'cryptography','requests', 'opencv-python', 'protobuf','numpy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )