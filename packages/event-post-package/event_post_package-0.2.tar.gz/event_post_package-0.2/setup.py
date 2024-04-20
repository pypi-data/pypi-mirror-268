from setuptools import setup, find_packages

setup(
    name='event_post_package',
    version='0.2',
    packages=find_packages(),
    package_data={'event_post_package': ['templates/user/*.html']},
    install_requires=[
        'Django',
    ],
)