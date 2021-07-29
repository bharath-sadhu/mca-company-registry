import os
import setuptools
from setuptools import setup
from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig

class register(register_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

class upload(upload_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

setup(
    name='mca-company-register',
    version='1.0.0',
    zip_safe=False,
    description='AE ops',
    url='https://github.nike.com/analytics-platform/ae-airflow-operators/',
    author='bharath sadhu',
    author_email='bharath.sadhu@cloudwick.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='Company Registry',
    packages=setuptools.find_packages(),
    include_package_data=True,
    setup_requires=['setuptools','pytest-runner'],
    install_requires=[
         'asgiref==3.4.1',
         'asyncio==3.4.3',
         'certifi==2021.5.30',
         'charset-normalizer==2.0.3',
         'click==8.0.1',
         'fastapi==0.67.0'
         'h11==0.12.0',
         'idna==3.2',
         'importlib-metadata==4.6.1',
         'prometheus-client==0.7.1',
         'pydantic==1.8.2',
         'pydash==5.0.2',
         'requests==2.26.0',
         'starlette==0.14.2',
         'starlette-prometheus==0.7.0',
         'typing-extensions==3.10.0.0',
         'urllib3==1.26.6',
         'uuid==1.30',
         'uvicorn==0.14.0',
         'zipp==3.5.0A'

    ],
    entry_points={
        'mca.register': [
            'CompanyRegister = companyregister:CompanyRegister'
        ]
    },
    cmdclass={
        'upload': upload
    }
)