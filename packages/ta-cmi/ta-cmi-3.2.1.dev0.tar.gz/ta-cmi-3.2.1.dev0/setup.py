from setuptools import setup

with open("README.md", "r", encoding="utf8") as f:
    readme = f.read()

with open("LICENSE", "r", encoding="utf8") as f:
    license = f.read()

setup(
    name="ta-cmi",
    version="3.2.1dev",
    description="A Python wrapper to read out sensors from Technische Alternative using the C.M.I.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/DeerMaximum/ta-cmi",
    author="DeerMaximum",
    author_email="2629822-DeerMaximum@users.noreply.gitlab.com",
    license=license,
    packages=["ta_cmi"],
    install_requires=["aiohttp>=3.9.3", "packaging>=24.0"],
)
