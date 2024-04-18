from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='sfmanager',
    version='0.0.7',
    author='GrandTheBest',
    author_email='grandinfo-cm@gmail.com',
    description='Super filemanager for python',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://t.me/grand_studios',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='tensor',
    project_urls={
        'GitHub': 'https://github.com/grandescobar/sfmanager'
    },
    python_requires='>=3.6'
    )
