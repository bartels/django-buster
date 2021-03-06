from setuptools import setup, find_packages

setup(
    name='django-buster',
    version='0.1.0',
    description='A simple utility for integrating gulp-buster with Django',
    author='Eric Bartels',
    author_email='ebartels@gmail.com',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
)
