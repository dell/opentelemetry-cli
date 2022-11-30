# Changelog

<a name="0.3.0"></a>
## 0.3.0 (2022-11-30)

### Changed

- ⬆️ Upgrade docker/metadata-action digest to 314ddf6 [[14fa9ea](https://github.com/dell/opentelemetry-cli/commit/14fa9ea3219a8f4e0e8af31381c89865332ea580)]
- ⬆️ Upgrade docker/login-action digest to f75d088 [[7e82b7a](https://github.com/dell/opentelemetry-cli/commit/7e82b7aec631cb189a0209c51fa8fd89cbb2eac3)]
- ⬆️ Upgrade OpenTelemetry libs to ~1.14.0 [[8018b69](https://github.com/dell/opentelemetry-cli/commit/8018b699f6cd246fda4e4ed578b042f60d628504)]
- ⬆️ Upgrade dependency pytest-cov to v4 [[0bd2302](https://github.com/dell/opentelemetry-cli/commit/0bd2302ea2ca7568e3a79a05dcec3589450f0597)]
- ⬆️ Upgrade ghcr.io/open-telemetry/opentelemetry-collector-releases/opentelemetry-collector Docker tag to v0.66.0 [[f7b4003](https://github.com/dell/opentelemetry-cli/commit/f7b4003c1af21fb55b72df724811f5223cfcd879)]
- ⬆️ Upgrade dependency Click to v8 [[2fb49f0](https://github.com/dell/opentelemetry-cli/commit/2fb49f02c0cd86c89169fdea277daec582d426f2)]
- ⬆️ Upgrade python Docker tag to v3.11.0 [[a284ddc](https://github.com/dell/opentelemetry-cli/commit/a284ddc4e2a167c9bb8ecca7102a2462ffe534f1)]
- ⬆️ Upgrade dependency typing-extensions to ~4.4.0 [[4fa0b6b](https://github.com/dell/opentelemetry-cli/commit/4fa0b6bf8006d4106427a59fef7c05f6e34c94aa)]
- 🔧 Add python 3.11 to test action [[29645d7](https://github.com/dell/opentelemetry-cli/commit/29645d71802cd5ee4b6b0507fa65d4a78b9894d7)]
- ⬆️ Upgrade docker/setup-buildx-action digest to 39a1a82 [[727f7c8](https://github.com/dell/opentelemetry-cli/commit/727f7c83d2b411366a8d4a08026aec2552d5d9d0)]
- ⬆️ Upgrade docker/build-push-action digest to 175d02b [[1b23cce](https://github.com/dell/opentelemetry-cli/commit/1b23cce9c4857b2b0bfcde2f61846c3fa4f70238)]
- ⬆️ Align dependencies for pytest 7.2.0 [[b2a0102](https://github.com/dell/opentelemetry-cli/commit/b2a0102f085ad553bf4fcccfa3196392fbe7e36c)]
- ⬆️ Bump pytest from 6.2.5 to 7.2.0 [[fc9aa3a](https://github.com/dell/opentelemetry-cli/commit/fc9aa3a080a285da69ca5ab777018bd05802ede2)]
- ⬆️ Update poetry to 1.2.2 [[a61754c](https://github.com/dell/opentelemetry-cli/commit/a61754c42bd6f72551641ed130d857bf686523a4)]
- ⬆️ Bump OpenTelemetry libs to 1.13.0 [[ed557f0](https://github.com/dell/opentelemetry-cli/commit/ed557f03d0414eb2c6c6162ecd7f6646f65263e6)]
- ⬆️ Update minimum Python version to 3.7 [[d12df33](https://github.com/dell/opentelemetry-cli/commit/d12df33897ab1695055db11f0a4151e155f360e7)]
- ⬆️ Bump actions/setup-python from 3 to 4 [[a877d74](https://github.com/dell/opentelemetry-cli/commit/a877d74d8af75d57988b7bed0d6d52cc41d4e16f)]
- ⬆️ Bump docker/metadata-action from 3.3.0 to 4.1.1 [[d0610ba](https://github.com/dell/opentelemetry-cli/commit/d0610baba892d93256cbd8b936c8075f9eecf2a3)]
- ⬆️ Bump docker/login-action from 1.9.0 to 2.1.0 [[69e7d46](https://github.com/dell/opentelemetry-cli/commit/69e7d46de0ab9026f9a9285e5a07ad00b33f244e)]
- ⬆️ Bump docker/build-push-action from 2.10.0 to 3.2.0 [[79356f7](https://github.com/dell/opentelemetry-cli/commit/79356f76302ad32d1f4fe864028eaf1743107528)]
- ⬆️ Bump docker/setup-buildx-action [[0c796ea](https://github.com/dell/opentelemetry-cli/commit/0c796ea262207ea0c498d991a43e297f7c88dbee)]
- 🚚 Move dependabot config to correct place [[473ffb4](https://github.com/dell/opentelemetry-cli/commit/473ffb4aadbcc2e3c4beea8c384c463eaea40ed1)]
- 🔧 Add dependabot config [[90623ba](https://github.com/dell/opentelemetry-cli/commit/90623baacd4cfc50e646c178b5f83b2530a6a247)]

### Removed

- 🔥 Remove unused files [[781b884](https://github.com/dell/opentelemetry-cli/commit/781b884cfddc9d9089e6436745860080651395be)]

### Fixed

- 💚 Set different cache key for each python version [[36e5bad](https://github.com/dell/opentelemetry-cli/commit/36e5bad3ed4c0b506eef593dec898d7b6fff6bf1)]
- 💚 Add otelcol service container to test action Fixes [#19](https://github.com/dell/opentelemetry-cli/issues/19) [[03a5e44](https://github.com/dell/opentelemetry-cli/commit/03a5e443e63cb2db9d36b0ed41e018a5a0533c6b)]
- 🐛 Fix entrypoint on docker image [[b3ee4de](https://github.com/dell/opentelemetry-cli/commit/b3ee4dee35088187f1203b8253b3923a37a66253)]

### Miscellaneous

- 📝 Add python 3.11 pypi classifier [[4c75568](https://github.com/dell/opentelemetry-cli/commit/4c755683098212fd6bf3865838da0190b3dbb580)]
-  👷 Exclude the collector from OTel library check [[5a81058](https://github.com/dell/opentelemetry-cli/commit/5a81058180171399a881493daa1a74ff684ebac3)]
-  👷 Group all OpenTelemetry libs in renovate [[800c301](https://github.com/dell/opentelemetry-cli/commit/800c301b6e3b2e03bbba869c3e7fd4456b5d607d)]
-  👷 Enable automerge for minor renovate updates [[1baf779](https://github.com/dell/opentelemetry-cli/commit/1baf7798d088dcf98e667a1f2469a84ac1318c5f)]
-  👷 Disable dependabot in favor of renovate [[1d218d7](https://github.com/dell/opentelemetry-cli/commit/1d218d73b418225194f6c7ad89709ee21aaf5acd)]
-  👷 Add renovate config [[f5c6ba1](https://github.com/dell/opentelemetry-cli/commit/f5c6ba16e3a49ca259cffd7cc68fb8c9eccdf831)]
-  👷 Remove caching from CI [[9fde674](https://github.com/dell/opentelemetry-cli/commit/9fde6744c97e4bb1c3d9c2ae55cae37ce740a9ca)]
-  👷 Actions: add python matrix [[6b29ef2](https://github.com/dell/opentelemetry-cli/commit/6b29ef241130918141cfd3a39052192ee5fcae70)]
- 📝 Fix dockerhub badge url [[66d95a4](https://github.com/dell/opentelemetry-cli/commit/66d95a46a5f99d88a894b64ae162d8512be2bc76)]
- 🧑‍💻 Set yaml indent to 2 spaces [[2b88e56](https://github.com/dell/opentelemetry-cli/commit/2b88e566a49790b2a43c1402785af912297aa0f1)]
- 📝 Add codecov badge [[68fecc4](https://github.com/dell/opentelemetry-cli/commit/68fecc4927ce4b881397cdf1094a916c0c5f7bbf)]
- 📝 Add pypi badge [[1f740b3](https://github.com/dell/opentelemetry-cli/commit/1f740b372d10ee1e38455fae9b9c6fc06790fc96)]
-  Update docker-publish.yml [[a20ed1c](https://github.com/dell/opentelemetry-cli/commit/a20ed1c8a0248aa8bd7317035ada53b1a2307456)]
-  Add pypi to readme [[862cdc6](https://github.com/dell/opentelemetry-cli/commit/862cdc6cafb82e0ba0a4eb3eb74d3d41b18bc4c7)]
-  Update README.md [[db008c5](https://github.com/dell/opentelemetry-cli/commit/db008c5b6a51df015d57a653b8e3db3bb98056b9)]
-  👷 Add github action for build &amp; test [[72ec444](https://github.com/dell/opentelemetry-cli/commit/72ec444423fe2674246d0c4dde8e309423b76050)]
-  Update README.md [[a5a752b](https://github.com/dell/opentelemetry-cli/commit/a5a752b53e4ba2668ff1ae25708287f5c0cb0ad2)]
- 📄 Add license file Fixes [#21](https://github.com/dell/opentelemetry-cli/issues/21) [[17d759e](https://github.com/dell/opentelemetry-cli/commit/17d759e69098af8d753eb7781239985a5c1dfed6)]
- 📝 Align badge style [[0ac5663](https://github.com/dell/opentelemetry-cli/commit/0ac56635da9e281bde3907f2e8d2b4580c86a637)]
- 📝 Add gitmoji badge [[7c92585](https://github.com/dell/opentelemetry-cli/commit/7c9258534809d8ee0ffbc93b0b08e38b68ef05eb)]
-  Add badges to the readme [[2a41b05](https://github.com/dell/opentelemetry-cli/commit/2a41b057e8558544c1c2d877c721da5885932471)]
-  Create docker-publish.yml [[d228e68](https://github.com/dell/opentelemetry-cli/commit/d228e687fe832e1be9a75e6aa605a4727e629a3f)]
-  Create CODEOWNERS [[e3ed9ab](https://github.com/dell/opentelemetry-cli/commit/e3ed9abdbcb2152cd33097752d06633545b04d66)]
- 🔨 Use poetry to upload package [[c4662b1](https://github.com/dell/opentelemetry-cli/commit/c4662b13d70aa51222323c952b6481dd4a977fab)]
- 📝 Update docs with new repo name [[d6f67e2](https://github.com/dell/opentelemetry-cli/commit/d6f67e2f4a4f0597a6a115f1b65493380b9e3d4d)]


<a name="0.2.0"></a>
## 0.2.0 (2022-08-24)

### Added

- ✨ Add support for array attributes Fixes #7 [d60fb6b]
- ✅ Include &#x60;str:&#x60; attribute prefix in tests [b8cf709]
- ✨ Support str: prefix for attributes Fixes #6 [6d5c574]
- ✅ Add tests for updown counter from CLI [f19c923]
- ✅ Add tests for updown counters [13dffb8]
- ✨ Add UpDownCounter support to otel-cli metrics Fixes #5 [af94026]

### Changed

- ⬆️ Bump opentelemetry libs to 1.12.0 [8707340]

### Removed

- ➖ Remove mypy pre-commit hook [09428c8]
- ➖ Remove pytest-otel [a93f4f9]

### Miscellaneous

- 📝 Update command name in docs to &quot;otel&quot; [fe32825]
- 📝 Add documentation about updown counters [3053e6f]


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
