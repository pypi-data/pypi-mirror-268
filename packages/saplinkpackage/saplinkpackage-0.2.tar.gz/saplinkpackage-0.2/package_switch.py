from setuptools import setup

setup(
    name='saplinkpackage',
    version='0.2',
    packages=["saplinkpackage"],
    package_data={"saplinkpackage": ["*.pyd"]},
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

pypi-AgEIcHlwaS5vcmcCJGQwYjMwY2NmLTA3NDgtNGM5ZC1hYmM1LWRlZThiNGFlODkyZAACKlszLCJiZTA4ZTg5Mi02NmI5LTQ3YWItOGNiNC0xZGE4NmRlNjI2ZTQiXQAABiAaDeyXp8HC8z9CTu2LGf9KRMgQsB2PkVHxR3qSCdyVWw
