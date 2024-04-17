from setuptools import setup, find_packages

setup(
    name='django_tailwindcss_automated',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        # add dependencies here.
        # e.g 'num>=1.11.1'
    ],
    entry_points={
        "console_scripts": [
            "automate-django-tailwind = django_tailwindcss_automated:main",
        ],
    }
)
