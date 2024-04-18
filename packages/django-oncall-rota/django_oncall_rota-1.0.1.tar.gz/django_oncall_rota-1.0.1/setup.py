from setuptools import setup, find_packages

setup(
    name='django-oncall-rota',
    version='1.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'asgiref==3.8.1',
        'Django==5.0.4',
        'django-filter==24.2',
        'sqlparse==0.5.0',
        'tzdata==2024.1',


        # Add any other dependencies here
    ],
    author='Adam Hughes',
    author_email='info@manaweb.io',
    description='A simple on call rota using Django',
    long_description=open('README.MD').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/adamlh/oncall',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        # Add any other relevant classifiers
    ],
)
