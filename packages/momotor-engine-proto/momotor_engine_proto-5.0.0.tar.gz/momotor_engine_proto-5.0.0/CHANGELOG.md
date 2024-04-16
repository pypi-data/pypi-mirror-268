# CHANGELOG



## v5.0.0 (2024-04-16)


## v5.0.0-rc.2 (2024-03-21)

### Breaking

* feat: convert to PEP420 namespace packages

requires all other momotor.* packages to be PEP420 too

BREAKING CHANGE: convert to PEP420 namespace packages ([`96e50c1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/96e50c14c79526071eaab3527b4c1dc922c0097f))

### Chore

* chore: update dependencies ([`e4877cb`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/e4877cb9da2f603b18a0bf2dead3dd1c9cb60d92))

### Feature

* feat: upgrade to latest GRPC version ([`8e2d7ef`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/8e2d7ef5b69f045928da34c0e24a46d907ed3ea4))

### Refactor

* refactor: replace all deprecated uses from typing (PEP-0585) ([`67e3b4f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/67e3b4ffcc10db8d1db5f4cb625c6ccaabc280d2))

### Unknown

* doc: update dependencies ([`6596288`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/6596288a0278c19e7f8e050b456b9d55f4540ea9))


## v5.0.0-rc.1 (2024-02-05)

### Breaking

* feat: drop Python 3.8 support, test with Python 3.12

BREAKING CHANGE: Requires Python 3.9+ ([`c4ddf3e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/c4ddf3e51998a5d5b82b78d5390e31897ec11ca3))

### Chore

* chore: add Python 3.10 and 3.11 classifiers ([`0294e4a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/0294e4ab9b570519eba6f0f4db8b3d6f2b7905fa))

### Refactor

* refactor: update type hints for Python 3.9 ([`d075761`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/d075761af9a246be88a41f37eca23bc0a93b4c3d))

### Test

* test: update to latest Pytest ([`0cbae15`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/0cbae150213857f8c2df03f836801342e31fc8b3))

### Unknown

* doc: update documentation theme and other documentation updates ([`10a117c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/10a117c99c2df89b492ed3fea16df96ac6cf4517))

* doc: update intersphinx links for momotor.org docs ([`5a60a30`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/5a60a30e57bbbba20471224eecea2e1353bb40fb))


## v4.4.0 (2022-03-14)

### Chore

* chore: link to documentation with the correct version number ([`aeaf50f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/aeaf50f56650236abd5ddf6132de8cbff65b7dcf))

* chore: cleanup CHANGELOG.md [skip-ci] ([`be95be9`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/be95be97949ed68a5fa37bd387a6ddc553398086))

### Feature

* feat: change tool message into toolset ([`16b77aa`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/16b77aa2730cf9b57279c2e104ebea7bd2fcd87e))

* feat: use a dataclass to represent tools and aliases ([`081e9cb`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/081e9cbb4ebf22beea7aaa7022eac2af09f39aad))

* feat: move `tools_to_message` from cli package to proto package ([`f943211`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/f9432114feb2975673797789ad323c9675fccc68))

* feat: add tool list to GetTaskResponse message ([`baf21b2`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/baf21b2f5dd63460d0725c0e1f3c18f8a49d836b))

### Fix

* fix: handle missing tool message ([`f85d5a6`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/f85d5a6451264fee98e39323f6a1b817b58a844f))

### Unknown

* 4.4.0

&#39;chore: bump version number&#39; ([`255f60b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/255f60bce496ed8aadffa7e3eae849552a8b91d0))


## v4.3.0 (2021-10-22)

### Chore

* chore: update version pin of base58 package ([`9abd691`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/9abd6913c4bda31cca9ccf32177c954f60e582aa))

* chore: revert version number ([`9d86913`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/9d86913aac924dbc64e2c42eeb0553e41a21d277))

### Feature

* feat: add `taskNumber` field to AssetQuery message ([`bd88832`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/bd888327a88d210673e79fbea50559294299f278))

* feat: extend TaskId message with `taskNumber` field, add helpers to convert step-id with task-number to step-task-id (Closes #12) ([`35a9c67`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/35a9c6755e37a99a157c8a98a737cdc46d50388d))

### Unknown

* 4.3.0

&#39;chore: bump version number&#39; ([`3080d66`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/3080d666ddcafb24637f73b65a44bd14d4e3901d))

* 4.3.0

&#39;chore: bump version number&#39; ([`03821fa`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/03821fa21830aae0fda4582946ab0a3401ec46d1))


## v4.2.1 (2021-10-01)

### Chore

* chore: update project files ([`11ee9a1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/11ee9a1c5e5e401e3277ea4f716dd69b51214ed5))

* chore: update project files ([`d240cdc`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/d240cdce1bde081ba62bffb458a1382a742ec4c3))

* chore: project file updated ([`a8d6431`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/a8d6431c8bc23add9de6918297eb4576ee4223bd))

### Fix

* fix: use async logging ([`ca7e454`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/ca7e4540f810a5057ccbc58f810be791443f847f))

### Unknown

* 4.2.1

&#39;chore: bump version number&#39; ([`fc43a13`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/fc43a138bdeb05376db21827f3e6ae4d177e8e23))


## v4.2.0 (2021-03-15)

### Chore

* chore: list Python 3.9 in the classifiers ([`e78c1de`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/e78c1deceabf1b7d83ba97fdcf7d7237cc07389a))

* chore: update protobuf dependency to ~3.15.6, update grpcio-tools dependency to ~1.36.1 ([`59a2756`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/59a27564c228235663f12d712e76654db3a3910f))

* chore: correct url to commit in CHANGELOG.md ([`0d3b9a9`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/0d3b9a9341af01cefe6778878f40a4d8e84d7fdc))

### Feature

* feat: add priority field to CreateJobRequest, JobStatus and GetTaskResponse ([`34b35e4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/34b35e4045b2c83364ea9042114950ed0a08f7d4))

### Fix

* fix: remove unused GetJobRequest/GetJobResponse. Add validator for GetTaskRequest ([`7881b14`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/7881b14a134b18ce716ac2f0eef50e545744299e))

### Unknown

* 4.2.0

&#39;chore: bump version number&#39; ([`566f78d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/566f78dbaadfa68f9e3825628e07606b05835f75))

* doc: update docs ([`9a183ad`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/9a183ad3acfec3b14efc1a1f3da40687091d29b3))


## v4.1.1 (2020-11-13)

### Chore

* chore: fix url in CHANGELOG.md ([`375e8c0`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/375e8c01deeb42f5ded75769410ad86b7f6fc968))

### Fix

* fix: always send pings, even if there was no data ([`e004f60`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/e004f6042aec9ddb3c678549e25296159f51a8e0))

### Unknown

* 4.1.1

&#39;chore: bump version number&#39; ([`1238db2`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/1238db20dd7fb8d99412f4e3f54e0ca6219664eb))

* Merge remote-tracking branch &#39;origin/master&#39; ([`fd065c1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/fd065c12041b07d608594e2eaf922db87fb56f28))


## v4.1.0 (2020-11-05)

### Chore

* chore: rebuild pb2 files ([`b724317`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/b724317cce23066e51a4ea6058ce8ec5f98f0ad7))

* chore: update/move PyCharm module files ([`1efb674`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/1efb674da280938f6c4f4e6bbf4d299f0bccec1c))

### Feature

* feat: update grpclib to latest, set a low keepalive time, make it configurable ([`7c94095`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/7c94095cb8f02cdf4de39de9caae7b940e9e8de0))

### Unknown

* 4.1.0

&#39;chore: bump version number&#39; ([`52ee90b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/52ee90b19a11f78dabd2f859075fdda02d6fcf88))

* doc: correct commit url in CHANGELOG.md ([`00af2f5`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/00af2f55239e59350f05d3accece2856b3de4162))


## v4.0.1 (2020-10-23)

### Chore

* chore: update Python SDK ([`bf9641a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/bf9641a9b020584d586fdd14cb30da26bd65cdfc))

* chore: update Python version classifiers ([`244b0a8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/244b0a8ba16150100cd7c52a0ac324412564ef18))

### Fix

* fix: the loop parameter is deprecated ([`024d0d3`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/024d0d317bd07b3d4511568cfd323ef37abeb872))

### Unknown

* 4.0.1

&#39;chore: bump version number&#39; ([`862e369`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/862e369c3a923716eee4884c2b1e265f3ffc862b))


## v4.0.0 (2020-08-17)

### Breaking

* feat: changed minimum Python requirement to 3.7

BREAKING CHANGE: Requires Python 3.7 or higher ([`8fcc8b2`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/8fcc8b20ec150bcc68981716a4fb396aeb981d1c))

### Unknown

* 4.0.0

&#39;chore: bump version number&#39; ([`a5b4504`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/a5b45040cf7f6534195f04c184860d3a0d0beb59))


## v3.0.1 (2020-06-29)

### Fix

* fix: bump grpclib, grpcio, and protobuf versions ([`0108a35`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/0108a359b74177abef92ebf2086939a9803f0143))

### Unknown

* 3.0.1

&#39;chore: bump version number&#39; ([`f030a31`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/f030a31614c1b4aefd7e551910a65b257598c290))


## v3.0.0 (2020-04-23)

### Breaking

* feat: move query related validators into momotor.rpc.validate.query, document validators

BREAKING CHANGE: renamed momotor.rpc.validate.shared to momotor.rpc.validate.base, renamed momotor.rpc.validate.types to momotor.rpc.validate.query, moved momotor.rpc.validate.shared.validate_query_field() to momotor.rpc.validate.query ([`a8ab9e0`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/a8ab9e0ec44db1cec26c42117bf96bef5092d9c5))

### Chore

* chore: increase default chunk size from 256KiB to 8MiB ([`8f680af`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/8f680afc4ac9f89ded47a0ca6365ab4b705fa13b))

### Feature

* feat: move query related validators into momotor.rpc.validate.query

doc: document validators ([`0fc268c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/0fc268c6476dd3af2269075605d723bb5b3e96c3))

### Unknown

* 3.0.0

&#39;chore: bump version number&#39; ([`fdd9439`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/fdd94391ca7cf5292c86eeabfe1ae601d7de9dc7))

* doc: added introduction texts for most modules ([`fc62f2b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/fc62f2bc44a0a0b196d43cbcf914fc138ee2c82a))

* doc: document const.py ([`3a603f1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/3a603f15bc0b706c0725942e30a7b8918fed86d6))

* revert: feat: move query related validators into momotor.rpc.validate.query

This reverts commit 0fc268c6 ([`4e81334`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/4e81334b3da1c7f417af525abd423aa416a6c9c6))

* project: update version requirement for momotor-engine-shared ([`af4ecc8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/af4ecc8fed8b0ab2ba1109885ba133917eed0de9))

* revert: doc: document validators

Fixing commit message even more

This reverts commit 77aa1b1d ([`ee45872`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/ee458722b616a5eefaba50366c60e773912f7c4d))

* doc: document validators

feat: move query related validators into momotor.rpc.validate.query ([`77aa1b1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/77aa1b1dfecfab8d11a054bf268a3b94d284e404))

* revert: doc: document validators feat: move query related validators into momotor.rpc.validate.query

Fixing commit message

This reverts commit bab952b9 ([`bc1e5ce`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/bc1e5ce9ee536b41eaf7afb4d5342b5581efe145))

* doc: document validators
feat: move query related validators into momotor.rpc.validate.query ([`bab952b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/bab952b9dc33c6202d52fb3a88d73dfd89dc5055))

* doc: document status ([`6d4f0f2`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/6d4f0f23992434a6bb0ad24f421e49a4ed86f33f))

* doc: document shared state ([`8e23b2a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/8e23b2af8f9d28fc69e898af17d796f7fcba65cd))

* doc: document resources ([`879bfe6`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/879bfe61afb50f0372c74072be815a726ae9c88f))

* doc: document identity hash on module level ([`754c09a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/754c09a771139207232f2c19c7c4602160338e24))

* doc: add digest_size on identity hash module for PEP452 compatibility ([`854d0a5`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/854d0a539d51c294fc7675884ee16f8b5851df24))

* doc: document hash ([`e52c7c7`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/e52c7c74fd8bd76f9313e5aa55c6e5457c920028))

* doc: document exceptions ([`2ea64d0`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/2ea64d03f2f13165504c24503e94dc89a1c26dec))

* doc: document momotor.rpc.auth ([`c19e8c6`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/c19e8c6eab84e959e53a9dbf565edcd28bf2b229))

* doc: document momotor.rpc.asset ([`31c43b8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/31c43b8cb5a84d3874071f9c09670f84b91bf315))

* doc: add missing momotor.rpc.proto.auth ([`675a326`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/675a3262034afecc30e66e5fba0138d391787182))

* doc: update references ([`33ec74d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/33ec74d7032807fb7337770b12a588eb667ef2dd))

* doc: correct Sphinx&#39; conf.py ([`ebdb3c3`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/ebdb3c376bafb5911ce14cfd209631045d4372df))

* doc: add protobuf definition files documentation ([`cb2d8f7`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/cb2d8f77ddeb881575d4b893c15c2bf0d09adb7d))

* doc: added skeleton for docs ([`debeec3`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/debeec3d83e6e7e2626ef5e93620bacde2bcdd45))


## v2.12.0 (2020-03-19)

### Feature

* feat: subclass h2&#39;s DummyLogger for compatibility ([`5a3f515`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/5a3f51554e3d4648fd0bf2066ce8304603a1422f))

### Refactor

* refactor: calling task.result() is redundant ([`4ee30e5`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/4ee30e5a4dc7ac3a558c2dcc9f3166bb52bbbf52))

### Unknown

* 2.12.0

&#39;chore: bump version number&#39; ([`82ab91c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/82ab91cc30ced3dbf7b6d2d33982e144a8f0c897))

* revert: build: use a fork of h2 to work around #9

This reverts commit a9721e19 ([`59673b4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/59673b4f1390628b3cc97c699164abec552042bd))

* Merge remote-tracking branch &#39;origin/master&#39; ([`bf386b3`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/bf386b3c5113ddf8c26a66f5ef3857239663071a))


## v2.11.0 (2020-03-13)

### Feature

* feat: add file_reader() and file_writer() utils ([`591ae2b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/591ae2b2131bdc804c092d3d6e267caa73a64aa5))

### Refactor

* refactor: use file_reader() and file_writer() to streamline file I/O (closes momotor/engine-py3/momotor-engine-broker#40) ([`2f7a6d4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/2f7a6d4725e805759355e25e5c8b64f8c4fa574e))

### Unknown

* 2.11.0

&#39;[ci skip] Automated release&#39; ([`4410972`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/4410972c7d9e0a5f3095f9ba299523f6e79783c3))


## v2.10.0 (2020-02-28)

### Feature

* feat: deprecated ID_HASH_CODE constant, use is_identity_code() instead ([`aa6e141`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/aa6e1414b7f67fbf583b5801a4b72e5f17f4ad5c))

### Fix

* fix: do not check for existence of identity encoded content in cache (Closes #8) ([`a00be3c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/a00be3c9aee40370746c7ea9bfd5509d1262f971))

### Unknown

* 2.10.0

&#39;[ci skip] Automated release&#39; ([`bf750cf`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/bf750cfe94d9222bb4394ade8fc38aba3c92fa5a))


## v2.9.0 (2019-10-28)

### Feature

* feat: add &#39;exclusive&#39; option to SharedLockRequest (closes #7) ([`a9733cc`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/a9733cc0b8e33dcd931ad1fc699932efc90cc8b3))

### Unknown

* 2.9.0

&#39;[ci skip] Automated release&#39; ([`92d7245`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/92d724535bc6f8d4c734074e232da0e1462914ea))


## v2.8.0 (2019-10-14)

### Feature

* feat: export DEFAULT_PORT and DEFAULT_SSL_PORT ([`0469d14`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/0469d146a71665fcc66791df2486565b133e27f2))

### Unknown

* 2.8.0

&#39;[ci skip] Automated release&#39; ([`9af2956`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/9af2956d4667058279bb059a78d20c1ce0e0f58d))


## v2.7.0 (2019-10-14)

### Feature

* feat: Add SSL Support ([`5812a41`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/5812a41c2e6a051d2a69d92dc1166d853c98a221))

### Refactor

* refactor: typo in comments fixed ([`c39027e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/c39027e6c3cc2403e1491a46d07d29df9264980b))

### Unknown

* 2.7.0

&#39;[ci skip] Automated release&#39; ([`80997dc`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/80997dc6cb50687bcc16647bf65eafdafd90a406))

* doc: corrected docstring ([`fd491c4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/fd491c4da25765c682f77df77ee63b76af559781))


## v2.6.0 (2019-10-10)

### Feature

* feat: upgrade grpclib to version 0.3 ([`710c99f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/710c99f5c55330deb217ecbb1c674724fcc2ac27))

### Refactor

* refactor: use contextlib.asynccontextmanager on Python&gt;=3.7 ([`9baf0ae`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/9baf0ae4e2eb2a1c694d52df84d5428e48ab2080))

* refactor: reduce debug log spam further ([`6804e63`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/6804e639f970864a14f0f380d08c586336831e56))

* refactor: reduce debug log spam ([`d23d0d8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/d23d0d8ba1d6d6a65dd729165fa42fe28cc18263))

### Unknown

* 2.6.0

&#39;[ci skip] Automated release&#39; ([`35bcdf1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/35bcdf1bbfda318d6b57379997743af19c227a12))


## v2.5.1 (2019-09-26)

### Fix

* fix: remove ResourceUnavailableException as a worker cannot report this as an exception ([`6326a5c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/6326a5c600796e34bc6fe1cb1cf56e3b17da5b17))

### Unknown

* 2.5.1

&#39;[ci skip] Automated release&#39; ([`7205ac7`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/7205ac79d8cbb048c01606d40af025579fb4c4cf))


## v2.5.0 (2019-09-24)

### Feature

* feat: add resource unavailable RPC exception ([`682f821`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/682f82164dad336365d1642ce72c81845da2f364))

### Unknown

* 2.5.0

&#39;[ci skip] Automated release&#39; ([`fd29264`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/fd292642e53baf6e4a7f254a2c104b88f7a62697))

* Merge remote-tracking branch &#39;origin/master&#39; ([`d5b74ed`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/d5b74eda91d53bd7fa80557df4c1d60e544150c2))


## v2.4.0 (2019-09-24)

### Feature

* feat: add resource field to GetTaskResponse ([`d750178`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/d7501781c9829b2b645651e41e92eae5660f44d8))

### Unknown

* 2.4.0

&#39;[ci skip] Automated release&#39; ([`9786774`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/97867740f51d2e26725188ceb408a21ef0a07710))

* Merge remote-tracking branch &#39;origin/master&#39; ([`e462c19`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/e462c19854275e03b4d944939f51ac51495f5b9e))


## v2.3.1 (2019-09-24)

### Fix

* fix: conversion from Resources to ResourceMessages is wrong ([`ed26bee`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/ed26bee24a22f8f531879cd2e681e1061c7bd2cd))

### Refactor

* refactor: logging changes

* no uppercase initial characters ([`808a8c7`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/808a8c7fb402b4eceb434c3007361d76f1125078))

### Unknown

* 2.3.1

&#39;[ci skip] Automated release&#39; ([`f4885b4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/f4885b485a0dbd29690cf24492bcee56ebe78a5b))


## v2.3.0 (2019-09-09)

### Feature

* feat: add methods to convert resources field in rpc messages to and from Resources ([`8481420`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/84814200c3d9c5656f2e57d83d94e2228b3649bc))

### Unknown

* 2.3.0

&#39;[ci skip] Automated release&#39; ([`7d3cf84`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/7d3cf84dfee79d24c9032d87e56464dc7b4a60fd))


## v2.2.2 (2019-09-05)

### Fix

* fix: move before_script to test base ([`a479e48`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/a479e483b5e2b6b46fc36568b606199f7536418c))

### Unknown

* 2.2.2

&#39;[ci skip] Automated release&#39; ([`09b055e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/09b055ecb6c343d5740f0234dc0772f84895c495))


## v2.2.1 (2019-09-05)

### Fix

* fix: move StateABC and LockFailed classes to shared package ([`b7af7e4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/b7af7e4164d05f90b1b468e2516c019506f272ea))

### Unknown

* 2.2.1

&#39;[ci skip] Automated release&#39; ([`21247ce`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/21247ce14c224aea028c46000f06ccd495c79a63))


## v2.2.0 (2019-08-22)

### Feature

* feat: add resource fields to jobs and tasks ([`a304999`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/a30499946790e26cb9c0603ae969752e409d16b1))

### Refactor

* refactor: updated generated pb2 files for latest version of protobuf compiler ([`17edd4a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/17edd4afefd43bd46dfc190beeecef1ed2170a8d))

### Unknown

* 2.2.0

&#39;[ci skip] Automated release&#39; ([`1ec6366`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/1ec6366035ec1a073a17e24945b1226049f147d8))


## v2.1.2 (2019-06-25)

### Fix

* fix(lock): sharedLock is a streamStreamMethod, so it expects and returns sequences ([`e5e0060`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/e5e006083450d22c5d67387e63bc5437670adf85))

### Unknown

* 2.1.2

&#39;[ci skip] Automated release&#39; ([`925282b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/925282ba6ae6ea2e7638c72bdb780d039d50f532))

* Merge remote-tracking branch &#39;origin/master&#39; ([`e0b347f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/e0b347f324d5e83f7d7c8b2d1cfef63e941bdb29))


## v2.1.1 (2019-06-25)

### Fix

* fix(lock): end stream when releasing shared lock ([`2da3424`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/2da34244ddab84370302b714cd594f2c1009929f))

### Unknown

* 2.1.1

&#39;[ci skip] Automated release&#39; ([`a7de40e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/a7de40e1cec294becaab63c144c5d66732efa4dd))


## v2.1.0 (2019-06-25)

### Feature

* feat(auth): Add `momotor.rpc.auth.client.get_authenticated_channel`

This provides all the plumbing needed to connect and authenticate
a client using grpclib.

Also re-exports grpclib&#39;s exceptions for use in dependencies ([`e35df74`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/e35df7401288dd5eb36d9cd6a8175a4d9f52781b))

### Unknown

* 2.1.0

&#39;[ci skip] Automated release&#39; ([`5fd7a02`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/5fd7a02cd01fcd69af37c55e11cd4fe3cf77becc))

* Reverted grpclib version pin, since 0.2.5 is unstable due to an issue in h2

See https://github.com/vmagamedov/grpclib/issues/78 and https://github.com/python-hyper/hyper-h2/issues/1183 ([`fcbe908`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/fcbe9089dea317a27222f8c2d13238a641ab74a2))


## v2.0.0 (2019-06-21)

### Breaking

* feat(hash): Simplify hashing API

BREAKING CHANGE: hashing API changes ([`5985e3e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/5985e3edb2372e4fd7175bb06009584f19484ade))

* feat(hash): Switch to better supported py-multihash library for asset hashes

BREAKING CHANGE: hashing API changes

`momotor.rpc.asset_hash` was changed to `momotor.rpc.hash` and most methods have changed
`momotor.rpc.identity_hash` has been merged with `momotor.rpc.hash`
`momotor.rpc.const.SUPPORTED_HASH_FUNCS` is now a list of integers
`momotor.rpc.const.HASH_ENCODING` has been removed. `base58` encoding is required
`momotor.rpc.const.MAX_HASH_LEN` has been changed to 1024
`momotor.rpc.const.MAX_IDENTITY_LENGTH` has been changed to 747 ([`afa14ec`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/afa14ec23464a0fec414b8ba9c1650ba84177f36))

### Fix

* fix: get_file_multihash content encoding maximum size is one-off ([`66f6c77`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/66f6c77d579c2bd91c27cb80469bbcd6040a2135))

### Refactor

* refactor: import hash decode and encode functions as decode_hash and encode_hash ([`9a403f7`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/9a403f7fd2bb57789da9d775c24a7664188ef2e7))

### Style

* style: Add missing newline at end of file ([`c7fc40b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/c7fc40b09868fea08c0ceb0765d2f6cb7f5a3f1a))

### Unknown

* 2.0.0

&#39;[ci skip] Automated release&#39; ([`a197167`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/a1971672085d122974c9c6eb55ed082f0675102a))

* 2.0.0

&#39;[ci skip] Automated release&#39; ([`3689b65`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/3689b65046c7834e0d8a8a1df687ab6b9d72651f))

* Python3.8 tests are allowed to fail for now ([`a9bb2c4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/a9bb2c46f7c8cfdf431b099670372b5aa3558563))

* Fixed assert of hash existence ([`cb4ec4f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/cb4ec4f00e3cedd0dc6d7676366a566c36457340))

* Added test job for Python 3.8-rc ([`a8c0b80`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/a8c0b80045e2f1329550fa596bc16e428789aefd))


## v1.1.0 (2019-03-05)

### Unknown

* Added logging ([`67bb6e9`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/67bb6e9c142bfa07e9378a4b7c9e934d8ac2f068))

* Extracted implementation of the shared values so it can be used for local processing ([`b65e5e5`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/b65e5e5fd9c095174e08c5a30cc43f1ee0cb51b1))

* Added remote implementation for shared items ([`506fb2f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/506fb2fd745b894b83d0caa5cf3085232962b7c6))

* Only adding sharedLock interface for now ([`4841125`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/4841125aab21c6e4e867deb62cf74f501e578af4))

* Added sharedValue and sharedLock endpoints ([`f7fde99`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/f7fde99998f18f1462bfca6bbc48822bf3bedb09))

* Bumped version number ([`ed24f65`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/ed24f6590fc0d639ded695dfd94ecee0a73f0e3e))

* Fixed matching supported hash functions ([`184f291`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/184f291ff89023a0f63a2b5ec80881a36f1a9c34))

* * Use files instead of buffers to send and receive bundles
* Added a `process_executor` argument to `send_asset` and `receive_asset` to execute hashing in a separate process
* Replaced `get_size_and_hash` with `get_file_multihash`
* Removed `content_chunks_generator` ([`6a34e77`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/6a34e777e72ecf6ff15b8e1bc161b3efa3638670))

* Added helper to calculate file hash ([`213bdc8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/213bdc8169e38c096a31c8fb9211a43cdd775533))

* Changed hash util functions to non-async, so they can be used in executors ([`92049dd`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/92049dddcd9c55eed1150d46b807199da1cef3e9))

* No default timeout for send/receive asset methods, no retries on TimeoutError
Convert grpclib&#39;s &#39;Incomplete data&#39; exception into an UnexpectedEndOfStream exception
Set chunk size to 256kB ([`584eb01`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/584eb01a1c2491b4a83cf9ff5b8a5924b41d0faa))

* Limit chunk size ([`c0406c8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/c0406c822df27dd83c5011f7a2fcd8a0f4085d30))

* Get version without doing an import in setup.py ([`51770e2`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/51770e2f64a96ff21219882c9302a5e17648727b))

* Updated version for initial public release ([`07d64a5`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/07d64a5dd39fd2d177d4a178c49f7c07234d4492))

* Version pin grpclib to 0.2.2rc2 ([`dd8ae6d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/dd8ae6dc7431093e5c0ca6a962db402bb1d9be48))

* Better logging ([`b3408a9`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/b3408a93c1c3f2ff0e0f9ab270ea9a4fdb8ac079))

* Correctly set end=True on last message sent on a stream ([`27a8f2c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/27a8f2c4f8cd133f19b25a5ffce1f0033524f3d0))

* Always end stream when uploading or downloading ([`ab0c9f9`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/ab0c9f9a06d086752a60c4b63b64e4301ff9a8da))

* uploadAsset is stream-stream ([`ba40dff`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/ba40dff4ec990cbdeec07cb553d4d774e2bedad2))

* Handle messages without exception field ([`d8cf053`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/d8cf05398723be3c3bd430459ab11a2b10f8fc66))

* Added additional message to downloadAsset requests to indicate acceptance of the stream ([`ea4a4c3`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/ea4a4c34b278d126682606931a8a58ef409814d5))

* Format protobuf messages ([`4f2ec31`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/4f2ec31a72e277d2bde11fcd70fef2bbdf91cd9e))

* Raise &#39;UnexepectedEndOfStream&#39; where appropriate ([`1d6013e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/1d6013ea95b283d46772ddf583ec93043db71d7f))

* Handle GeneratorExit in generators ([`c906882`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/c906882474fbae2f337a01ae5e0b3f63d4604284))

* Set maximum backoff time ([`30ebc76`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/30ebc7605f79501f5bb26333cc91ac42294a50b5))

* Removed use of asyncio.gather ([`bc00c55`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/bc00c55d66f28e002479136864450429f8e7b011))

* Added send/receive timeouts and logging ([`609e830`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/609e830799b6b30902e5057c6cbd62dc6936006a))

* Merge remote-tracking branch &#39;origin/master&#39;

# Conflicts:
#	setup.py ([`8b60df4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/8b60df419bd3c44977dd1e40c0854fa87dc98f94))

* Use find_namespace_packages() ([`507958f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/507958f01d7fd20020de5c5a9af34598d5cac8de))

* Use find_packages() ([`d24f8df`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/d24f8dfb1cb0da3e27f8d231b61d0c39efe9d226))

* Fixed setup.py ([`3d2094a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/3d2094a7fb8957ee4d2ad94a0303a2e989f5a3d5))

* Made pysha3 a required dependency ([`1c7391b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/1c7391b90999f69bc5ae6c445a1dd50cad04a58a))

* Removed debug print statements ([`41dd162`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/41dd16286d461f8d94ff091a350416e49ea78f73))

* Added --threads option ([`fa8591c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/fa8591cc0125c469fde4dc2e6a2c7ea44d64c38c))

* Make sure .aclose() is always called on the async generators ([`8ff94dd`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/8ff94ddcfd9693729025ee9edfa0da4dffe9f4dd))

* Support memoryview for hash functions ([`9137171`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/9137171385df0777cd269e62fd2b020a31ae3bbe))

* Renamed JobStatusResponse &#39;jobStatus&#39; field to &#39;status&#39; ([`0b7b72c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/0b7b72c64c4c7ce2dfcf1e7d87858b0a2913d109))

* PEP8 fixes ([`0af33c1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/0af33c1abb54cabf5a201183a79126155360b6a2))

* Fixed setup.py ([`c809b96`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/c809b96290f7f17f04adddf99aca909634346fd0))

* * Fixed and assert job/session key type consistency
* Implemented multiJobStatusStream endpoint ([`c4b7e74`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/c4b7e74c082108d2e802fb4bf0fddee2fdda0ce2))

* Provide &#39;progressUpdateInterval&#39; value in serverInfo ([`29e5d5f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/29e5d5fd29ef4f50fa7f0d6fcd434f6dab6168d7))

* Added TaskId message type ([`a710ceb`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/a710ceb56107acdee7740abfd4549ce786e116bb))

* Made `exists` callback for `receive_asset` async ([`4cc02fe`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/4cc02fed80db4791a85a790bbfc6bd29812f8e95))

* Renamed AssetType to AssetFormat ([`855d363`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/855d363f3f7c1086e74ed2bc3850605351948096))

* Export AssetNotFoundException ([`efb7f6c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/efb7f6c49d49e73633d85ab3cc016a4c49d25d2b))

* Added additional argument to receive_asset to cancel downloading a known (cached) asset ([`ef1a5a4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/ef1a5a4fe7e7978f665b42109665ec9dd0c8c3ea))

* Added &#39;decode_identity_hash&#39; ([`be05909`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/be059095ea3c0c4d78f2f42b3a5c9e24f89e4554))

* Added ASSET_NOT_FOUND exception message ([`5977158`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/5977158cfc5509751eb38e5f532c6702ca73db6a))

* Document that remote.py and server.py are each other&#39;s counterpart ([`0ba9c85`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/0ba9c85b36f03637cc954fa82914be7b916555a9))

* Renamed momotor.rpc.asset.client to momotor.rpc.asset.remote (remote indicates this code is for both clients and workers) ([`060c919`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/060c919cec3088a2aadbc2442e0b43b39f25d57a))

* Test empty chunks generator ([`b8b8f81`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/b8b8f81a71ce156fe78577560de3df1051d84172))

* Make pytest xfail strict by default ([`96219a7`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/96219a7ad0b7ae5b2cb31c8de875c1dc12149655))

* Use a check that also passes for SpooledTemporaryFile ([`45ff244`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/45ff24498f919681f637e31822592e59185ffc9d))

* Generate combined results bundle ([`def2b63`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/def2b639017fc478e454b4c428ef9c45621016d3))

* Validate asset hash on download, handle size==0 as special case that doesn&#39;t need a hash ([`cdd4def`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/cdd4def6c72ae56656134989caabc60f5b75f11e))

* Move core of server upload/download code to protocol package ([`755afd1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/755afd1f62a52d5601f4a0f3963ae083cecd2ddb))

* Changed JobStatus message ([`21ebe47`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/21ebe472af0bc16b1d1ea2ceafe42a3e87e85cd0))

* Removed TASK_RESULT asset
Check upload/download asset query parameters according to spec ([`80774ef`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/80774ef8d60a342b8dec2fb51fc83f157b6a3a94))

* Added AssetQuery type
Removed AssetPool.get_all
Rewrote Controller.start_job ([`9cff434`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/9cff4348171af1cf44fc90828ff13a8d40012b18))

* Better asset file handling ([`b9f2c2e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/b9f2c2eeb697ff12859cbf5cafdc6370fffbfb36))

* Lot&#39;s of changes to get end-to-end test working ([`4afaa3d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/4afaa3dad197ec9d21e9a88cf493d1dde3014839))

* Started with an end-to-end unit test case that test the run of a complete processing job ([`7d549d1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/7d549d15fa68f4d3b159e073bea4254e9cea1b2c))

* WIP: Started with adding worker tasks ([`bc63674`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/bc63674d3b85cbcc1221294fe5bf7143cc73be92))

* * Rewrote Authenticator class to SessionPool
* No global pools, but initialize them at start and connect them to the RPC classes ([`72187b4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/72187b44ecdfab892a3d85815fe3db4a8ff30739))

* * Changes to get RPC client working again
* Changed DownloadAssetResponse to allow first response to include a chunk
* Include server hash support info in ServerInfoResponse ([`acc4b25`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/acc4b25f35824df70b0f34cdfb1dd53e2fc96288))

* Updated preferred hash functions
Allow tests for unsupported hash functions to fail ([`25bda3f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/25bda3f0f105093242d9bba147d168b1d29309ee))

* Refactoring/cleanup ([`2d5fc25`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/2d5fc25791b629b73b6d36f0affd7c89c31d601a))

* Test encode/decode cycle ([`81d53f2`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/81d53f2d0995f5ec08422956a517346be169bfa6))

* Document real maximum length ([`4087de1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/4087de1247ce85aa2ddcfec132d421e941bb9f1b))

* Mark test directories as such ([`2a18417`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/2a1841797df03eedd944db4a110d88f8ae6fbf46))

* Added pytest dependencies ([`4b061a4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/4b061a4ae7d21ea33d2d27eafdadcb3584f0b035))

* Added .gitlab-ci.yml ([`3ddd700`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/3ddd7007e3af11d1595b4a6c66264db03ac2a43b))

* pymultihash does not support varints, so code and length should be limited to 127
(See https://github.com/ivilata/pymultihash/issues/7) ([`b31c283`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/b31c283bf79bc5c68f4493d387ec5af47c3e0bf8))

* Added support for an identity hash, ie. content encoded inside the hash value ([`938f40a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/938f40a1b33819edbda29f61523238f03a4f542d))

* Moved asset decoding tests to momotor-engine-proto module ([`c98b86e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/c98b86e1984cf8fe110d3f66b83ca119f584f323))

* Raise AssetException on invalid hashes ([`21cc185`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/21cc185b84f2ea2b94c5e37425948e6a4a4ac7d2))

* Simplified upload protocol: only one RPC stream for upload is needed
Removes the need for a UUID field in the Asset model ([`2365310`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/23653105a62e4f69aa7537245c3e8b40f03aea76))

* Added missing RECIPE category ([`092ed36`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/092ed36ab16bf169fe9a0af4cc5d46e25113ea85))

* Changed Asset.hash field into a BinaryField
Require job_asset.asset field to be cached when creating AssetHandler instance ([`f5759fa`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/f5759fa060114e084940eda595cae6d70bb566bc))

* Move almost all uses of the multihash library to momotor.rpc.asset_hash
Only one test function left that needs deep access to multihash ([`2d35f13`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/2d35f137e26e9d532fb73756eb420c234ad69bde))

* Corrected and extended hash value documentation ([`0f59fee`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/0f59fee76e8e673a235f3f80c8d9fe5a7f062753))

* Added HASH_FUNC constant
Version pinned pymultihash and base58 packages, because they have incompatible latest versions ([`421e08f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/421e08f8e3bc3fe30ade254f982c9f9813d264fb))

* Created constant for hash encoding ([`975eab9`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/975eab9bd015b718dcfe7556a1ac0f91fc0288cf))

* Added AssetHandler.validate ([`3c402e9`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/3c402e963314b6232c8aa92d45626fb3f18413eb))

* Added models, pools and handlers for Jobs and Assets
Added asset file creation from an async stream of chunks helper

WIP: no migrations, yet ([`a354082`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/a354082a01f167367a9fc7943ff1378d5ed65fab))

* Set Python 3.6 minimum ([`63023d3`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/63023d32acd383b834794844119e539cc2c7de6b))

* Renamed &#39;WorkSession&#39; to &#39;Job&#39;
Renamed &#39;AuthSession&#39; to &#39;Session&#39; (Django model is called RPCSession, to prevent confusion with Django&#39;s builtin sessions)
Added Django migration ([`ea9f496`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/ea9f4963fbfad424b77dd66c2e0969153d78c4c3))

* Changed the `forward_rpc_exception` decorator into a `process_response` decorator that not only converts and emits an exception response, but also converts responses from the wrapped method into the correct type and emits it on the stream

Added the `process_request` and `empty_request` decorators consume the first message on the stream, validate it and provide it to the wrapped method as an additional argument. ([`18e9dcb`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/18e9dcbc948d773092a2dce5f476f4a2b6019b1c))

* * Created models for auth/work sessions.
* Use auth/work sessions in RPC calls. ([`3b5165a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/3b5165a5988e10ed964ed94f11bb975b3e920c82))

* Moved authentication to a separate service ([`a930b60`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/a930b6022bd5f4f448db339677738fdea12610b3))

* Initial commit ([`b2f97c2`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-proto/-/commit/b2f97c2ccb5f3e8af0eba5920279cc03947a723d))
