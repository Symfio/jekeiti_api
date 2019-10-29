__author__ = 'MuhBayu <bnugraha00@gmail.com>'
__version__ = '1.0.0'

packages = [
    'jekti_api',
    'jekti_api.endpoints',
]

setup(
    name='jekeiti_api',
    version=__version__,
    author='MuhBayu',
    author_email='bnugraha00@gmail.com',
    license='MIT',
    url='https://github.com/MuhBayu/jekeiti_api',
    install_requires=[],
    description='A client interface for the JKT48',
    packages=packages,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.7',
    ]
)