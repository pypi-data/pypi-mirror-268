from setuptools import setup, find_packages

setup(
    name='jiebanlp',
    version="2.1.0",
    packages=find_packages(),
    include_package_data=True,
    author="xl",
    author_email="123456@qq.com",
    description="A short description of your package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    # install_requires=[
    #     'jieba',
    #     'Flask',
    #     'APScheduler',
    #     'mysql-connector-python',
    # ]
)
