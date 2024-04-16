from setuptools import setup

r = open("./README.md", "r")

setup(

    name= 'proyectojhanel',
    packages= ['proyecto'],
    version= '0.1',
    description= 'Trabajo de modulos',
    long_description= r.read(),
    long_description_content_type= 'text/markdown',
    author= 'jhanelsollesgarcia',
    author_email= 'jhanelsollesgarcia2@gmail.com',
    classifiers= [],
    license= 'MIT',
    include_package_data= True
)