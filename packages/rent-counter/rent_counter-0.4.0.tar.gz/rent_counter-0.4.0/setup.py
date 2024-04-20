from setuptools import setup, find_packages

setup(
    name='rent_counter',
    version='0.4.0',
    py_modules=['countdown'],  # Include countdown.py as a module
    include_package_data=True,
    description='A Python library for managing rent expiration countdowns',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Erick Adikah',
    author_email='your.email@example.com',
    license='MIT',
    url='https://github.com/Erickadikah/count',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[],
)
