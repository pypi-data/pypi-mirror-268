from setuptools import setup, find_packages

setup(
    name='libraryfine',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='A simple Django app to manage books fines',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Chinmay',
    author_email='lawd7131@gmail.com',
    license='MIT',
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 3.2',  # Specify your Django version
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'Django>=3.2',  # Ensure compatibility with your Django version
    ],
    url='http://github.com/yourusername/my_library_app',
)
