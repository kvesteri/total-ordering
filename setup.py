"""
total_ordering
--------------

functools.total_ordering backport for Python 2.6
"""

from setuptools import setup, Command
import subprocess


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call(['py.test'])
        raise SystemExit(errno)


extras_require = {
    'test': [
        'pytest>=2.2.3',
    ],
}


setup(
    name='total-ordering',
    version='0.1.0',
    url='https://github.com/kvesteri/total-ordering',
    license='BSD',
    author='Konsta Vesterinen',
    author_email='konsta@fastmonkeys.com',
    description='functools.total_ordering backport for Python 2.6',
    long_description=__doc__,
    py_modules=['total_ordering'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[],
    extras_require=extras_require,
    cmdclass={'test': PyTest},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
