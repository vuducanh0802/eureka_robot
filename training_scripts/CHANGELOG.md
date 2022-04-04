# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.2.0 - Unreleased

### Added
* Package and install via APT; docker image is automatically
  downloaded once package is configured
* [#164] Unit and integration tests for SemSegTraining
* [#155] Added training module for ClassificationTasks using `TimmClassifier`

### Changed
* Update development docs
* [#164] Refactor backend to new model training workflow
* [#185] Remove scheduler when using Adam optimizer

### Fixed
* Fix a bug in `utils` that causes `training_server` cannot detect gpu in Jetson
* Separate mlflow src which is copied to training docker from `DLProject` data
* [#185] Fix typo in creating mask function
* [#185] Fix get-pip url for python3.6 in docker image
* [#195] Fix incompatibility with `eureka-annotator` headless and new attribute def schema


## [0.1.0] - 2021-12-24
- [#116] Package model after training finishes
- Fix minor issues about training
- Set server default port to 50053
- Fix a bug that cause server address to not be resolved.
- Modify the training docker image definition to install from wheels

### Added

- Add bump2version configuration and implement Jenkins CI
- Added a changelog
