import subprocess
import pkg_resources

def install(package):
    subprocess.check_call(['python', '-m', 'pip', 'install', package])

def validate_package(package):
    required = { package }
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        install(package)

def validate_packages():
    validate_package('pygame')

validate_packages()