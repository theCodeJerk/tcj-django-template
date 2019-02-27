# Django Template

## Overview

I created this as a template for creating new Djano projects.

Please see the README.init.md file for information about the
author, and setup details, of the original github repository
that I started with when building this template.

I needed a time saving template to be able to quickly start
a new website without having to constantly re-do some of the
most frequent operations.

1. Login/Registration System
	* Complete with OAuth for common providers
2. Private, repository independent settings.
3. Bootstrap
4. SASS
5. SSL Ready
6. Static files
7. Complete .gitignore

## Future Updates
I'd like to change this a little so that provider services aren't
so dependent on the settings file, instead using only the database
to store their information.  Allowing the optional use of the 
settings file to provide the values (which would only put them in
the database and still wouldn't be dependent on setting them here.
This would still allow using the configure.py script to set providers,
maybe a little better even.

I'd also like to use the database to store email server fields for
the admin to use, as well as being able to set them in prompts with
the configure.py script, the way the providers are set using the 
configure.py script. 

There seems to be a problem when no social networks are setup for a
user and they click the social networks link in their profile dropdown
menu.  I'm not sure if this only happens when there are no providers
setup in settings.py or if this happens just because the user doesn't
have any setup.  Need to find out, because if it is just because there
aren't any in the settings.py file, then we can fix this by making the
link not show in that case.  If it happens when providers are installed
but the user just hasn't linked any accounts, then we've a bigger problem.
