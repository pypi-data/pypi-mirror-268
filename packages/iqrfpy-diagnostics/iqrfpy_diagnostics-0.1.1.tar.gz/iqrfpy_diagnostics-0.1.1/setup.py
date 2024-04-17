from __future__ import annotations
from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(
    name='iqrfpy-diagnostics',
    description='Diagnostics for iqrfpy',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.1',
    url='https://gitlab.iqrf.org/open-source/iqrf-sdk/iqrfpy/iqrfpy-diagnostics',
    author='Karel Hanák',
    author_email='karel.hanak@iqrf.org',
    license='Apache-2.0',
    keywords=['iqrf'],
    project_urls={
        'Homepage': 'https://gitlab.iqrf.org/open-source/iqrf-sdk/iqrfpy/iqrfpy-diagnostics',
        'Changelog': 'https://gitlab.iqrf.org/open-source/iqrf-sdk/iqrfpy/iqrfpy-diagnostics/-/blob/master/changelog.md',
        'Source code': 'https://gitlab.iqrf.org/open-source/iqrf-sdk/iqrfpy/iqrfpy-diagnostics',
        'Issue tracker': 'https://gitlab.iqrf.org/open-source/iqrf-sdk/iqrfpy/iqrfpy-diagnostics/-/issues',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
    packages=['iqrfpy.ext.diagnostics'],
    package_dir={
        'iqrfpy.ext.diagnostics': 'diagnostics'
    },
    package_data={
        'iqrfpy.ext.diagnostics': [
            'py.typed'
        ]
    },
    python_requires='>=3.10',
    install_requires=[
        'iqrfpy>=0.2.0',
        'tabulate>=0.9.0',
    ]
)
