## Version 1.0.1 (2024-04-16)
### 👷 Bug fixes

- stringify select options' values in vocabulary functions

### 📝 Documentation

- licence: update licence dates

## Version 1.0.0 (2023-08-03)
### 🎉 New features

- run flynt on the code base to convert everything into f-strings
- upgrade CubicWeb version to 4, and upgrade dependencies
  *BREAKING CHANGE*: upgrade CubicWeb version to 4, and upgrade dependencies

### 👷 Bug fixes

- recipients finder are now in services registry, no more components one

### 🤖 Continuous integration

- that tox option is now named allowlist_externals

## Version 0.21.0 (2023-01-10)
### 🎉 New features

- cubicweb-3.38: change all cubicweb.web/views to cubicweb_web cube
  *BREAKING CHANGE*: change all cubicweb.web/views to cubicweb_web cube
- run pyupgrade

### 🤖 Continuous integration

- gitlab-ci: use templates from a common repository

## Version 0.20.0 (2022-05-06)
### 🎉 New features

- minimum version of CW is not 3.43 and rdflib >= 6

## Version 0.19.0 (2022-05-05)
### 🎉 New features

- setup.py: increase cubicweb max version to 3.37.x

### 👷 Bug fixes

- force rdflib bellow version 6

### 🤖 Continuous integration

- gitlab-ci: use templates from a common repository

## Version 0.18.0 (2022-04-08)
### 🎉 New features

- setup.py: increase cubicweb max version to 3.36.x

## Version 0.17.0 (2022-04-05)
### 🎉 New features

- setup.py: increase cubicweb max version to 3.35.x

### 📝 Documentation

- licence: update licence dates

### 🤖 Continuous integration

- gitlab-ci: use templates from a common repository

## Version 0.16.1 (2021-06-23)
### 👷 Bug fixes

- remove upperbound on cubicweb


## Version 0.15.0 (2021-03-16)
### 🎉 New features

- setup.py: uses new format
- switch to cubicweb-seo>=0.3 to move to python3
- upgrade to CubicWeb 3.26 and pyramid
- make tests pass in python 3

### 👷 Bug fixes

- deprecated: renamed entity.set_attributes to entity.cw_set
- pkginfo: cube is not compatible with latest version of seo because of py3
- remove "_ = unicode"
- remove oldstyle tests
- tests: make objects order deterministic
- tests: use new format imports

### 📝 Documentation

- licence: update licence dates
- README: move to .rst extension

### 🤖 Continuous integration

- add basic tox.ini and .gitlab-ci.yml to launch tests
- run py3 tests in python 3.7

### 🤷 Various changes

- Add a .hgignore
- Indicate that Python 2.7 is now the minimum version
- Fix typo in purl dc URI
- Fix typo in RDFS URI
- pkg: 0.14.0
