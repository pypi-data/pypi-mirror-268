from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='django_tailwindcss_automated',
    description="Handles all setup and configuration automatically.",
    version='0.6',
    author='Jan Leander',
    packages=find_packages(),
    install_requires=[
        # add dependencies here.
        # e.g 'num>=1.11.1'
    ],
    entry_points={
        "console_scripts": [
            "automate-django-tailwind = django_tailwindcss_automated:main",
        ],
    },
    long_description=description,
    long_description_content_type="text/markdown",
)
