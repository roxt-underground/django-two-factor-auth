from setuptools import find_packages, setup

setup(
    name='django-two-factor-auth',
    version='1.8.0',
    description='Complete Two-Factor Authentication for Django',
    long_description=open('README.rst').read(),
    author='Bouke Haarsma',
    author_email='bouke@haarsma.eu',
    url='https://github.com/MyBook/django-two-factor-auth',
    license='MIT',
    packages=find_packages(exclude=('example', 'tests')),
    install_requires=[
        'Django>=1.11',
        'django_otp>=0.3.4,<0.99',
        'qrcode>=4.0.0,<6.99',
        'django-phonenumber-field>=1.1.0,<2.3',
        'django-formtools',
    ],
    extras_require={
        'Call': ['twilio>=6.0'],
        'SMS': ['twilio>=6.0'],
        'YubiKey': ['django-otp-yubikey'],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
    ],
)
