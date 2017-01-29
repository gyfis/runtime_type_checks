from setuptools import setup

setup(name='runtime_type_checks',
      version='0.1',
      description='Decorator for runtime type checking',
      long_description='By using the provided decorator, the parameter types and return value is checked at runtime',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language:: Python:: 3.6',
        'Topic :: Software Development :: Testing',
      ],
      keywords='python typing type check runtime',
      url='https://github.com/petrbel/runtime_type_checks',
      author='Petr Belohlavek, Tomas Hromada',
      author_email='me@petrbel.cz, gyfis@seznam.cz',
      license='MIT',
      packages=['runtime_type_checks'],
      include_package_data=True,
      zip_safe=False,
      test_suite='runtime_type_checks.tests')
