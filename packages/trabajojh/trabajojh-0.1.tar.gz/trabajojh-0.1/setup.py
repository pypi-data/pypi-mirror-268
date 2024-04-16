from setuptools import setup

r = open("./README.md", "r")

setup(
    name= 'trabajojh',
    packages= ['trabajojh'],
    version= '0.1',
    description= 'Trabajo en clases',
    long_description= r.read(),
    long_description_content_type= 'text/markdown',
    author= 'jheomarasollesgarcia',
    author_email= 'jheomaras@gmail.com',
    classifiers= [],
    license= 'MIT',
    include_package_data= True
)