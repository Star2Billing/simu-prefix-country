from setuptools import setup
import os

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('prefix_country'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[len('prefix_country')+1:] # Strip "dummyapp/" or "dummyapp\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(
    name='simu-prefix-country',
    version='0.1',
    description='Application providing Prefixes and Countries code',
    author='Belaid Arezqui',
    author_email='areski@gmail.com',
    packages=packages,
    package_dir={'prefix_country': 'prefix_country'},
    package_data={'prefix_country': data_files},
    entry_points={'django.apps': 'prefix_country = prefix_country'},
)
