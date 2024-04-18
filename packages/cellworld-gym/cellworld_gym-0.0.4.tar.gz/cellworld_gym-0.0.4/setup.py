from setuptools import setup

setup(name='cellworld_gym',
      author='German Espinosa',
      author_email='germanespinosa@gmail.com',
      long_description=open('./cellworld_gym/README.md').read(),
      long_description_content_type='text/markdown',
      packages=['cellworld_gym'],
      install_requires=['cellworld_game', 'gym'],
      include_package_data=True,
      version='0.0.4',
      zip_safe=False)
