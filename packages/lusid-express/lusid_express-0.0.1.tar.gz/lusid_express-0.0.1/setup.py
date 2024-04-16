from setuptools import setup, find_packages


# List of requirements
requirements = [
    'pyyaml',
    'luminesce-sdk-preview==1.14.758',
    'lusid-jam==0.1.2',
    'lusid-sdk-preview==1.1.120',
    'fbnlab-preview==0.1.108',
    'finbourne-access-sdk==0.0.3751',
    'finbourne-identity-sdk==0.0.2834',
    'finbourne-insights-sdk-preview==0.0.763',
    'finbourne-sdk-utilities==0.0.10',
    'lusid-configuration-sdk-preview==0.1.514',
    'lusid-drive-sdk-preview==0.1.617',
    'lusid-notifications-sdk-preview==0.1.923',
    'lusid-scheduler-sdk-preview==0.0.829',
    'lusid-workflow-sdk-preview==0.1.810',
    'lusidtools==1.0.14',
    'dve-lumipy-preview==0.1.1075'
]




setup(
    name='lusid_express',
    version='0.0.1',
    packages=find_packages(),
    install_requires=requirements,
    description='lusid-express is a python package that makes it quick and easy to get started using Lusid and Luminesce.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Orlando Calvo',
    author_email='orlando.calvo@finbourne.com',
    url='https://gitlab.com/orlando.calvo1/lusid-express',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)