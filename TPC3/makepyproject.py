import jinja2
from glob import glob
    
'''
DESCRIPTION
   This script uses jinja2 and glob as a way to make a template for a pyproject.toml file.
   Jinja2 is used for the template and variable substitution, while glob is used to find all the .py files in the current directory.
   With that, we are able to make pyprojects of the first file found, using the template below. 
 
RUN
   Run using this command: python3 makepyproject.py > pyproject.toml
   Then do: pip install .
   And run the script by calling the module name
   
NOTES   
   It is also important to mention that the dependencies, as well as the author and email need changing.
   And don't forget to only use this when you have a file.py in the directory and that file has __version__= x.y.z, or else I assume 1.0.0.
'''    

# Get list of Python files in the directory
python_files = glob("*.py")

# Determine project name based on the first Python file found or user input
if python_files:
    name = python_files[0].replace(".py", "")
else:
    name = input("Input Module Name: ")

# Determine version based on the presence of __version__ in the Python file
version = None
if python_files:
    with open(python_files[0]) as f:
        for line in f:
            if "__version__" in line:
                version = line.split("=")[1].strip().strip('"')
                break

# Prompt user for version if not found in the file
if version is None:
    line = "__version__ = 1.0.0"
    version = line.split("=")[1].strip().strip('"')


pp = jinja2.Template('''
                   
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "{{name}}"
authors = [
    {name = "{{autor}}", email = "{{email}}"},
]
classifiers = [
    "License :: OSI Approved :: MIT License",
]
requires-python = ">=3.8"
dynamic = ["version", "description"]

dependencies = [
    "FIXME"
]

[project.scripts]
{{name}} = "{{name}}:main"
                   
                   
''')

#FIX ME
print(pp.render({"name":name,"autor":"","email":""}))