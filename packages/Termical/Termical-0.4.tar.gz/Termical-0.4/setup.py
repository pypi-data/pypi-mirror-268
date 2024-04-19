from setuptools import setup 
  
setup( 
    name='Termical', 
    version='0.4', 
    description='Simple terminal-based calendar', 
    author='Marek Kužel', 
    author_email='marekuzel1@gmail.com', 
    packages=['termical_lib'],
    entry_points = {
        "console_scripts": ['termical = termical_lib.termical:main']
        },
    install_requires=[ 
         "google-api-python-client",
         "google-auth-httplib2",
         "google-auth-oauthlib",
         "pytz"
    ], 
) 
