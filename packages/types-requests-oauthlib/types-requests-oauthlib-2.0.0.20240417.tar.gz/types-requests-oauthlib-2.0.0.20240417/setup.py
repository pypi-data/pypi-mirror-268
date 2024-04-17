from setuptools import setup

name = "types-requests-oauthlib"
description = "Typing stubs for requests-oauthlib"
long_description = '''
## Typing stubs for requests-oauthlib

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`requests-oauthlib`](https://github.com/requests/requests-oauthlib) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`requests-oauthlib`.

This version of `types-requests-oauthlib` aims to provide accurate annotations
for `requests-oauthlib==2.0.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/requests-oauthlib. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `7d56cd9a6cf6e0a4ea89c68d0397e197aff32cbe` and was tested
with mypy 1.9.0, pyright 1.1.358, and
pytype 2024.4.11.
'''.lstrip()

setup(name=name,
      version="2.0.0.20240417",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/requests-oauthlib.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['types-oauthlib', 'types-requests'],
      packages=['requests_oauthlib-stubs'],
      package_data={'requests_oauthlib-stubs': ['__init__.pyi', 'compliance_fixes/__init__.pyi', 'compliance_fixes/douban.pyi', 'compliance_fixes/ebay.pyi', 'compliance_fixes/facebook.pyi', 'compliance_fixes/fitbit.pyi', 'compliance_fixes/instagram.pyi', 'compliance_fixes/mailchimp.pyi', 'compliance_fixes/plentymarkets.pyi', 'compliance_fixes/slack.pyi', 'compliance_fixes/weibo.pyi', 'oauth1_auth.pyi', 'oauth1_session.pyi', 'oauth2_auth.pyi', 'oauth2_session.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0 license",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
