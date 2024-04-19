from setuptools import setup, find_packages

setup(
    name='nbnlp',
    version="2.0.0",
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
    package_data={
        'nbnlp': ['data/*', 'model/*'],
    },
    install_requires=[
        # 'mysql-connector-python',
        # 'hanlp',
        # 'Flask',
        # 'APScheduler',
        # 'requests'
    ]
)
