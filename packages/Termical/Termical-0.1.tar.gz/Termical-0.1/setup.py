from setuptools import setup 
  
setup( 
    name='Termical', 
    version='0.1', 
    description='Simple terminal-based calendar', 
    author='Marek Kužel', 
    author_email='marekuzel1@gmail.com', 
    #packages=['termical'], 
    install_requires=[ 
         "google-api-python-client",
         "google-auth-httplib2",
         "google-auth-oauthlib"
         "pytz"
    ], 
) 
