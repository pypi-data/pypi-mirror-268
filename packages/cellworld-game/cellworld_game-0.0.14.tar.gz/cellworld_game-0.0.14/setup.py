from setuptools import setup

setup(name='cellworld_game',
      author='German Espinosa',
      author_email='germanespinosa@gmail.com',
      long_description=open('./cellworld_game/README.md').read(),
      long_description_content_type='text/markdown',
      packages=['cellworld_game'],
      install_requires=['cellworld'],
      include_package_data=True,
      version='0.0.14',
      zip_safe=False)
