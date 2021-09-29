from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="wagtailcodeblock",
    description="Wagtail Code Block provides PrismJS syntax highlighting in Wagtail.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tim Allen",
    author_email="tallen@wharton.upenn.edu",
    url="https://github.com/FlipperPA/wagtailcodeblock",
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=["wagtail>=2.13",],
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
