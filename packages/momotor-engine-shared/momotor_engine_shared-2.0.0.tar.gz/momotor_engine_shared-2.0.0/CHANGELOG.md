# CHANGELOG



## v2.0.0 (2024-04-16)


## v2.0.0-rc.2 (2024-03-19)

### Breaking

* feat: convert to PEP420 namespace packages

requires all other momotor.* packages to be PEP420 too

BREAKING CHANGE: convert to PEP420 namespace packages ([`bddd7c4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/bddd7c48d3f63fe6ccea60bdb9be75eb9694b1dc))

### Refactor

* refactor: replace all deprecated uses from typing (PEP-0585) ([`5043246`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/50432464f68e9963576ec1d190657e7ee927e488))

### Unknown

* Merge remote-tracking branch &#39;origin/upgrade&#39; into upgrade ([`e5d8de8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/e5d8de83a342e345058ffb050dccf7f861d4c324))

* doc: update dependencies ([`92c7b65`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/92c7b65ae8b4b740221ab47436c085fa7225082d))


## v2.0.0-rc.1 (2024-02-06)

### Breaking

* feat: drop Python 3.8 support, test with Python 3.12

BREAKING CHANGE: Requires Python 3.9+ ([`dedba4a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/dedba4a38cc392a87179179882b4ceaf9560e3e9))

### Chore

* chore: add Python 3.10 and 3.11 classifiers ([`e6b117e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/e6b117e454fc346f1de78150d2a78fafb2f69e6e))

### Refactor

* refactor: update type hints for Python 3.9 ([`ab73d16`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/ab73d16c31083c42e6e8e4c04f371daaa6d70d77))

### Test

* test: update to latest Pytest ([`00893a9`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/00893a926a3a4de885cfd00f9666c1fd83df244b))

### Unknown

* doc: update documentation theme and other documentation updates ([`5f90b1d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/5f90b1d13374448eb268f6487e311262b4bce4c3))


## v1.4.2 (2022-06-10)

### Fix

* fix: typo in dependencies ([`8c87f28`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/8c87f2844fed82f929d509bb43b2e30fea849ada))

### Unknown

* 1.4.2

&#39;chore: bump version number&#39; ([`38adc82`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/38adc82f2b6a701e977319acf0ac7c9898318ed3))

* Merge remote-tracking branch &#39;origin/master&#39; ([`b51fcb0`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/b51fcb05e8edc35627b52d7ea7e842d3f8660ace))


## v1.4.1 (2022-04-04)

### Fix

* fix: correct type annotations for (async_)log_exception method ([`b59f5d2`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/b59f5d21b48721be6954099a90ab6d44fca03462))

### Unknown

* 1.4.1

&#39;chore: bump version number&#39; ([`4934f7f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/4934f7fe037d18bedebddcec5e6bc56f346a44b1))


## v1.4.0 (2022-01-24)

### Feature

* feat: make caller_name argument to (Ex)LockSet optional ([`ffbc23e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/ffbc23e50334342d9e19b1ec4088ea8abfa92489))

### Unknown

* 1.4.0

&#39;chore: bump version number&#39; ([`a867c54`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/a867c54f10d5096b584ceaeaa069643a87c8a5e1))


## v1.3.0 (2021-12-06)

### Feature

* feat: moved lockset module from broker ([`9d80d0c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/9d80d0c2450ff88c7adf4aee04fee0d7f771715e))

### Unknown

* 1.3.0

&#39;chore: bump version number&#39; ([`992831e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/992831e113b387ca7cbd7f3f48f7e66e0d54e6ee))


## v1.2.1 (2021-11-04)

### Chore

* chore: link to documentation with the correct version number ([`38c1b12`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/38c1b1237ac6ff2e2ca8795dc186900bfb9a5306))

### Fix

* fix: save exception info before submitting log message to executor ([`431ec1f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/431ec1f949dc83572767e8cddb1c9195a721fe3f))

### Unknown

* 1.2.1

&#39;chore: bump version number&#39; ([`03f36a7`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/03f36a76530c81f4d05e075aaf450dbba2e74aee))


## v1.2.0 (2021-10-01)

### Feature

* feat: implement AsyncLogWrapper.handle ([`329c283`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/329c2830fe13f209580e329acc6841d4d7ff64ec))

### Unknown

* 1.2.0

&#39;chore: bump version number&#39; ([`072cd91`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/072cd911f5a00a3889bac5155301190c294effde))

* Merge remote-tracking branch &#39;origin/master&#39; ([`eaaa133`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/eaaa133fb50ec976fb54b6a627eced310e9369f2))


## v1.1.1 (2021-10-01)

### Fix

* fix: correctly wait on completion after log message has been sent to the Python logger; always wait on completion for critical messages and messages with exception info ([`364bb8d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/364bb8d1c10694d083da2cb2a66e8f06a354e769))

### Unknown

* 1.1.1

&#39;chore: bump version number&#39; ([`c5d2905`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/c5d290545e32c744ce40e398945e2d3e458cae48))


## v1.1.0 (2021-10-01)

### Chore

* chore: update project files ([`88ef9df`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/88ef9dfe7247975a33d9f3c8839d98516cadfe8f))

* chore: update project files ([`267016b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/267016bb24551fad8b5fb3c2c066ee70e94c223b))

* chore: update project files ([`bdb976f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/bdb976f1959a397a9de6b02d8bb3a5ee4c40b249))

### Feature

* feat: moved `log` module from momotor-django package, changed the way async logging is handled ([`7a58618`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/7a586183c1fc6d728a0ca006cfd288337ea581f5))

### Fix

* fix: remove dependency on Django ([`a2cdb8b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/a2cdb8b245dd32ec8c1c18aeb62fd3d825269311))

### Unknown

* 1.1.0

&#39;chore: bump version number&#39; ([`d5977b0`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/d5977b05208044354b49745f7c0dc080b2ad9ab4))

* doc: fix various Sphinx warnings ([`2be5fd9`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/2be5fd959301d7fdd2854e45411959232bb2dc38))

* doc: add log module to documentation ([`3a65ec6`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/3a65ec64584d7e6b93098723c06fa2b44ff18294))


## v1.0.1 (2021-02-11)

### Chore

* chore: update/move PyCharm module files ([`44a96bb`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/44a96bb10c0a156c1ee5962e82067202302ab5ad))

* chore: update Python SDK ([`0533760`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/0533760a47ce3c9fb3439d5f46d114761bf1f139))

* chore: update Python version classifiers ([`448f909`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/448f909feacf6e31d86fc1cb1e3fa0802fb2915c))

* chore: added missing [docs] extra ([`631e714`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/631e7141617e7df62326d6b04266e01063f08b9d))

### Fix

* fix: __doc__ is not available when running Python with the -OO option ([`0e66a4f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/0e66a4f124776cf09fe1b4d24eab469100e85c77))

### Unknown

* 1.0.1

&#39;chore: bump version number&#39; ([`09fbc9c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/09fbc9c1e3d716483e20f9d0b60f9f637cf274b6))


## v1.0.0 (2020-08-17)

### Breaking

* feat: changed minimum Python requirement to 3.7

BREAKING CHANGE: Requires Python 3.7 or higher ([`26286b0`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/26286b05ad4e2c3dc44e25e729dba98e1fed2fc1))

### Unknown

* 1.0.0

&#39;chore: bump version number&#39; ([`9d7e0ee`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/9d7e0ee98ef668c48659149893cf285d5fc88ec5))

* doc: small documentation fixes ([`fe838e9`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/fe838e9a1abf5478f788b73502d1c012f35c4bc8))

* Merge remote-tracking branch &#39;origin/master&#39; ([`d9985f2`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/d9985f2a3176a74ec26e889bffffaeab02c51244))


## v0.7.0 (2020-04-23)

### Feature

* feat: version bump to make `annotate_docstring` available as new feature ([`f82c77d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/f82c77d20f877bba8d29f9b05fc1ca7569d72888))

### Unknown

* 0.7.0

&#39;chore: bump version number&#39; ([`87fe980`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/87fe980d72269cf9f1689bfcdf492e7af9ffe823))

* project: correct docs/build exclusion ([`1b36df0`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-shared/-/commit/1b36df0f86a216cc10f1f22e061197397ab4e57f))
