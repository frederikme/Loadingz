from distutils.core import setup

setup(
  name='loadingz',         # How you named your loadingz folder (MyLib)
  packages=['loadingz'],   # Chose the same as "name"
  version='0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description='Tool for displaying loading processes',   # Give a short description about your library
  author='Frederik Mees',                   # Type in your name
  author_email='frederik.mees@gmail.com',      # Type in your E-Mail
  url='https://github.com/frederikme/Loadingbar',   # Provide either the link to your github or to your website
  download_url='https://github.com/frederikme/Loadingbar/archive/v_02.tar.gz',    # I explain this later on
  keywords=['Loading', 'Process', 'Display'],   # Keywords that define your loadingz best
  install_requires=[],            # I get to this in a second

  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your loadingz
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
