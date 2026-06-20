# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [48.0.0] - 2026-06-20

### Added

- Add automation module tests. (GitHub # 138)

### Changed

- Test the new shared-action.
- Fix type linting error
- Update config for new vjer.
- Use released shared actions.
- Update input name.
- Automate change log generation. (GitHub #139)
- Update documentation build pieces. (GitHub #30)
- Use new build-docs option in CI/CD workflow. (GitHub #71)
- Fix documentation link.
- Have ReadTheDocs generate everything. (GitHub #71)
- Update the copyright year. (GitHub #71)
- Fix the RTD config. (GitHub #71)
- Update Sphinx requirements.
- Update Sphinx to latest. (GitHub #71)

### Removed

- Remove Google SDK from Android install.
- Remove unused ECHILD import from sysutil.

## [47.1.1] - 2026-02-20

### Changed

- Fixed bug which prevented rmtree from working in some cases. (GitHub #137)
- Test new workflow.
- Fix rmtree on UNIX OSEN.
- Update change log.

## [47.1.0] - 2026-02-18

### Added

- Added the active_branch property to cms.Client. (GitHub #135)
- Added sysutil functions get_app_data_dir and get_app_config_dir. (GitHub #135)
- Added missing sysutil tests.
- Added delete_branch method to cms.Client. (GitHub #135)
- Added rebase argument to cms.Client.update.
- Added reset option to cms.Client.switch. (GitHub #135)
- Added all_files option to cms.Client.add_files. (GitHub #135)
- Added all_files and remote_ref arguments to cms.Client.checkin_files to inhibit gt push. (GitHub #135)
- Added set_remote method to cms.Client. (GitHub #135)

### Changed

- Apply copilot suggestions.
- Restore skipped tests.
- Run new tests only on local platform..
- Always test local module.
- Allow setting remote on branch creation.
- Allow remote to be None on cms.Client.checkin_files to inhibit gt push. (GitHub #135)
- Merge pull request #136 from Arisilon/feature/git-stream

## [47.0.0] - 2026-02-13

### Changed

- Test updated reusable workflow.
- Change default cms.Client branch to the repo default. (GitHub #134)

## [46.0.1] - 2026-02-10

### Added

- Add missing permission.
- Add new missing permission.

### Changed

- Test job checking.
- Force job fail.
- Updated dependencies. (GitHub #132)
- Test failure
- Test failure.
- Test 3.14 failure mode.
- Test a fix.
- Allow PRs to publish test results to comments.
- Test workflow fix.
- Test updated reusable workflow permissions.
- Merge pull request #133 from Arisilon/jesmith/fix-test
- Fix change log.

### Removed

- Remove test pipeline.
- Remove blank line.

## [46.0.0] - 2025-04-30

### Added

- Add missing permissions.
- Add skip-pypi-test option.
- Add rc_release config file.

### Changed

- Fixed issue with creating an Image instance for an remote registry. (GitHub #128)
- Update pyproject file.
- Set the pyproject-build flag for vjer.
- Use test workflow.
- Test new workflow.
- Pass secrets and update Vjer config.
- Merge pull request #129 from Arisilon/feature/shared-action
- Use pre-release Vjer.
- Fix syntax.
- Pass auth correctly.
- Update change log.
- Use released workflow.
- Test release workflow.
- Revert to pre-release.
- Test new vjer.
- Revert version.
- Use updated Vjer.
- Fix release number.
- Fix version spec.

### Removed

- Removed support for Google Container Registry. (GitHub #127)

## [45.0.2] - 2025-03-18

### Changed

- Update key words.
- Don't expand numeric values. (GitHub #126)
- Fix lint warning.

### Removed

- Remove use-flit in build action.

## [45.0.1] - 2025-02-16

### Changed

- Update issue templates
- Migrate repo to Arisilon organization. (GitHub #125)
- Use setuptools instead of flit. (GitHub #123)
- Fix lint error.
- Fix lint errors.
- Improve is_debug logic. (GitHub #124)

### Removed

- Remove spurious template.

## [45.0.0] - 2025-01-01

### Added

- Add publish to the main workflow. (GitHub #121)
- Add missing permissions.
- Add release token.

### Changed

- Use type in place of TypeAlias. (GitHub #78)
- Fix typing lint errors.
- Use new override decorator.
- Use pathlib.Path.walk in place of os.walk
- Update rmtree deprecated argument.
- Update dependencies.
- Update change log.
- Merge pull request #120 from tardis4500/feature/python-3.12
- Fix workflow.
- Merge pull request #122 from tardis4500/feature/better-publish
- Update actions and turn on PyPi debugging.
- Need to put publish all in primary workflow.
- Try a fine-grained release token.
- Fix workflow permissions.

## [44.0.2] - 2024-07-06

### Added

- Add publish reusable workflow.

### Changed

- Update utility scripts.
- Use re-usable workflows for test and build.
- Improve unit test results publishing.
- Fix unit test results dir name.
- Fix build.
- Update dependencies.
- Update change log.
- Revert release.
- Test release publish.
- Ignore all test_results directories.

### Removed

- Remove obsolete dependencies.
- Remove test output.

## [44.0.0] - 2024-05-06

### Added

- Add Vjer to dev requirements.

### Changed

- Merge remote-tracking branch 'origin/release/v43.2'.
- Fix change log.
- Start adding Vjer build support. (GitHub #109)
- Use Vjer for builds. (GitHub #109)
- Fix unit test on Windows.
- Fix install test.
- Install psutil and PyQt5 on MacOS.
- Need flit install before testing.
- Fix unit test directory.
- Publish unit test results.
- Fix reporter.Table first argument type. (GitHub #117)
- Update change log.
- Fix publish jobs.
- Fix publish.

## [43.2.3] - 2024-04-11

### Changed

- Fixed k8s.Cluster.patch_item. (GitHub #116)

## [43.2.2] - 2024-04-11

### Changed

- Update readme.
- Fixed k8s.ClusterObject.api_object return. (GitHub #115)

## [43.2.1] - 2024-04-11

### Changed

- Fixed issue with new spec attribute. (GitHub #114)

## [43.2.0] - 2024-04-11

### Added

- Added patch support to objects in the k8s module. (GitHub #113)

### Changed

- Fix token variable.
- Switch to OICD for publishing. (GitHub #111)
- Fix publish job permissions.
- Improve CI/CD script.
- Fix release publish.
- Update release instructions.
- Replaced the versbose argument to fileutil.prune with log_handle. (GitHub #112)
- Update publish tokens.
- Fix publish permissions.
- Fix relelase publish.
- Fix release number.

### Removed

- Remove obsolete comment.

## [43.1.1] - 2024-03-19

### Changed

- GitHub #110:
- Update change log.

## [43.0.1] - 2024-03-19

### Added

- Added argument switch to fileutil.prune. (GitHub #106)

### Changed

- Allow Path as first argument to syscmd. (GitHub #107)

## [43.0.0] - 2024-02-18

### Changed

- Update dependencies.
- Update change log.

### Removed

- Remove pre-release tag testing.

## [43.0.0rc3] - 2024-02-14

### Added

- Added fileutil.prune function. (GitHub #101)

### Changed

- Update changelog.
- Refresh .gitignore.
- Update .p4ignore to match .gitignore.
- Update release.
- Restore missing directory.
- Upgrade minimum Python to 3.11. (GitHub #69)
- Fix xor usage and age calulation.
- Reduce line errors in tests.
- Update README test section.
- Correct test ordering.
- Allow both age and count.
- Initial pass at fileutil tests.
- Fix unit tests on UNIX.
- Fix ignore_case test.
- Fixed the version tagging. (GitHub #103)
- Test tagging. (GitHub #103)

### Removed

- Remove prune complications.

## [42.2.1] - 2024-02-09

### Added

- Add test job. (GitHub #100)
- Add unit-tests. (GitHub #100)
- Add build job.
- Add MacOS support.
- Add build and pip cache.
- Add install test. (GitHub #100)
- Add Python 3.12 to tests.
- Add Python version to unit test name.
- Add token for artifact download.

### Changed

- Use updated bumpver.
- Fix pyproject.toml.
- Test GitHub actions. (GitHub #100)
- Initial GitHub action migration. (GitHub #100)
- Wait to implement virtual env caching. (GitHub #100)
- Wiat to implement checkin. (GitHub #100)
- Make test script executable. (GitHub #100)
- Try setting the environment. (GitHub #100)
- Move env vars to base workflow. (GitHub #100)
- Fix lint errors.
- Fix permissions on script.
- Use script for common actions. (GitHub #100)
- Fix build error. (GitHub #100)
- Switch from shared action to build script. (GitHub #100)
- Store build artifacts. (GitHub #100)
- Debug artifacts.
- Try hard-coding the artifacts path.
- Fix install test.
- Debug artifacts issue.
- Examine downloads.
- Look at artifacts.
- Fix install-test.
- Implement publish-test.
- Fix parameter usage.
- Try naming the job.
- Fix script permissions after rename.
- Need twine to publish.
- Improved workflow. (GitHub #100)
- Implement a matrix for testing.
- Disable failing platforms.
- Implement test install. (GitHub #100)
- Start adding final publish support. (GitHub #100)
- Try to fix bumpver checkin. (GitHub #100)
- Try fixing the bumpver commit. (GitHub #100)
- Test cache.
- Fix bulid cache.
- Fix virtualenv creation.
- Run testing on MacOS.
- Don't run static analysis on multiple OSen.
- Fix unit test on Mac.
- Fix lint error.
- TODO updates.
- Parameterize common build vaules.
- First run on Windows.
- Run Windows unit tests.
- Implement Windows unit tests.
- Print the os name.
- Fix Windows unit tests.
- Limit publishing to release branches.
- Publish the unit tests.
- Fix test results publish.
- Restrict unit test publish to Linux.
- Publish tests for MacOS and Windows.
- Create separate worklow for publishing.
- Fix shell syntax.
- Fix publish artifact download.
- Require run id input.
- Expose run ID.
- Debug publish.
- Prepare for release.
- Fix publish.
- Finalize publish steps.
- Update README.
- Fix Production publish.
- Fix release creation.
- Reset version to pre-release.

## [42.2.0] - 2023-08-10

### Added

- Added more Kubernetes objects to k8s module. (GitLab #76)

### Changed

- Set version to pre-release.

## [42.1.0] - 2023-07-05

### Added

- Added the time module. (GitLab #75)

### Changed

- Fix typeing error.
- Update change log.

## [42.0.4] - 2023-06-26

### Changed

- Fix menu.SimpleMenu class. (GitLab #74)

## [42.0.3] - 2023-06-24

### Changed

- Fix reporter.ReportObject creation when specifying an attribute. (GitLab #73)

## [42.0.2] - 2023-06-14

### Added

- Added pywin32-stubs as a requirement. (GitLab #72)

## [42.0.1] - 2023-06-09

### Changed

- Fixed issue with types and new union operator. (GitLab #70)

## [42.0.0] - 2023-06-02

### Added

- Add pylint and flake8 config to pyproject.
- Added new TypeAlias typing. (GitLab #62)
- Add pipeline file to bumpver.
- Add bumpver after publish test
- Add releases to pipeline.
- Added dotmap_to_yaml and yaml_to_dotmap functions to the lang module. (GitLab #64)
- Support ssh authentication on remote server actions. (GitLab #61)

### Changed

- Switch from Union[X, Y] to X|Y. (GitLab #62)
- Fix new mypy linting errors.
- Don't use distutils for the bulid program. (GitLab #62)
- Use setuptools build. (GitLab #62)
- Fix Pylance lint.
- Fix build.
- Move configs to pyproject.toml.
- Update pipeline to use new build mechanism.
- Fix pipeline.
- Fix mypy test.
- Fix mypy tests.
- Fix static analysis tests.
- Update unit test run.
- Update the build.
- Replaced switch with new match syntax. (GitLab #62)
- GitLab #66:
- Update pipeline.
- Fix pipeline syntax.
- Implement flit.
- Update pipeline to use flit. (GitLab #68)
- Allow flit to install without virutal env. (GitLab #68)
- Flit needs git on build. (GitLab #68)
- Fix apt usage.
- Update apt before install.
- Fix install test.
- Use raw twine forPyPi upload.
- Start bumpver implementation. (GitLab #67)
- Bump version 42.0.0rc0 -> 42.0.0rc1
- Don't create tag on rc bumpver.
- Try using virutal env.
- Source the venv setup.
- Debug mkvirtualenv issue.
- Better debugging.
- Use base virutalenv package.
- Fix syntax.
- Fix flit root install.
- Improve test install.
- Merged from master.
- Bump version 42.0.0rc1 -> 42.0.0rc2
- Print venv status.
- Bump version 42.0.0rc2 -> 42.0.0rc3
- Fix venv init.
- Limit cache.
- Rename publish to release.
- Bump version 42.0.0rc3 -> 42.0.0rc4
- Fix broken release job.
- Debug bumpver failure.
- Bump version 42.0.0rc4 -> 42.0.0rc5
- Perform git install for publisher.
- Bump version 42.0.0rc5 -> 42.0.0rc6
- Install git for all .base jobs.
- Bump version 42.0.0rc6 -> 42.0.0rc7
- Bump version 42.0.0rc7 -> 42.0.0rc8
- Bump version 42.0.0rc8 -> 42.0.0rc9
- Bump version 42.0.0rc9 -> 42.0.0rc10
- Bug in bumpver push.
- Fix git push.
- Bump version 42.0.0rc10 -> 42.0.0rc11
- Debug git push.
- Fix debug line.
- Really stupid typo.
- Try fixing push.
- Bump version 42.0.0rc11 -> 42.0.0rc12
- Debug checking.
- Fix typo.
- Bump version 42.0.0rc12 -> 42.0.0rc13
- Improve bumpver config.
- Fix bumpver usage.
- Bump version 42.0.0rc13 -> 42.0.0rc14
- Test release job.
- Never push with bumpver.
- Pull before push on release.
- Fix lint.
- Fix the git pull on release.
- Setup for release testing.
- Fix release.
- Update test version.
- Also push the final release tag.
- Fix release spec.
- Fix release job.
- Update version for release testing.
- Fix release parameters.
- Update for release testing.
- Fix final publish workflow.
- Need separate job for final version bump.
- Unify final publish into a single job.
- Fix version for testing.
- Need curl installed.
- Reorder final push commands.
- Fix bumpver variable name usage.
- New test version.
- Fix release info.
- Fix mypy error for missing dotmap stubs. (GitLab #64)
- Fix release number after testing. (GitLab #67)
- Improved version module. (GitLab #55)
- Require full path to Google Cloud service account key file. (GitLab #57)
- Update dotmap/yaml utilities.

### Removed

- Remove extraneous mypy argument.
- Remove obsolete code.
- Remove test upload from legacy builder.
- Remove obsolete version def.
- Remove sudo usage.

## [41.0.0] - 2022-09-20

### Changed

- Update release number.

### Removed

- Remove LoadBalancer module. (GitLab #63)
- Remove obsolete comment lines.

## [40.0.0] - 2021-10-26

### Changed

- Upgrade minimum Python to 3.9. (GitLab #51)
- Use new dict union operators. (GitLab #51)
- Use removeprefix. (GitLab #51)
- Update release number.

## [39.0.5] - 2021-05-18

### Changed

- Fixed k8s delete_item for non-namespaced objects. (GitLab #60)
- Update requirements.

## [39.0.4] - 2021-05-18

### Changed

- Allow namespace args in k8s module to be either positional or named. (GitLab #58)

## [39.0.3] - 2021-05-18

### Changed

- Assume container output always has Linux endings. (GitLab #59)

## [39.0.2] - 2021-05-18

### Added

- Add requirement for pywin32-stubs. (GitLab #56)

### Changed

- Update release.

## [39.0.1] - 2021-03-05

### Added

- Add marker file to indicate typing support. (GitLab #54)

## [39.0.0] - 2021-03-02

### Added

- Added PEP484 type hints to expander module. (GitLab #29)
- Added PEP484 type hints to fileutil module. (GitLab #29)
- Added PEP484 type hints to gui module. (GitLab #29)
- Added PEP484 type hints to iispy module. (GitLab #29)
- Added PEP484 type hints to k8s module. (GitLab #29)
- Added PEP484 type hints to lang module. (GitLab #29)
- Added PEP484 type hints to loadbalancer module. (GitLab #29)
- Added PEP484 type hints to logger, menu, and netutil modules. (GitLab #29)
- Added PEP484 type hints to platarch and qbpy modules. (GitLab #29)
- Added PEP484 type hints to reporter module. (GitLab #29)
- Added PEP484 type hints to servermgr module. (GitLab #29)
- Added PEP484 type hints to serverpath module. (GitLab #29)
- Added PEP484 type hints to statemachine module. (GitLab #29)
- Added PEP484 type hints to sysutil module. (GitLab #29)
- Added PEP526 type hints where required to resolve type linting. (GitLab #29)
- Added PEP526 type hints to automation, cloudmgr, and cms modules. (GitLab #29)
- Added PEP526 type hints to cms and commander modules. (GitLab #29)
- Added PEP526 type hints to configmgr modules. (GitLab #29)
- Add static analysis tools to requirements. (GitLab #29)
- Added close/__enter__/__exit__ to ConfigurationSet and Configuration in configmgr. (GitLab #35)
- Added Namespace support to k8s module. (GitLab #44)
- Add fstr = for debug. (GitLab #6)
- Add basics for documentation generation. (GitLab #1)
- Added cmdliner module. (GitLab #53)

### Changed

- Update release number and fix bad pipline on tags.
- Finished adding PEP484 type hints to commander module. (GitLab #29)
- GitLab #29:
- Finished adding PEP484 type hints to data module. (GitLab #29)
- Fix build error. (GitLab #29)
- Finished adding PEP484 type hints. (GitLab #29)
- Update requirements.
- Fix PyQt5 bulid issue.
- Fix unit tests. (GitLab #29)
- Debug pipeline failure.
- Install git for build.
- Fix type linting issues. (GitLab #29)
- Move build driver to project root.
- Fix remake_dir.
- Fix build.
- GitLab Issue #29:
- Fix build by adding pylint to requirements. (GitLab issue #29)
- Fixed refactor linting in gui, iispy, k8s, lang, loadbalancer, logger, menu, netutil, platarch, qbpy, and reporter modules. (GitLab #29)
- Fixed refactor linting in servermgr, serverpath, statemachine, and sysutil modules. (GitLab #29)
- Fix pylint run. (GitLab #29)
- Finish static analysis for build pipeline. (GitLab #29)
- Fix docker version.
- Update .p4ignore to match .gitignore.
- Fix Linux build errors. (GitLab #29)
- Fix issue with 3.7 Path.rename. (GitLab #29)
- Ignore TODO on static analysis. (GitLab #29)
- Fix type hints.
- Fix gcloud command on Windows.
- Fixed failure on cloudmgr.Image.pull method. (GitLab #41)
- Fix pylance linting errors.
- Fix errors in cms.Client.switch method for existing branches in Git. (GitLab #50)
- Don't install PyQt5 on Android architectures. (GitLab #39)
- Fix pylint error on Linux.
- Don't install psutil on arm architectures. (GitLab #39)
- Use splitlines() instead of split('\n'). (GitLab #40)
- Use exception chaining where appropriate. (GitLab #49)
- Start converting properties to read-only where applicable. (GitLab #38)
- Protect read-only public members behind property definition. (GitLab #38)
- Create an annotated tag on release. (GitLab #30)
- Upgrade minimum Python to 3.7 and use dataclasses where applicable. (GitLab #5)
- Move build.py to root of project. (GitLab #45)
- Fix protected usage.
- GitLab #6:
- Continue adding walrus operator where applicable. (GitLab #6)
- Continued adding walrus operator where applicable. (GitLab #6)
- Finish adding walrus operator where applicable. (GitLab #6)
- Start adding position only parameters where applicable. (GitLab #6)
- Consitued adding position only parameters. (GitLab #6)
- Continue adding position only parameters. (GitLab #6)
- Continue adding position only parameters where applicable. (GitLab #6)
- Finish adding position only parameters where applicable. (GitLab #6)
- Fix build. (GitLab #6)
- Update change log.
- Start cleaning up documentation build errors. (GitLab #1)
- Fix doc build. (GitLab #1)
- PyQt5 not building on Alpine.
- Use apt instead of apk.
- Fix apt package names.
- Fix apt install.
- Need -y on apt commands.
- Try fixing pip install issues.
- Try using Alpine PyQt5 OS package.
- Test Ubuntu slim image.
- Fix mypy import error for msvcrt on Linux.
- Start improving mypy linting.
- Fix linting issues.
- Fix documentation build. (GitLab #1)
- Build the docs with Python 3.8. (GitLab #1)
- Fix publish stages.
- Improve SysCmdRunner. (GitLab #53)
- Cleanup linting errors.

### Removed

- Remove PyQt5 from build requirements.
- Remove debugging line.
- Removed logger module. (GitLab #37)
- Remove test file.

## [38.1.2] - 2020-05-19

### Added

- Add line to prevent merge conflicts.

### Changed

- Finished adding PEP484 type hints to cms module. (GitLab #29)
- Pass Kubernetes API call parameters to exec call. (GitLab #48)
- Fix release number.

## [38.1.1] - 2020-05-05

### Added

- Added class method docstrings for the cms.Label class. (GitLab #29)
- Added class method docstrings for the commander and configmgr modules. (GitLab #29)
- Added class method docstrings for the expander module. (GitLab #29)
- Added class method docstrings for the gui module. (GitLab #29)
- Added class method docstrings for the lang, logger, menu, and platarch modules. (GitLab #29)
- Added class method docstrings for the qbpy module. (GitLab #29)
- Added class method docstrings for the reporter module. (GitLab #29)
- Add nitrosdl-python, psutil, and wmi modules. (Gitlab #8)
- Added class method docstrings for the statemachine module. (GitLab #29)
- Added class method docstrings for the sysutil module. (GitLab #29)
- Added class method docstrings for the tcpy module. (GitLab #29)
- Added class method docstrings for the loadbalancer module. (GitLab #29)
- Added class method docstrings for the serverpath module. (GitLab #29)
- Added PEP484 type hints to automation module. (GitLab #29)
- Added PEP484 type hints to cloudmgr module. (GitLab #29)

### Changed

- Started adding class method docstrings for cms.Client. (GitLab #29)
- Continued adding class method docstrings for cms.Client. (GitLab #29)
- Fixes after last updates. (GitLab #29)
- Finished adding class method docstrings for the cms module. (GitLab #29)
- Fix CHANGELOG lint warning.
- Started adding class method docstrings for the data module. (GitLab #29)
- Continued adding class method docstrings for the data module. (GitLab #29)
- Finished adding class method docstrings for the data module. (GitLab #29)
- Started adding class method docstrings for the expander module. (GitLab #29)
- Started adding class method docstrings for the k8s module. (GitLab #29)
- Update TODO list.
- Started adding class method docstrings for the iispy module. (GitLab #29)
- Continued adding class method docstrings for the iispy module. (GitLab #29)
- Finished adding class method docstrings for the iispy module. (GitLab #29)
- Continued adding class method docstrings for the k8s module. (GitLab #29)
- Finished adding class method docstrings for the k8s module. (GitLab #29)
- Try to fix freeze logic.
- Update Python and frozen requirements.
- Move load balancer support from servermgr to new loadbalancer module. (GitLab #46)
- Started adding class method docstrings for the servermgr module. (GitLab #29)
- Continued adding class method docstrings for the servermgr module. (GitLab #29)
- Move ServerPath from servermgr to a new module.
- Finished adding class method docstrings for the servermgr module. (GitLab #29)
- Reordered class members alphabetically by type. (GitLab #29)
- Started adding PEP484 type hints to cms module. (GitLab #29)
- Set the required WMI version to be less than 1.5. (GitLab #47)
- Fix WMI setup version specification. (GitLab #47)
- Fix release number.

## [38.1.0] - 2020-02-15

### Added

- Added context parameter to k8s.Cluster initializer. (GitLab #43)

### Changed

- Update freeze file and release number.
- Fix build error after pip package updates.
- Need to install libffi-dev.
- Also need libssl-dev.
- Fix ssl package on alpine.
- Don't run full before_script on publish.
- Fix publisher template.
- Try to fix publish.

## [38.0.1] - 2020-02-13

### Added

- Added more docstrings. (GitLab #29)
- Add module level doctrings, including attributes. (GitLab #29)
- Added module level function docstrings for neutil, servermgr, version. (GitLab #29)
- Add function level docstrings to land and sysutil. (GitLab #29)
- Add class docstrings for data module. (GitLab #29)
- Add class docstrings to the expander module. (GitLab #29)
- Add class docstrings to fileutil module. (GitLab #29)
- Add class docstrings to gui module. (GitLab #29)
- Added more class docstrings. (GitLab #29)
- Add more Error docstrings. (GitLab #29)
- Added remaining error docstrings. (GitLab #29)
- Add docstrings to the class init methods for commander and configmgr. (GitLab #29)
- Added docstrings for class init methods for the expander module. (GitLab #29)
- Added docstrings for class init methods for the fileutil and gui modules. (GitLab #29)
- Added docstrings for class init methods for the iispy and k8s modules. (GitLab #29)
- Added docstrings for class init methods for the lang and logger modules. (GitLab #29)
- Added docstrings for class init methods for the menu module. (GitLab #29)
- Added docstrings for class init methods for the qbpy module. (GitLab #29)
- Added docstrings for class init methods for the tcpy module. (GitLab #29)
- Added docstrings for class init methods for the reporter, statemachine, and sysutil modules. (GitLab #29)
- Added docstrings for class init methods for the servermgr module load balancer objects. (GitLab #29)
- Added docstrings for class init methods for servermgr module objects. (GitLab #29)
- Added class property docstrings for the cloudmgr module. (GitLab #29)
- Added class property docstrings for the cms.Label class. (GitLab #29)
- Added class property docstrings for the cms and configmgr modules. (GitLab #29)
- Added class property docstrings for the data module. (GitLab #29)
- Added class property docstrings for the expander, iispy, k8s, and logger modules. (GitLab #29)
- Added class property docstrings for the qbpy module. (GitLab #29)
- Added class property docstrings for the reporter module. (GitLab #29)
- Added class property docstrings for the servermgr and tcpy modules. (GitLab #29)
- Added class method docstrings for the automation module. (GitLab #29)
- Added class method docstrings for the cloudmgr module. (GitLab #29)

### Changed

- Lint cleanup. (GitLab #33)
- Set -x on build script for Linux.
- Create PyPi facing README-USER. (GitLab #26)
- Fix filetype.
- Fix build after new PyPi long description. (GitLab #26)
- More variable renames due to rename to BatCave. (GitLab #27)
- Start creating improved docstrings. (GitLab #29)
- Update docstrings for automation module. (GitLab #29.)
- Move cSpell ignores to bottom. (GitLab #29)
- Start adding module function docstrings. (GitLab #29)
- Start adding class docstrings. (GitLab #29)
- Finished adding class docstrings. (GitLab #29)
- Started adding docstrings to Error classes. (GitLab #29)
- Started adding class init docstrings. (GitLab #29)
- Finish the CMS module init docstrings. (GitLab #29)
- Update TODO list. (GitLab #29)
- Started adding init docstrings to expander. (GitLab #29)
- Continued adding init docstrings to expander. (GitLab #29)
- Finished adding docstrings for class init methods for servermgr module objects. (GitLab #29)
- Fixed the class property docstrings for the cloudmgr module. (GitLab #29)
- Update .gitlab-ci.yml
- Fixed str_to_pythonval when ~ in value. (GitLab #42)
- Allow publish from release branch.
- Try to allow publishing from a release branch.

## [38.0.0] - 2019-10-30

### Added

- Added auto-increment of the release during production publish. (GitLab #15)
- Added better control on k8s.Cluster.create_job with wait_for and timeout options. (GitLab #24)
- Added release instructions to README.rst. (GitLab #20)

### Changed

- Renamed hallog to logger. (GitLab #25)
- Update README.rst
- Update README.md
- Rename CHANGELOG.rst to CHANGELOG.md.
- Fix comments for Markdown.
- Fix comments in markdown.
- Converted README and CHANGELOG from restructuredText to Markdown.

## [37.1.2] - 2019-10-29

### Changed

- Fixed kubectl issue. (GitLab #22)

## [37.1.1] - 2019-10-28

### Added

- Added missing Kubernetes module requirement. (GitLab #21)

## [37.1.0] - 2019-10-28

### Added

- Added initial Kubernetes support module. (GitLab #17)
- Add debugging output.

### Changed

- Updated change log.
- Need to pass the release number in when publishing. (GitLab #18)
- Converted from pipenv to standard pip requirements file. (GitLab #19)
- Update release.
- Freeze the packages. (GitLab #19)
- Don't install development packages durin CI build. (GitLab #19)
- Don't use pipenv to run python commands. (GitLab #19)
- Automated tagging during build
- Use cmd.Client for git interactions in build.py. (GitLab #16)
- Fix installation on Android. (GitLab #10)
- Try to set the test release number.
- Try to generate a random release number.
- Generate the random release in build.py.
- Update change list.

## [37.0.1] - 2019-10-24

### Added

- Added CI/CD support to build.py. (GitLab #7)
- Add initial CI/CD configuration.
- Add wildcard to catch all test results.
- Add release tagging. (GitLab #7)
- Added release management. (GitLab #9)

### Changed

- First commit.
- Fix switch for Python 3.7.
- Update change log.
- GitLab issue #3:
- Made dependencies less restrictive. (GitLab #2)
- Fix syntax.
- Don't require build.py to be executable.
- Move packages from dev that are needed for all builds.
- Update pipenv lock file. (GitLab #13)
- Need to run the build in the pipenv context. (GitLab #7)
- Improve stage names and add install test. (GitLab #7)
- Get the release number for the install test. (GitLab #7)
- Fix unit test results.
- Fix unit test publish. (GitLab #14)
- Fix unit test publishing. (GitLab #14)
- Fix use of extends. (GitLab #7)
- Need better image for install testing. (GitLab #7)
- Set username. (GitLab #7)
- Fix syntax. (GitLab #7)
- Don't use keyring for CI publishing.
- Update lock file. (GitLab #7)
- Improve publish. (GitLab #7)
- Simplify the release number injection for now. (GitLab #7)
- Update variable usage. (GitLab #7)
- Update .gitlab-ci.yml
- Test tagging. (GitLab #7)
- Improve CI/CD flow. (GitLab #7)
- Use random number for test publish. (GitLab #7)
- Fix variable syntax and rename all artifacts. (GitLab #7)
- Fix test publish. (GitLab #7)
- Test install filure. (GitLab #7)
- Make the same adjustment for the wheel. (GitLab #7)
- Debug upload. (GitLab #7)
- Debug publish test. (GitLab #7)
- Only publish wheel no test and use different tokens for test vs. prod. (GitLab #7)
- Use apt instead of apt-git. (GitLab #7)
- Use more complete Python image. (GitLab #7)
- No need to install git in new image. (GitLab #7)
- Try pushing to a different remote. (GitLab #7)
- Fix git URL on new remote. (GitLab #7)
- Don't allow failure of manual jobs. (GitLab #7)
- Improve CI/CD flow and release management. (GitLab #7, GitLab #9)
- Fix unit test artifacts. (GitLab #7)

### Removed

- Remove obsolete cache file and reference. (GitLab #7)

<!-- generated by git-cliff -->
<!-- begin legacy manual entries -->

### [37.0.0] - 2019-10-15

- Added
- Added support for publishing to PyPi.

- Changed
- Updated build.py to not rely on build and prdb modules.

- Removed
- Moved build and prdb modules to a separate project.

### [36.3.2] - 2019-09-26

- Changed
- Fix update_cfg_list rename to updater.

### [36.3.1] - 2019-09-26

- Changed
- Convert Path to str before passing to COM handler.

### [36.3.0] - 2019-09-19

- Changed
- Allow multiple property holders in Expander.
- Fix lang.flatten() and add lang.flatten_string_list().
- Allow bypass of nuget restore in MSBuildBuilder.
- Make sure the results is a Path() in MSTestUnitTester.
- Add support for dashboards to the qbpy module.
- Fix build when docker authentication fails.
- Upgrade cx_Freeze to 5.1.1.
- Upgrade GitPython to 3.0.2.
- Upgrade pyodbc to 4.0.27.
- Upgrade PyQt5 to 5.13.1.
- Upgrade setuptools to 41.2.0.

### [36.2.0] - 2019-07-25

- Added
- Added build.DotCoverTester().
- Added build.NUnitTester().
- Added support for command arguments on servermgr.Server().create_scheduled_task().

### [36.1.1] - 2019-07-15

- Changed
- Fix servermgr.ScheduledTask().TASK_PATH definition on Linux.

### [36.1.0] - 2019-07-12

- Added
- Added start_in and disable arguments to servermgr.Server().create_scheduled_task().

- Changed
- Fix servermgr.Server().create_scheduled_task() issue when spaces in task executable path.

### [36.0.0] - 2019-07-05

- Changed
- Improved options for servermgr.Server().create_scheduled_task().
- Upgraded docker to 4.0.2.
- Upgraded PyQt to 5.13.0.

### [35.1.0] - 2019-06-17

- Added
- Add servermgr.Server create_service() and remove_service() methods.

- Changed
- Don't perform a remote appcmd call on the local host in iispy.
- Upgraded docker to 4.0.1.
- Upgraded psutil to 5.6.3.
- Upgraded PyQt to 5.12.2.
- Upgraded requests to 2.22.0.

### [35.0.0] - 2019-05-08

- Changed
- Allow ConfigCollection to take a pathlib.Path object.
- Fix error in qbpy.QuickBuildCfg._get_id().
- Fix configmgr parent/include processing.
- Upgraded psutil to 5.6.2.
- Upgraded setuptools to 41.0.1.

### [34.0.0] - 2019-04-25

- Added
- Added CopyBuilder and CopyProduct to build module.
- Added option to both publish and extract files from docker container.
- Added __setattr__(), enable(), and disable() to qbpy.QuickBuildCfg.
- Added qbpy.QuickBuildBuild class to support wait flag in QuickBuildCfg.disable().

### [33.1.0] - 2019-04-17

- Added
- Added redirect_output argument to build.MSBuildBuilder.
- Added Server.get_scheduled_task_list() method.
- Added Server.get_service_list() method.

- Changed
- Fixed issues with C-Sharp version files and created Builder.update_cs_assemblyinfo().
- Upgraded docker to 3.7.2.
- Upgraded setuptools to 41.0.0.
- Upgraded unittest-xml-reporting to 2.5.1.
- Fixed lang.str_to_pythonval() to convert None.

### [33.0.2] - 2019-03-26

- Changed
- Upgraded docker to 3.7.1.
- Upgraded psutil to 5.6.1.
- Upgraded PyQt5 to 5.12.1.

### [33.0.1] - 2019-03-22

- Changed
- Replace use of property decorator when getter has optional arguments.

### [33.0.0] - 2019-03-05

- Added
- Added support for extracting build artifacts from container builds.

- Changed
- Use property decorator.
- Fix bad use of self.
- Don't install cx_Freeze if Python > 3.6.
- Upgraded psutil to 5.5.1.
- Upgraded pyodbc to 4.0.26.

- Removed
- Removed virtualenv.

### [32.0.0] - 2019-02-14

- Added
- Added support for nested configurations.
- Added build.ConfigurationBuilder() argument ignore_configs.
- Added start and stop methods to iispy.IISInstance.
- Added ignore_files and no_expand_files to build.ConfigurationBuilder and expander.Expander.expand_directory().
- Added prdb.Product.children property.

- Changed
- Server().get_iis_instance() should return local reference.
- Made all names more Pythonic.
- Made module constants into class member variables where possible.
- Fixed usage of configure and make in GNUBuilder.
- Upgraded psutil to 5.5.0.
- Upgraded pyQt to 5.12.
- Upgraded setuptools to 40.8.0.

### [31.0.0] - 2019-01-11

- Added
- Added qbpy.QuickBuildCfg.remove() method.

- Changed
- Fix git errors on push not throwing catch-able exceptions.
- Updated PRDB schema to use good python naming convention.
- Make sure iispy module does not cause an import failure on Linux.
- Provide proper iteration on groups, classes, and properties in prdb module.
- Provide interface for adding a property class.
- Upgraded docker to 3.7.0.
- Upgraded p4python to 2018.2.1743033.
- Upgraded pyodbc to 4.0.25.
- Upgraded unittest-xml-reporting to 2.2.1.

### [30.0.3] - 2019-01-09

- Changed
- Fix expander.Expander.evaluate_expression().

### [30.0.2] - 2018-12-18

- Changed
- Fix build.EUPBuilder commander.Commander variable handling.

### [30.0.1] - 2018-12-17

- Changed
- Revert inadvertent PRDB schema change.

### [30.0.0] - 2018-12-13

- Changed
- Improved platarch.Platform().
- Use commander.Commander() to parse build arguments.
- Improved cx_Freeze package creation logic.
- Moved cmds functions to sysutil.
- Renamed cmds module to commander.
- Upgraded docker to to 3.6.0.
- Upgraded psutil to to 5.4.8.
- Upgraded requests to 2.21.0.
- Upgraded setuptools to 40.6.3.
- Final Pylint cleanup.

- Removed
- Moved BaRT specific support module to BaRT.

### [29.1.1] - 2018-11-29

- Changed
- Fixed remote_powershell member of iispy.IISInstance.

### [29.1.0] - 2018-11-27

- Added
- Added no_powershell option to iispy.IISInstance.

### [29.0.2] - 2018-11-20

- Changed
- Fix double remote option sent to syscmd by iispy.appcmd().

### [29.1.0] - 2018-11-02

- Changed
- User the docker client to manage Google registry images.
- Upgraded setuptools to 40.5.0.

### [29.0.1] - 2018-10-24

- Changed
- Fixed servermgr.Service.get_service() on Windows.

### [29.0.0] - 2018-10-22

- Added
- Added servermgr.LoadBalancer support for adding a VIP.
- Added upstart support to servermgr.Service().

- Changed
- Fixed SysV service management in servermgr.LinuxService.
- Upgraded docker to to 3.5.1.
- Upgraded requests to 2.20.0.

### [28.0.3] - 2018-10-10

- Changed
- Fixed service servermgr service detection on non-systemctl Linux systems.

### [28.0.3] - 2018-10-08

- Changed
- Pass credentials on remote command in servermgr.Server.run_command().

### [28.0.2] - 2018-10-04

- Changed
- Upgraded PyQt to to 5.11.3.
- Upgraded pywin32 to 224.

### [28.0.1] - 2018-10-02

- Changed
- Fixed issue with servermgr.LinuxService.status failing on Linux2.

### [28.0.0] - 2018-09-26

- Added
- Added support for running remote commands using PowerShell from Windows to Windows.

- Changed
- Pylint cleanup of servermgr module.

- Removed
- Removed sqlscript module.

### [27.3.0] - 2018-09-24

- Added
- Added virtual directory support to iispy.IISObject management.

- Changed
- Improved appcmd handling in iispy module.
- Upgraded setuptools to 40.4.3.
- Pylint cleanup of setup.py.

### [27.2.0] - 2018-09-19

- Added
- Added start/stop support to iispy.IISObject management.

- Changed
- Upgraded setuptools to 40.4.1.
- Pylint cleanup in iispy module.

### [27.1.0] - 2018-09-07

- Changed
- Improved cms.Client.merge().

### [27.0.0] - 2018-08-24

- Added
- Added cms.Client.chmod_files().

- Changed
- Fix build.DockerDotNetCoreProduct() default for verfiles.
- Return AttributeError to fix hasattr() usage.
- Fixed issue with cms.Client.switch() creating existing branch.
- Convert cms to use arg list rather than requiring lists.
- Upgraded docker to 3.5.0.
- Upgraded google-cloud to 0.34.0.
- Upgraded psutil to 5.4.7.
- Upgraded pyodbc to 4.0.24.
- Upgraded setuptools to 40.2.0.
- Pylint cleanup on cms module.

### [26.4.3] - 2018-08-08

- Changed
- Ignoring stderr in cloudmgr.Image.manage().

### [26.4.2] - 2018-08-08

- Changed
- Ignoring stderr in cloudmgr.Image.tag().
- Pylint cleanup on cloudmgr module.

### [26.4.1] - 2018-08-08

- Changed
- Fixed issue with cmds.SysCmdRunner keeping keys from last run.
- Fix expander.Expander.expand_file() failure when intermediate empty directories don't exist.
- expander.Expander.expand_directory() double recurses into directories.
- Pylint cleanup on expander module.

### [26.4.0] - 2018-08-01

- Added
- Added build.DockerNodeProduct() and build.DockerDotNetCoreProduct().

- Changed
- Fix qbpy issues.
- Upgraded GitPython to 2.1.11.
- Upgraded setuptools to 40.0.0.

### [26.3.0] - 2018-07-13

- Added
- Added timeout parameter to servermgr.Process.manage().

- Changed
- Fixed timeout checks in servermgr.

### [26.2.0] - 2018-07-12

- Added
- Added timeout parameter to servermgr.Service.manage().

- Changed
- sysutil.syscmd(): Add an extra -t to ssh on remote calls to prevent blocking in some situations.

### [26.1.3] - 2018-07-11

- Changed
- Re-enable remove service management for Linux.

### [26.1.2] - 2018-07-09

- Changed
- Missed case compare change when running on Windows.

### [26.1.1] - 2018-07-09

- Changed
- Ignore case on Windows when running command drivers.

### [26.1.0] - 2018-07-05

- Added
- Added pyodbc module at version 4.0.23.

- Changed
- Upgraded docker to 3.4.1.
- Upgraded PyQt5 to 5.11.2.

### [26.0.1] - 2018-06-29

- Changed
- Fixed issues where servermgr.Server().get_service() thrown an error rather than None if the service is not found on CentOS 6.9.

### [26.0.0] - 2018-06-29

- Added
- Added support for Linux processes in servermgr.
- Added EUPBuilder and EUPProduct.

- Changed
- Fixed issues with servermgr.ServerPath when Server is local.
- Improved servermgr.ServerPath.copy() logic when remote is local.
- Upgraded requests to 2.19.1.
- Upgraded docker to 3.4.0.

### [25.0.1] - 2018-06-06

- Changed
- Fix issue setting default verfiles for MSBuild DB projects.

### [25.0.0] - 2018-06-06

- Changed
- Remove product definition defaults except for name from prdb.ProductDB.add_product().

### [24.1.0] - 2018-06-05

- Added
- Added support for new code roll parameters to prdb.ProductDB.add_product().

### [24.0.1] - 2018-06-05

- Changed
- Fix version calculations in build module.

### [24.0.0] - 2018-06-05

- Added
- Added pkgtype arg to build.MavenBuilder class.
- Added ant support.
- Added support for creating, switching and merging git branches.

- Changed
- Pass release argument to maven in build.MavenBuilder.
- Moved argument processing from build execution to Product instantiation.
- Converted initializers to use tuple() instead of None guard.
- Accept default args in ActionCommandRunner.
- Improved git branch management.
- Upgraded google-cloud to 0.33.1.
- Upgraded GitPython to 2.1.10.
- Upgraded setuptools to 39.2.0.
- Upgraded unittest-xml-reporting to 2.2.0.

### [23.0.0] - 2018-05-01

- Changed
- Upgraded docker to 3.3.0.
- Upgraded setuptools to 39.1.0.

- Removed
- Removed sysutil.recopytree().

### [22.2.2] - 2018-04-25

- Changed
- Remove Google Cloud login on every command.

### [22.2.1] - 2018-04-25

- Changed
- Need to login to Google Cloud instance before every command.

### [22.2.0] - 2018-04-24

- Added
- Added lang.flatten() and flatten_output argument to sysutil.syscmd().

- Changed
- GitPython doesn't handle pathlib.Path objects.

### [22.1.5] - 2018-04-18

- Changed
- Fixed issue where fileutil.unpack does not work if dest argument is used.

### [22.1.4] - 2018-04-17

- Changed
- Fixed minor_version calculation for single word versions.

### [22.1.3] - 2018-04-17

- Changed
- Fixed minor_version calculation for single word versions.

### [22.1.2] - 2018-04-16

- Removed
- Removed pypiwin32 since docker specifies a fixed version.

### [22.1.1] - 2018-04-16

- Added
- Added pypiwin32 back as it is used by some other package.

- Changed
- Fix minor issues with maven builds.

### [22.1.0] - 2018-04-13

- Added
- Added build.VisualStudioDatabase product type.
- Added build.MavenBuilder and MavenProduct.
- Added ability to parse python data types in lang.str_to_pythonval().
- Added append_stderr option to sysutil.syscmd().

- Changed
- Fix fileutil.unpack to work with pathlib.Path objects.
- Upgrade docker to 3.2.1.
- Improved SQLScript.execute().

### [22.0.0] - 2018-03-30

- Added
- Added cmds.SysCmdRunner as a generalized replacement of build.run_build_command.
- Added cloudmgr module.
- Added support for adding and removing IIS sites, apps, and pools.
- Added support for adding and removing servermgr.ScheduledTask.

- Changed
- Added ability to use Logger without writing to a file.
- Make sure npm calls fail when returning a non-zero error code.
- Fixed issue with setting a null list of version files on MSBuildBuilder.
- Update docker to 3.1.4.
- Update GitPython to 2.1.9.

### [21.0.0] - 2018-03-19

- Added
- Added artifact archive support to base Builder class.

- Changed
- Fix Windows to Windows remote file copy in servermgr.ServerPath().copy().
- Fix build.ConfigurationBuilder use of verfiles.
- Update docker to 3.1.3.

- Removed
- Removed automated post-build expansion of config files in build.Builder.execute().
- Removed arch argument to build.Builder.

### [20.0.0] - 2018-03-19

- Changed
- Overhaul servermgr.ServerPath() to subclass pathlib.PurePath().
- Update setuptools to 39.0.1.

### [19.0.2] - 2018-03-16

- Changed
- Fixed use of walk with Path().

### [19.0.1] - 2018-03-14

- Changed
- Use the --pull option on docker builds.

### [19.0.0] - 2018-03-13

- Added
- Added branch and environment information to PRDB.
- Added support for .Net Core versioning in .csproj files.

- Changed
- Changed from os.path usage to pathlib.Path.
- Update docker to 3.1.1
- Update PyQt5 to 5.10.1
- Update pywin32 to 223
- Update setuptools to 38.5.2

- Removed
- Removed the PRDB build, release, and revision information.
- Removed workspace and cmsclient support.

### [18.0.0] - 2018-02-21

- Added
- Added build.DockerUnitTester for extracting test results run during Docker image build.

- Changed
- Use Docker Python API instead of Docker CLI.

- Removed
- Removed the civars.txt file.

### [17.1.3] - 2018-02-19

- Added
- Added Docker Python API.

- Changed
- Fixed servermgr module use of sysutil.syscmd.

### [17.1.2] - 2018-02-13

- Changed
- Improved menu.SimpleMenu implementation.
- Update setuptools to 38.5.1
- Update unittest-xml-reporting to 2.1.1
- Update p4python to 2017.2.1615960

### [17.1.1] - 2018-02-01

- Changed
- Fixed issue using both lists and tuples.

### [17.1.0] - 2018-01-30

- Added
- Added extra_vars argument to build.ConfigurationBuilder.

### [17.0.0] - 2018-01-29

- Changed
- Update pypiwin32 to 222.
- Update PyQt5 to 5.10.
- Changed the repo reference file name.
- Always publish repo references in artifacts directory for Docker builds.

- Removed
- Removed slacker dependency.
- Removed obsolete static variable.

### [16.1.0] - 2018-01-18

- Added
- Added support for Docker images push to Google Cloud registry.

### [16.0.1] - 2018-01-11

- Changed
- Fixed build.VisualStudioApplication to work with MSBuildBuilder changes.

### [16.0.0] - 2018-01-10

- Added
- Added netutil.download.
- Added support for enabling/disabling system services.
- Added to sysutil: create_user, create_groups.

- Changed
- Replace sysutil.chmodtree with chmod/chown with recursive parameter.
- Make Cmd driver processing case-sensitive.
- Update sysutl.syscmd to take command, arg1, arg2 rather than cmdspec.
- Updated internal version number to three digits.
- Fixed error with unpacking compressed tar files.
- Update setuptools to 38.4.0.

### [15.4.0] - 2017-12-19

- Added
- Improved MSTest support.
- Build completed successfully message.

- Changed
- Update default version file for webapp project type.
- Update setuptools to 38.2.4.
- Update virtualwrapper-win to 1.2.5.
- Update GitPython to 2.1.8.
- Update cx_Freeze to 5.1.1.

### [15.3.0] - 2017-12-07

- Added
- Added VisualStudioWebsite and VisualStudioWebapp.

- Changed
- Improve product and builder argument handling.
- Added leader to build messages.
- Change Docker tag to be just the buildname.

- Removed
-Removed vsver argument to Visual Studio products and builders.

### [15.2.0] - 2017-11-30

- Added
- Added create_package argument to CxFreezeBuilder.

- Changed
- Don't require packages which aren't available in Docker Alpine containers.
- Don't install PyQt5 on unsupported Linux distributions.
- Improve Linux build OS determination in platarch.get_type.

### [15.1.1] - 2017-11-29

- Changed
- Make sure all __getattr__ calls raise AttributeError on failure.

### [15.1.0] - 2017-11-28

- Added
- Added VisualStudioWebapp product type.
- Added hasapp option to VisualStudioWebsite product type.

- Changed
- Update setuptools to 38.2.3.

### [15.0.5] - 2017-11-27

- Changed
- Update setuptools to 38.2.1.
- Update PyQt5 to 5.9.2.

### [15.0.4] - 2017-11-22

- Changed
- Updated multi-server build config file handling.
- Update setuptools to 37.0.0.
- Update virtualwrapper-win to 1.2.4.
- Update PyQt5 to 5.9.1 on Linux.

### [15.0.3] - 2017-11-16

- Changed
- Fix multi-server build config file handling.

### [15.0.2] - 2017-11-15

- Changed
- Fix build config file handling.

### [15.0.1] - 2017-11-13

- Changed
- PyQt5 downgraded to 5.9 on Linux since 5.9.1 is not available.

### [15.0.0] - 2017-11-13

- Changed
- Improve the way build arguments are passed to the build through the command line.
- Allow more control of docker registry push.
- Don't print debugging output unless environment variable set.
- Updated dependencies: setuptools to 36.7.1, PyQt5 to 5.9.1.

### [14.0.4] - 2017-11-08

- Changed
- Add more ignore strings to npm build.

### [14.0.3] - 2017-11-06

- Changed
- PROG_FILES should have the same data type on Linux as Windows.

### [14.0.2] - 2017-11-06

- Changed
- Fixed issue with PROG_FILES import on Linux.

### [14.0.1] - 2017-11-06

- Changed
- Fixed issue with PROG_FILES import on Linux.

### [14.0.0] - 2017-11-06

- Added
- Added VisualStudioBuilder and VisualStudioWebsite.
- Added MSTestUnitTester.
- Added support for running remote commands on a different OS.
- Add cross-platform support to servermgr module.
- Moved Procedure classes to new expander module.

- Changed
- Moved Expander from fileutil to new expander module.
- Fix Node build on Windows.
- Allow servermgr.Server() usage to default to localhost.
- Renamed all Exceptions to Errors.
- Update setuptools to 36.6.0.
- Update virtualwrapper-win to 1.2.3.

- Remove
- netutil.remote_copy replaced by servermgr.ServerPath.copy.

### [13.2.3] - 2017-10-09

- Changed
- Fix Node build on Windows.

### [13.2.2] - 2017-10-03

- Changed
- Update GitPython to 2.1.7.

### [13.2.1] - 2017-09-28

- Changed
- Add more strings to ignore during npm commands.

### [13.2.0] - 2017-09-26

- Changed
- Improve Node.js builds.
- Update GitPython to 2.1.6.

### [13.1.4] - 2017-09-25

- Changed
- Inhibit un-checkout on PRDB close for Git.

### [13.1.3] - 2017-09-21

- Changed
- Speed up Git info clients by cloning to depth 1.

### [13.1.2] - 2017-09-21

- Removed
- IMPORT_GIT and IMPORT_PERFORCE don't work as expected.

### [13.1.1] - 2017-09-21

- Added
- IMPORT_GIT control flag.

### [13.1.0] - 2017-09-21

- Added
- Added support for Docker builds.
- Added Git support.

- Changed
- Update setuptools to 36.5.0.
- Update virtualwrapper-win to 1.2.2.

### [13.0.2] - 2017-08-28

- Changed
- Update requests to 2.18.4.
- Update setuptools to 36.3.0.
- Update slacker to 0.9.60.

### [13.0.1] - 2017-08-24

- Changed
- Removed extraneous period in package creation.
- Create the package using LZMA compression.
- Update chmod usage for better UNIX support.

### [13.0.0] - 2017-08-22

- Added
- Added build.GNUProduct class.

- Changed
- Improved build.GNUBuilder.

### [12.2.0] - 2017-08-18

- Added
- SERVICE_SIGNALS.restart for use with servermgr.Service on Linux.
- More debugging output from sysutil.syscmd.

- Changed
- Throw away output on Linux when remotely managing a service to avoid intermittent hang.

### [12.1.2] - 2017-08-17

- Changed
- Protect cms against fake git import.

### [12.1.1] - 2017-08-14

- Changed
- Add -t argument to ssh on remote Linux commands to prevent hangs.

### [12.1.0] - 2017-08-11

- Added
- Add Linux support to build.CxFreezeBuilder.
- Added LZMA (xz) creation support to fileutil.pack.

- Removed
- Remove workaround for Python 3.6.0 bug from build.CxFreezeBuilder.

### [12.0.0] - 2017-08-08

- Added
- Linux support for servermgr.Service and sysutil.syscmd with remote=True.

### [11.1.0] - 2017-08-07

- Added
- Added config property to configmgr.ConfigCollection.
- Added build.ConfigurationBuilder and build.ConfigurationProduct classes.

- Changed
- Update requests to 2.18.3.
- Update setuptools to 36.2.7.

### [11.0.3] - 2017-07-12

- Changed
- Improve symlink handing in build.NodeJSBuilder.
- Update p4python to 2017.1.1526044.
- Update PyQt5 to 5.9.

### [11.0.2] - 2017-07-05

- Changed
- Protect sysutil.syscmd against spaces in commands and argument names when using the shell.
- Minor NodeJSBuilder improvements.
- Improve lang.str_to_pythonval algorithm.
- Fix missing import.

### [11.0.1] - 2017-06-20

- Changed
- Add is_local property to servermgr.Server.
- Improve error checking on robocopy in servermgr.ServerPath.copy method.

### [11.0.0] - 2017-06-19

- Changed
- The handling of build information the build module has been overhauled to remove reliance on the command line and PRDB.
- Update requests to 2.18.1 and setuptools to 36.0.1.

### [10.0.3] - 2017-06-15

- Changed
- When sysutil.syscmd is run with useshell, pass the command and args as a string to Popen as suggested by the documentation.

### [10.0.2] - 2017-06-14

- Changed
- Catch any PyQt load failure in version module to protect against missing GNUC libs.
- Determine users home directory in a cross-platform way.
- Rename some variables.

### [10.0.1] - 2017-06-09

- Changed
- The node npm command needs to be run by the shell.

### [10.0.0] - 2017-06-01

- Added
- Converted the envcfg module to configmgr.
- Added Linux support.
- Added GNUBuilder.
- Added statemachine.StateMachine.reset method.
- Added statemachine.StateMachine.start method to facilitate crash recovery.

- Changed
- Update error related to Linux support.
- The servermgr.Server.run_command method should not run the command remotely if the server is local.
- Add more files ignored when build.NodeBuilder publishes.
- Updated dependencies: cx-Freeze to 5.0.2, requests to 2.17.3, slacker to 0.9.50.

### [9.0.0] - 2017-05-16

- Added
- Added support for using the node package.json file as a version file.

- Changed
- Change WMIObject type to a string to allow grabbing any available.

### [8.0.1] - 2017-05-08

- Added
- Added dependency on P4Python.
- Add privileged run option to psexec in sysutil.syscmd.

- Changed
- Upgrade setuptools to 35.0.2.
- Ignore more robocopy codes that indicate success in servermgr.ServerPath.copy.
- Fix issue with LoadBalancer management of a Server without DNS name resolution available.

### [8.0.0] - 2017-04-26

- Changed
- Raise ServerObjectManagementException on all COM and WMI connection errors.

### [7.1.0] - 2017-04-24

- Changed
- Improved build.MochaTest.

### [7.0.0] - 2017-04-24

- Added
- Require the unittest-xml-reporting package.
- build.PythonUnitTester.
- build.MochaTester.

- Changed
- Updated build for new build.Product definition.

### [6.0.1] - 2017-04-21

- Changed
- Update build.run_system_command for new syscmd usage.

### [6.0.0] - 2017-04-20

- Added
- servermgr.LoadBalancer.get_cache_content_group and flush_cache_content.

- Changed
- Changed servermgr.Server wmi_connect arg to defer_wmi.
- Let servermgr.Server make WMI connection when needed.
- Fixed statemachine unit tests.
- Update iispy.IISConfigurationSection to be more section generic.
- Upgrade setuptools to 35.0.1.

### [5.0.0] - 2017-04-17

- Added
- servermgr.Server.remove_directory method.
- ServerPath object for better remote file management.

- Changed
- servermgr.Server.run_remote_command method change to run_command.
- Allow servermgr.Server.run_command to take a string or list argument.
- Fixed issue with statemachine rollback.
- Allow the IP Address to be passed in to Server to get around lack of name resolution.
- Fix problems with LoadBalancer usage of Server objects.
- Provide enum for Service states.
- Delete WMI object reference before refreshing to prevent locking the WMI interface.
- Increase the wait time for service state checks.
- Return result from send in netutil.send_email.

### [4.4.0] - 2017-04-05

- Added
- Ability to pass credentials to sysutil.syscmd when running remotely.
- Ability to inhibit WMI connection on servermgr.Server instantiation.
- servermgr.Server.run_remote_command method.
- Provide servermgr.COMObject.disconnect() method.

- Changed
- Improve servermgr.ServerObjectManagementException.REMOTE_PERMISSION_ERROR wording.
- Allow servermgr.COMObject to be initialized with a win32com client object.

### [4.3.1] - 2017-04-03

- Added
- Provide log_filename property for Logger.
- Fix system command call in sqlscript.

- Changed
- Pin requirements to specific versions.

### [4.3.0] - 2017-03-31

- Added
- New envcfg module.

- Changed
- Fixed sqlscript usage of syscmd.

### [4.2.0] - 2017-03-29

- Added
- Authorization parameter to SQLScript.
- Authorization parameter to servermgr objects.
- Process management to servermgr.
- Ability to redirect output to a Qt widget.
- Added COM support to server mgr.
- Added IIS support to servermgr.Server.
- Check for server existence in servermgr.Server.
- Provide iispy.IISInstance.exists property.
- Default cmds.Commander option of --quiet.
- cmds.Commander --raise-on-error parameter to throw errors when parser problem.
- Ability to get current Logger.level.

- Changed
- Use closing and suppress from contextlib.
- Fix sys module usage.
- Allow SQLScript to be used in a with statement.
- Return output from iispy.IISInstance.reset.

### [4.1.1] - 2017-03-21

- Changed
- Updated DEFAULT_PRODUCT_DB.
- Make Logger logname argument required.

### [4.1.0] - 2017-03-20

- Added
- Added rollback method to StateMachine.
- Added exist property to Service.

- Changed
- Convert possible string to server object in LoadBalancer method.

### [4.0.0] - 2017-03-17

- Added
- Added the statemachine module.
- Added the servermgr module.
- Added requirement for slacker module.
- Added requirement for WMI module.

- Changed
- Update setuptools to 34.3.2.
- Throw RaiseAttribute when appropriate.

- Removed
- Removed the singleton implementations since those can be handled with global instances in Python.

### [3.0.0] - 2017-03-09

- Changed
- Allow fileutil.Expander use non-strings for replacement.
- Fix issue with use of variable named 'path' in sysutil module.
- Rename home directory variable.
- Update PyQt to 5.8.1.1.
- Update setuptools to 34.3.1.

### [2.0.1] - 2017-03-07

- Changed
- Fixed crash when the command is not in the driver.
- Fixed problem in fileutil.Expander.expand_directory() where it did not popd().

### [2.0.0] - 2017-03-03

- Changed
- Improve expansion condition evaluation when the condition contains a variable.
- Cleanup expression condition exception handling.
- Fix issue with Perforce integration.
- Rename iispy member function to be consistent.

### [1.0.1] - 2017-02-27

- Changed
- Fixed issues with XML parsing.
- Upgrade setuptools to 34.3.0.

### [1.0.0] - 2017-02-21

- Changed
- Fixed bad imports.
- Fixed bad return in str_to_pythonval.
- Change xml parser to standard in xml module.
- Rename constant in data module to uppercase.
- Fix issue in data module when returning columns in XML table.
- Upgrade PyQt5 to 5.8.
- Upgrade setuptools to 34.2.0.

### [0.12] - 2017-02-09

- Changed
- Improved Cmd error handling.
- Fixed import issue.

### [0.11] - 2017-02-09

- Added
- Created fileutil module from file-related init functions.

- Changed
- Moved system-related init functions to sysutil.
- Convert expander to a class.
- Don't raise custom exceptions inside standard ones.
- Fix typo in str_to_pythonval().
- Cleanup fileutil.spew().

- Removed
- Move procedure module to BatCave.

### [0.10] - 2017-02-07

- Changed
- Update setup.py to include all required modules.

### [0.9] - 2017-02-06

- Changed
- Update CxFreezeBuilder to handle Python 3.6.0 issue with process module.

### [0.8] - 2017-02-06

- Added
- sysutil.is_user_administrator()

### [0.7] - 2017-02-03

- Added
- Support for building Python applications using cx_Freeze.
- Support for debugging output during syscmd execution.
- Module for remote IIS administration.
- bool_to_str().
- Support for running commands on remote systems.
- Created netutil and sysutil modules.
- Require xmltodict (for new iispy module).
- Modules for network and system utilities created from __init__ functions.

- Changed
- Upgraded requests module.
- Moved is_debug from module initialization to lang submodule.
- Rename debug environment variable.
- Use new Python 3 super().
- Update syscmd to use new Python 3 subprocess module features.
- Cleanup imports.
- Inhibit return of stderr lines when ignorestderr is set in syscmd.

- Removed
- Serialization support from syscmd.

### [0.6] - 2017-01-27

- Changed
- Use USERPROFILE for default PRDB database.

### [0.5] - 2017-01-27

- Added
- CHANGELOG.rst.

- Changed
- Allow the command line parser to be passed in.
- Update the location of the default product database.

### [0.4] - 2017-01-25

- Added
- Unit tests.

- Changed
- When an application calls get_version_info(), return info for the app and not this module.
- Improved get_version_info() output format.

### [0.3] - 2017-01-17

- Added
- Support for deployment automation.

### [0.2] - 2017-01-16

- Added
- Support for building Node.js applications.

- Changed
- Improved output during automation.

### [0.1] - 2017-01-12

- Initial release.

<!-- end legacy manual entries -->
<!-- generated by git-cliff -->
[48.0.0]: https://github.com/Arisilon/BatCave/compare/47.1.1..48.0.0
[47.1.1]: https://github.com/Arisilon/BatCave/compare/47.1.0..47.1.1
[47.1.0]: https://github.com/Arisilon/BatCave/compare/47.0.0..47.1.0
[47.0.0]: https://github.com/Arisilon/BatCave/compare/46.0.1..47.0.0
[46.0.1]: https://github.com/Arisilon/BatCave/compare/46.0.0..46.0.1
[46.0.0]: https://github.com/Arisilon/BatCave/compare/v45.0.2..46.0.0
[45.0.2]: https://github.com/Arisilon/BatCave/compare/v45.0.1..v45.0.2
[45.0.1]: https://github.com/Arisilon/BatCave/compare/v45.0.0..v45.0.1
[45.0.0]: https://github.com/Arisilon/BatCave/compare/v44.0.2..v45.0.0
[44.0.2]: https://github.com/Arisilon/BatCave/compare/v44.0.0..v44.0.2
[44.0.0]: https://github.com/Arisilon/BatCave/compare/v43.2.3..v44.0.0
[43.2.3]: https://github.com/Arisilon/BatCave/compare/v43.2.2..v43.2.3
[43.2.2]: https://github.com/Arisilon/BatCave/compare/v43.2.1..v43.2.2
[43.2.1]: https://github.com/Arisilon/BatCave/compare/v43.2.0..v43.2.1
[43.2.0]: https://github.com/Arisilon/BatCave/compare/v43.1.1..v43.2.0
[43.1.1]: https://github.com/Arisilon/BatCave/compare/v43.0.1..v43.1.1
[43.0.1]: https://github.com/Arisilon/BatCave/compare/v43.0.0..v43.0.1
[43.0.0]: https://github.com/Arisilon/BatCave/compare/v43.0.0rc3..v43.0.0
[43.0.0rc3]: https://github.com/Arisilon/BatCave/compare/42.2.1..v43.0.0rc3
[42.2.1]: https://github.com/Arisilon/BatCave/compare/v42.2.0..42.2.1
[42.2.0]: https://github.com/Arisilon/BatCave/compare/42.1.0..v42.2.0
[42.1.0]: https://github.com/Arisilon/BatCave/compare/v42.0.4..42.1.0
[42.0.4]: https://github.com/Arisilon/BatCave/compare/v42.0.3..v42.0.4
[42.0.3]: https://github.com/Arisilon/BatCave/compare/v42.0.2..v42.0.3
[42.0.2]: https://github.com/Arisilon/BatCave/compare/v42.0.1..v42.0.2
[42.0.1]: https://github.com/Arisilon/BatCave/compare/v42.0.0..v42.0.1
[42.0.0]: https://github.com/Arisilon/BatCave/compare/v41.0.0..v42.0.0
[41.0.0]: https://github.com/Arisilon/BatCave/compare/v40.0.0..v41.0.0
[40.0.0]: https://github.com/Arisilon/BatCave/compare/v39.0.5..v40.0.0
[39.0.5]: https://github.com/Arisilon/BatCave/compare/v39.0.4..v39.0.5
[39.0.4]: https://github.com/Arisilon/BatCave/compare/v39.0.3..v39.0.4
[39.0.3]: https://github.com/Arisilon/BatCave/compare/v39.0.2..v39.0.3
[39.0.2]: https://github.com/Arisilon/BatCave/compare/v39.0.1..v39.0.2
[39.0.1]: https://github.com/Arisilon/BatCave/compare/v39.0.0..v39.0.1
[39.0.0]: https://github.com/Arisilon/BatCave/compare/v38.1.2..v39.0.0
[38.1.2]: https://github.com/Arisilon/BatCave/compare/v38.1.1..v38.1.2
[38.1.1]: https://github.com/Arisilon/BatCave/compare/v38.1.0..v38.1.1
[38.1.0]: https://github.com/Arisilon/BatCave/compare/v38.0.1..v38.1.0
[38.0.1]: https://github.com/Arisilon/BatCave/compare/v38.0.0..v38.0.1
[38.0.0]: https://github.com/Arisilon/BatCave/compare/v37.1.2..v38.0.0
[37.1.2]: https://github.com/Arisilon/BatCave/compare/v37.1.1..v37.1.2
[37.1.1]: https://github.com/Arisilon/BatCave/compare/v37.1.0..v37.1.1
[37.1.0]: https://github.com/Arisilon/BatCave/compare/v37.0.1..v37.1.0
[37.0.1]: https://github.com/Arisilon/BatCave/tree/v37.0.1

