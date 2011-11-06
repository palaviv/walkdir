from distutils.core import setup

setup(
    name='iterwalk',
    version='0.1',
    py_modules=['iterwalk'],
    license='Simplified BSD License',
    description='Iterator tools to manipulate and filter os.walk() output',
    long_description=open('README.txt').read(),
    author='Nick Coghlan',
    author_email='ncoghlan@gmail.com'
)
