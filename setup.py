"""pyramid_mongodb installation script.
"""
import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README")).read()
README = README.split("\n\n", 1)[0] + "\n"

requires = [
    "pyramid",
    "pymongo",
    ]

entry_points = """
    [paste.paster_create_template]
    pyramid_mongodb = pyramid_mongodb.paster_templates:MongodbProjectTemplate
    [pyramid.scaffold]
    pyramid_mongodb = pyramid_mongodb.paster_templates:MongodbProjectTemplate
"""

setup(name="pyramid_mongodb",
      version="1.3",
      description="Pyramid application template for a traversal-based URL mapping and MongoDB project.",
      long_description=README,
      #long_description=README + "\n\n" +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pylons",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        ],
      keywords="web wsgi pylons pyramid mongodb",
      author="Niall O'Higgins",
      author_email="nialljohiggins@gmail.com",
      url="https://github.com/niallo/pyramid_mongodb",
      license="MIT",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require = requires,
      install_requires = requires,
      test_suite="pyramid_mongodb",
      entry_points=entry_points,
      )

