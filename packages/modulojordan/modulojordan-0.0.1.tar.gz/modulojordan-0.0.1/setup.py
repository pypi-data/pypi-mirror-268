from setuptools import setup

r = open("./README.MD","r")

setup(
    name = "modulojordan",
    packages = ["modulojordan"],
    version = "0.0.1",
    description = "esta es la descripcion de mi paquete",
    long_description = r.read(),
    long_description_content_type = "text/markdown",
    author = "jordan_sion",
    author_email = "yordansioncossiofuentes@gamil.com",
    license =  "MIT",
    include_package_data = True,
    classifiers = [],
) 