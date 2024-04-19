from setuptools import setup 
  
setup( 
    name='Termical', 
    version='0.3', 
    description='Simple terminal-based calendar', 
    author='Marek Kužel', 
    author_email='marekuzel1@gmail.com', 
    packages=['termical_lib'], 
    install_requires=[ 
         "google-api-python-client",
         "google-auth-httplib2",
         "google-auth-oauthlib",
         "pytz"
    ], 
) 
