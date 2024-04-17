from setuptools import setup 
  
setup( 
    name='Termical', 
    version='0.2', 
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
