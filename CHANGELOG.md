# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Support for Django 3.x.

### Changed
- Pinned the `django-parler` version to `>=2` and add a migration required to upgrade it.

### Fixed
- Add a `tzinfo` to `Street` and `Address.modified_at` migrations to fix the warning 
saying that a timezone-naive date was passed to a `DateTimeField`.
- helsinki importer: Reverted the change introduced in v0.3.6 which broke Helsinki division import
- helsinki importer: Fixed empty field value handling
- helsinki importer: Fixed crash with division types without a layer


## [0.3.6] - 2020-05-08

### Fixed
- helsinki importer: Raised the tolerance for divisions extending past their
  parents (from 1e-6 to 300 m^2). Helsinki data could not be imported previously.

[unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.3.6...HEAD
[0.3.6]: https://github.com/City-of-Helsinki/django-munigeo/compare/v0.3.5...v0.3.6
