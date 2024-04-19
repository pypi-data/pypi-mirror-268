from setuptools import setup, find_packages

setup(
    name='mzemail',
    version='0.1.1',
    author='Zardin Nicolo',
    description='A simple email package for Python. It provides a simple way to send emails using SMTP and SendGrid.',
    packages=find_packages(exclude=['tests*', 'tests']),
    install_requires=[
        'secure-smtplib',
        'sendgrid',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
