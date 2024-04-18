from setuptools import setup

setup(name='cellworld_gym',
      description='Experimental openAI gym environments for cellworld experimental setup',
      url='https://github.com/germanespinosa/cellworld_gym',
      author='German Espinosa',
      author_email='germanespinosa@gmail.com',
      long_description=open('./cellworld_gym/README.md').read(),
      long_description_content_type='text/markdown',
      packages=['cellworld_gym'],
      install_requires=['cellworld_game', 'gym'],
      license='MIT',
      include_package_data=True,
      version='0.0.7',
      zip_safe=False)
