from setuptools import setup

setup(
    name='loadcalculation',
    version='0.1',
    packages=["loadcalculation"],
    package_data={"loadcalculation": ["*.pyd"]},
    install_requires=[
        'pyqt5',
        'wmi',
        'xlrd',
        'numpy',
        'pywin32',
        'pyautogui',
        'datetime',
    ],
    author='None',
    author_email='None@gmail.com',
    description='Your package description',
    license='MIT',
)

#  terminal run
#  python package_switch.py sdist bdist_wheel
