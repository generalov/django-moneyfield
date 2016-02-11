from distutils.core import setup


DESCRIPTION="""
"""

setup(
    name="django-moneyfield",
    description="Django Money Model Field",
    long_description=DESCRIPTION,
    version="0.3.1",
    author="Carlos Palol",
    author_email="carlos.palol@awarepixel.com",
    url="https://github.com/carlospalol/django-moneyfield",
    packages=[
        'moneyfield'
    ],
    requires=[
        'django (>=1.5)',
        'money',
        'six',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
    ]
)
