# Changelog

<a name="0.1.3"></a>
## 0.1.3 (2022-08-10)

### Added

- ✅ Fix basic CLI test [322fef5]
- ✨ Add &#x60;-v|--version&#x60; support Fixes #9 [f6bd0ad]
- ✨ Support attribute type conversion in spans [8a5a3b6]
- ➕ Add myst_parser for markdown docs [030c8f0]
- ✅ Add tests for utils module [32590c0]
- ✨ Support int, float, bool attributes in metrics [9356f16]

### Changed

- 🚸 Remove deprecated issue template [c531d17]
- 🚸 Update issue templates [f86bf98]
- 🎨 Format test_utils.py [530bd58]
- ⬆️ Upgrade pip, coverage versions [ab3d6ba]
- ⬆️ Upgrade Sphinx to version 5.0.2 [f9818a9]

### Fixed

- 🐛 Add time_ns polyfill for Python 3.6 [5b2d983]
- 🐛 Fix typing import issue for Python&lt;3.8 [d6912ee]
- 🐛 Use CLI version as default, not &quot;0.0.1&quot; Fixes #1 [2d1c1fb]

### Miscellaneous

- 🧱 Update bump2version for poetry [a1f63b7]
- 🔨 Set up Poetry instead of setuptools [bec156d]
- 💥 Rename command to &quot;otel&quot; instead of &quot;otel-cli&quot; [bb734d8]
- 🧑‍💻 Add flake8 pre-commit hook [30c5968]
- 🧑‍💻 Add pre-commit hooks [c24e117]
- 📝 Document attribute type conversion [44f33ca]
- 🔨 Avoid git tag in b2v since we add a changelog [f124607]
- 🔨 Auto-tag Docker image [866df90]
- 🔨 Automatically determine tag from setup.cfg [e49b458]
- 🔨 Create GitHub releases from Makefile [01cbfeb]
- 📝 Add documentation for counters in README [553db5e]
- 🩹 Use single logic for remove_prefix [96c0fe0]
- 🔨 Make changelog commit non-interactive [86b73a1]


<a name="0.1.1"></a>
## 0.1.1 (2022-06-24)

### Added

- ✨ Add attribute support to otel-cli metric counter [f7c060e]

### Miscellaneous

- 🔨 Makefile path fixes [b932c02]
- 🔨 Change bump2version message and tag format [982533e]
- 📝 Remove history, add readme &amp; changelog to pypi [89b77ac]
- 📝 Add changelog, autogen by gitmoji-changelog [ce8d2e9]


<a name="0.1.0"></a>
## 0.1.0 (2022-06-23)

### Added

- ✨ Add support for counter metric [f55e14d]

### Changed

- ⬆️ Upgrade bump2version to 1.0.1 [701cc62]
- 🚚 Rename test_otel to split by signal type [8226384]

### Fixed

- ✏️ Convert init to double quotes [ab262b8]
- 🐛 Fix bump2version regex [a723da6]

### Miscellaneous

- 📝 typo: fix project name in docs [22b458b]
- 📝 Update README with some examples [2760f7d]
