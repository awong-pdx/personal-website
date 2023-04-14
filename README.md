### Personal Website
A repository for my personal website, refactored to use Django! The original site was a project for a web development class.

## Website:
[alessandralwong.com](https://www.alessandralwong.com)

## Setup
I used Visual Studio Code for MacOS when developing the site. Most of the setup follows the [Django tutorial](https://tutorial.djangogirls.org/en/) from DjangoGirls.
# Create A Virtual Environment
Before you begin, you might want to create a new virtual environment for this project.
`python3 -m venv nameofvirtualenvironment`
`source nameofvirtualenvironment/bin/activate`
# Install Requirements
`pip install --upgrade pip`
`pip install -r requirements`
# Migrate
`python manage.py migrate`
# Livereload
In separate terminals:
`python manage.py livereload`
`python manage.py runserver`
## Sources and Tutorials:
[Django Girls Tutorial](https://tutorial.djangogirls.org/en/)  
[Django Tutorial in VS Code](https://code.visualstudio.com/docs/python/tutorial-django)
