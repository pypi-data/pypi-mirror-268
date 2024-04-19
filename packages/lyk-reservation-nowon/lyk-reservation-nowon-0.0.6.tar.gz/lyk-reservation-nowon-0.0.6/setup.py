from setuptools import setup, find_packages

setup(
    name='lyk-reservation-nowon',
    version='0.0.6',
    description='lyk-reservation-nowon',
    author='officeyongki',
    author_email='officeyongki@gmail.com',
    install_requires=['pyperclip', 'selenium', 'webdriver_manager'],
    packages=find_packages(include=['reservation', 'reservation.*']),
    keywords=['reservation', 'lyk', 'pypi'],
    python_requires='>=3.10',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)