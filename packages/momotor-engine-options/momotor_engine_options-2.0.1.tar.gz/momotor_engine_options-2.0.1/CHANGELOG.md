# CHANGELOG



## v2.0.1 (2024-04-16)

### Fix

* fix: update dependencies ([`1b4261a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/1b4261a04486ff6174ae9cd1b7f3109b4f2684ed))


## v2.0.0 (2024-04-15)


## v2.0.0-rc.11 (2024-03-19)

### Breaking

* feat: convert to PEP420 namespace packages

requires all other momotor.* packages to be PEP420 too

BREAKING CHANGE: convert to PEP420 namespace packages ([`1b01285`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/1b01285620e39f7882e5a68590afdc5e2ee2e1b5))

### Refactor

* refactor: replace all deprecated uses from typing (PEP-0585) ([`00021e8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/00021e8ea1111d2112e611bd93975082678997d1))


## v2.0.0-rc.10 (2024-03-04)

### Feature

* feat: extend `document_option_definition` to document step options ([`83bbd22`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/83bbd22735b19f60c6ee7d2165dd0bc1e3f86876))

### Refactor

* refactor: update type hints for Python 3.9 ([`9705bb8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/9705bb832c19673b6fd8f0016ca0fc342bced1cf))

### Unknown

* doc: make production lists consistent ([`cdb8721`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/cdb87219a0ad6f965bd2f9e4690f5068d54d7c56))

* doc: correct reference syntax documentation ([`e26f1d7`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/e26f1d745bceae8ddf411c14d269008b4ad3bd3e))

* doc: correct reference syntax documentation ([`f4f4fe8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/f4f4fe84a09a035ed8cdbf45ed08ecc27b3bbded))

* doc: documentation update/clarifications ([`c61e8fc`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/c61e8fc30cdc40c5821cd152e009ab8285b521d0))

* doc: several documentation fixes/clarifications ([`048016d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/048016d44a3721b58cd9bf5114acdee64ee72beb))


## v2.0.0-rc.9 (2024-01-16)

### Breaking

* feat: add Sphinx extension to handle external references to local package

BREAKING CHANGE: moved `momotor.options.sphinx_ext` to `momotor.options.sphinx.option` ([`297382e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/297382e142841a1211c2452261e12fdbcd1e22c2))

* feat: remove deprecated interface of get_scheduler_tools_option()

BREAKING CHANGE: deprecated interface of get_scheduler_tools_option() removed ([`130078d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/130078d9c1d6d97397918565f71e3a7bbb1b41df))

### Fix

* fix: docutils is an optional dependency ([`1942882`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/1942882b2762b9cb14c78ff28e29e94c0b37093e))

* fix: allow comparing of OptionNameDomain with other types ([`9cb473b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/9cb473b9841614fe4a64f3dca9ac8629e706cadc))


## v2.0.0-rc.8 (2024-01-12)

### Feature

* feat: add `annotate_docstring` ([`3033245`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/3033245069fe1ef9b56ffe67d14bfa62fdb2a52d))

* feat: make it possible to xref a local option in the same checklet ([`a3ee72e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/a3ee72e60c639713a07ac3560f56e5e9d95e50d8))

### Fix

* fix: always include domain in option name ids ([`71fdf62`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/71fdf62552c86f6886875514856f2e6c3aaf2b4d))

* fix: correct toc entries ([`0ef4f2f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/0ef4f2fa049d4e60f5f46a4ad6281988cff41bf2))

* fix: change rendering of option attributes ([`a301d2d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/a301d2d44ba9fd7004b6a24630c41ea7241a1a98))

### Refactor

* refactor: remove __all__ from __init__ ([`d55e4e4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/d55e4e49c6b46d35e5540e7fca6ccf839705fb6c))

### Unknown

* doc: update docs ([`cdc7a36`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/cdc7a361d86e9d96b4a12842363175f6fcda5bb3))

* doc: update conf.py ([`6e2a503`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/6e2a503ea5b50dbbf1fabd7439ca278784cbec1a))


## v2.0.0-rc.7 (2024-01-09)


## v2.0.0-rc.6 (2024-01-09)

### Feature

* feat: extract and document task id placeholder replacement into a separate function that can be used by checklet base ([`ad6a189`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/ad6a189f2b4b5dbbd472c11d5b010828d52d229c))

* feat: add &#39;canonical&#39; option location link ([`f35bbf4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/f35bbf4a0e8e9fc5d171e0044448ce0dae0773cf))

### Fix

* fix: correct xref anchors ([`e22d78c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/e22d78cb5cccc2d876680b1e2ea9418272f3c5a6))

* fix: iterate over all references ([`156cf7d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/156cf7d571c0f87741bd644b2a8d06164d53193d))

### Unknown

* doc: small doc update ([`36a526d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/36a526da74d136d5054964c754ab7686e559c3a1))

* doc: use full path to reference Checklet options ([`5b1d1f1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/5b1d1f1ecc705949ce1927031fe9840131567540))

* doc: update intersphinx links for momotor.org docs ([`590d9e8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/590d9e87cba36e75c13272b1cf2a625ce6e89204))


## v1.2.0 (2023-10-26)

### Chore

* chore: show exact reference used in exception message ([`177fed1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/177fed1379073bab8738a9b3785d1d0be7966ef0))

### Feature

* feat: change `get_scheduler_tools_option` to include results bundle in option resolution, so references to step results can be used ([`39e2183`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/39e218353d7eea2297b992e273bdc4550b3ba14b))


## v1.1.1 (2023-08-29)

### Fix

* fix: regression: preflight option selector placeholders are not expanded ([`bdfa8c0`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/bdfa8c09ef7544342e4aaa451ce2bed7a834a207))

### Unknown

* 1.1.1

&#39;chore: bump version number&#39; ([`d37b901`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/d37b9011fe384c6dd84b7848e12477504b662f1e))

* Merge remote-tracking branch &#39;origin/master&#39; ([`5e9d94f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/5e9d94f6740b22274b0abac32ef031407cd38309))


## v1.1.0 (2023-08-29)

### Feature

* feat: add json style preflight status ([`a346c6d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/a346c6d09905b92f61cbaaae39795e1d2aaddd43))

### Fix

* fix: emulate LabelOptionMixin&#39;s handling of the label option when preflight causes step to not execute ([`6383900`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/63839005e2e5ea4d401330fbc25c4e3e28ff94e9))

### Test

* test: update to latest Pytest ([`2b2bb42`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/2b2bb425e0af16a6151d816933bcb678e010f1a7))

### Unknown

* 1.1.0

&#39;chore: bump version number&#39; ([`7608914`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/7608914796a3de95da1b924724424e0ac14a4f84))


## v1.0.0 (2023-07-06)

### Breaking

* chore: update supported Python versions

BREAKING CHANGE: Dropped Python 3.7 support ([`e1a3d05`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/e1a3d05abcfbaaec61b24ad21e94e599e1e869c3))

### Feature

* feat: support sub versions (dashed suffixes) in tool versions, to support Anaconda 2023.03-1 ([`aee2c3f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/aee2c3f1d266b78deb2c2a8bb20c756cb382d361))

### Unknown

* 1.0.0

&#39;chore: bump version number&#39; ([`ac3dbca`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/ac3dbcacbcccf1277f6df7701ff7a8121151f3d3))

* doc: fix typo ([`dc46cea`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/dc46cea160e2b667bbfd991a709e5c9b3bda0e77))


## v0.10.1 (2023-06-19)

### Fix

* fix: some error messages were incomplete/cryptic ([`3b37a8c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/3b37a8c1a2998e68b0661ff3999d4ab41a063571))

### Unknown

* 0.10.1

&#39;chore: bump version number&#39; ([`20fe626`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/20fe6260d57f06d0ddecaae8eb36daa893b6258d))

* doc: fix layout issues in doctests ([`51ab28c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/51ab28c36ce504f074de295d785d11087699acb9))


## v0.10.0 (2022-11-15)

### Feature

* feat: add &#39;pass-hidden&#39; and &#39;fail-hidden&#39; preflight actions ([`c749a05`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/c749a0560083ee6395ccdb829714626ff1f67796))

### Unknown

* 0.10.0

&#39;chore: bump version number&#39; ([`328d6ed`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/328d6edde51b6899a30837f8686d8d97193de077))


## v0.9.1 (2022-10-27)

### Fix

* fix: strip leading and trailing whitespace from selectors and references ([`929d233`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/929d23349700132234848921ed19de1f16628374))

### Test

* test: update doctest ([`271174c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/271174c31817d30434bc6a1e83e01efa45f99e27))

### Unknown

* 0.9.1

&#39;chore: bump version number&#39; ([`13648de`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/13648de60b78547ca878116fb4c78ba9fb03aa74))


## v0.9.0 (2022-10-21)

### Chore

* chore: clearer error message ([`3b81567`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/3b81567c15e1c95bda3811a0dc5d617aa6f3e8b8))

* chore: clean up tests ([`07b254c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/07b254ce97e10f0f86ac91c4bf2a4e772d670bde))

### Feature

* feat: restore `!` selector operator ([`d4581ba`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/d4581ba2bbb5356e12c639597396eafe76d0acf4))

### Unknown

* 0.9.0

&#39;chore: bump version number&#39; ([`b4cbb39`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/b4cbb39b665e0abf95070d4a19a87c8cfcdd6225))


## v0.8.0 (2022-10-06)

### Chore

* chore: update version pins ([`508c7d9`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/508c7d994d3ce7e7b366f8a2bc635e4fa0e5679d))

### Feature

* feat: add optional dimensions to `tasks@scheduler` option ([`9a4c768`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/9a4c7684392c10b9dfbc43d4525335ca3d2e1b60))

### Unknown

* 0.8.0

&#39;chore: bump version number&#39; ([`d66893b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/d66893bb59c84ce41feff487c223cfacc58594a9))

* doc: fix typo ([`a7b237d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/a7b237d9bd94891eeadcd2e858396e579d3a5220))


## v0.7.0 (2022-07-19)

### Feature

* feat: add key-value list parser ([`825d5ac`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/825d5ac277b3d687a4a2b0d1190a6dfdc047b307))

### Unknown

* 0.7.0

&#39;chore: bump version number&#39; ([`1bd7a5c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/1bd7a5c46054cba897e32170d24049a5d3968812))


## v0.6.0 (2022-07-07)

### Feature

* feat: add `sumf` and `sumr` modifiers ([`533f0cb`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/533f0cb7033cc2ff5d4e005852bd75b259ae7923))

* feat: add `empty_values` argument to `convert_intlist` ([`6be2ea1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/6be2ea14c10d60fb2967424fe691df28eb95ed5f))

* feat: add convert.convert_intlist ([`9a071c8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/9a071c8816ea8e913baac322ab409bafe8fb7bd8))

* feat: update ToolName.factory to accept a deconstructed tool base name and versions list ([`7d1b8e2`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/7d1b8e283d9c99bd3ab5effc03f9d0692fbb7267))

### Fix

* fix: handle tool options provided as child content ([`1a99ffb`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/1a99ffbbcbafdaba7e2451dec8e5bf46ee893e6a))

* fix: relax task reference parsing even more. the initial dot is now not required anymore. the $ and internal operators can be escaped to ignore them ([`f353e7d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/f353e7d6d52f772f76c326611bdbdb5513b8113b))

* fix: relax task reference parsing, allowing trailing text immediately after the references without a dot as seperator ([`829b40c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/829b40cee42ad376d4d000d3a3f0f780953eac94))

* fix: expand task-id placeholders in references ([`545a619`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/545a619b495e7ab0f9c12d9ee4b9ab41b77d1c76))

* fix: support placeholders in tool options ([`796f3ce`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/796f3ce75ebc404e08f86234154270215357c3fb))

### Unknown

* 0.6.0

&#39;chore: bump version number&#39; ([`aecb98d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/aecb98daa08021acd3f9e6f6e6b4357d8ce84c85))

* doc: update documentation and doctest for convert.convert_duration to include that seconds can contain decimals ([`71a1202`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/71a12029b48a486483ddd05e0384f26e0182bea2))

* doc: update documentation of convert.convert_size() ([`2af0a09`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/2af0a0939dca4389ffca56340cff3468fdeed284))


## v0.5.0 (2022-04-08)

### Feature

* feat: add duration and size conversion methods ([`424815f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/424815fcc9c57d2e62dbd79e017e5e039a660a62))

### Fix

* fix: correct option type usage and handling ([`2a0a537`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/2a0a537a2d2dfdab43fa3ab49c6c355c41170311))

* fix: use option types as defined by the momotor-bundles package ([`e53b4c3`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/e53b4c3fddc5dd03ea18d8d99a87c19d3012c50f))

### Unknown

* 0.5.0

&#39;chore: bump version number&#39; ([`69eaaed`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/69eaaed595ff3324d51918e468e782697bf1921e))

* doc: document filter_files.py ([`abd3253`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/abd32531105f5effe0267b9b7c4f80e25b5351da))

* doc: fix several Sphinx errors and warnings ([`2c63f18`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/2c63f1840aac4d83b8f3ced7772a03b00a96e891))

* doc: add utility functions to docs ([`ec8c8b3`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/ec8c8b3f6a6cdc84cd071be4481497773ceb9928))


## v0.4.0 (2022-04-04)

### Feature

* feat: add OptionDefinition.deprecated

(redo from commit 5cbfdf4834ad5bafc9c91972371f5978ee2c0a13 to fix commit message) ([`9a98031`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/9a98031723833fc5717027b56d890f47f3bd0e76))

### Unknown

* 0.4.0

&#39;chore: bump version number&#39; ([`a6d53f4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/a6d53f4fc8e48ca9ac8a2dac8f296afa48fc68df))

* Revert &#34;add OptionDefinition.deprecated&#34;

This reverts commit 5cbfdf4834ad5bafc9c91972371f5978ee2c0a13. ([`279d15c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/279d15cb7e294d3febeedee4fde2fb60fe2e4703))

* add OptionDefinition.deprecated ([`5cbfdf4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/5cbfdf4834ad5bafc9c91972371f5978ee2c0a13))


## v0.3.0 (2022-03-14)

### Fix

* fix: add more unit tests for cases with defaults ([`fd425a2`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/fd425a211f4d34bbc10b9a1d84204d5f4563ca26))

### Unknown

* 0.3.0

&#39;chore: bump version number&#39; ([`3439b8a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/3439b8a8eb29b2d4976b2374873aec6f22e45347))


## v0.2.3 (2022-01-24)

### Unknown

* 0.2.3

&#39;chore: bump version number&#39; ([`be35ea1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-engine-options/-/commit/be35ea1b1c0ff327d209d74360ef7e0df0126c84))
