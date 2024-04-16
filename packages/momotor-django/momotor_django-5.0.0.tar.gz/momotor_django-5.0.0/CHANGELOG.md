# CHANGELOG



## v5.0.0 (2024-04-16)


## v5.0.0-rc.3 (2024-04-04)

### Breaking

* feat: mark Django 5.0 as supported version and remove support for versions older than 4.2

BREAKING CHANGE: Dropped support for Django &lt; 4.2 ([`23af47a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/23af47ab39559c78a4bbd97bc765d00fa0589273))


## v5.0.0-rc.2 (2024-03-21)

### Breaking

* feat: convert to PEP420 namespace packages

requires all other momotor.* packages to be PEP420 too

BREAKING CHANGE: convert to PEP420 namespace packages ([`78378e7`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/78378e7fe7289c5a42cf61c603bcea09c2273226))

### Chore

* chore: update dependencies ([`db0d5ed`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/db0d5edd30968d7d0def9d97d7198b860f85ab50))

### Fix

* fix: get local protocol library version using importlib.metadata ([`d0b8981`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/d0b89812b9cc501b65a61eeabbbce0b473923b16))

### Refactor

* refactor: replace all deprecated uses from typing (PEP-0585) ([`2ab5026`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/2ab50260fc3fb4b4841edbd9448d998e5249748c))

### Unknown

* doc: update dependencies ([`7dc661d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/7dc661dde36bbcb531699dbdd6583061b7825c15))


## v5.0.0-rc.1 (2024-02-05)

### Breaking

* feat: drop Python 3.8 support, test with Python 3.12

BREAKING CHANGE: Requires Python 3.9+ ([`fc3763f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/fc3763f339af6edace5d91fbb0f3a2421e64069e))

### Chore

* chore: update project ([`b16d268`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/b16d2686cdfdd4cd59f4b9f83cd21747bb322913))

* chore: update setup.py ([`7fb8246`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/7fb8246d41fbe038cc45c02bbc0715d985a5ace7))

### Refactor

* refactor: update type hints for Python 3.9 ([`c5102e5`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/c5102e5b8c46d93449fbdd1fa571a5b1d3a50752))

### Unknown

* doc: update documentation theme and other documentation updates ([`066dd45`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/066dd45a382f78da0a8656edae762dcbd801f8dd))

* doc: update intersphinx links for momotor.org docs ([`cdde301`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/cdde301489b85825fcffe6394e3dd07ec8066092))


## v4.1.0 (2023-06-09)

### Feature

* feat: update Django version pin (closes #8) ([`326a37e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/326a37e2bef639c72166c273039a4766397c9200))

### Unknown

* 4.1.0

&#39;chore: bump version number&#39; ([`fd517a2`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/fd517a2711a0b66ef0966664fac46d09fea98691))


## v4.0.0 (2022-12-09)

### Breaking

* feat: drop deprecated features

BREAKING CHANGE: drop deprecated features ([`b029869`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/b02986919a701444cb34d12328e6fee2984cb1d6))

* feat: update versions pins

* Add Django 4.0, 4.1
* Drop Django &lt;3.2
* Drop Python 3.7

BREAKING CHANGE: Requires Django &gt;=3.2, Python&gt;=3.8 ([`ee022f0`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/ee022f0de6e836d447d97459877f423ca1c51df4))

### Chore

* chore: remove inactive debugging print statements ([`556c53c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/556c53c6714e92e5e57aa8ce6771d9b71349b3cd))

* chore: clean up project file ([`b7d8403`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/b7d8403c8e424f6e692a25e33e9cc7412e0b9972))

* chore: sync requirements.txt with setup.py ([`e595fe3`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/e595fe3d249c47386fe7eb1f0b3ef9f8618231cb))

* chore: default_app_config is removed ([`61d6783`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/61d6783dd39f1b3e8f3994e0521c00bf200f824f))

* chore: link to documentation with the correct version number ([`a7d3c12`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/a7d3c124f4004e5479f5f38e7e29cca12a755f68))

### Fix

* fix: replace use of `asyncio.get_event_loop` ([`2df42b9`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/2df42b97f3115968eb3ae7ebf7fd2acba09f6aa8))

### Refactor

* refactor: specify return type of `BrokerConnection.multi_job_status_stream` ([`0be85e8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/0be85e8da1d5b1cd3e784ae1dca6ad1a91000920))

### Unknown

* 4.0.0

&#39;chore: bump version number&#39; ([`4faffdc`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/4faffdcd20d8d479955b41970ab75c4f207ba6f1))


## v3.2.1 (2021-10-01)

### Chore

* chore: update project files ([`8ea8cbc`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/8ea8cbccaa32cfd85696cdc7bad0bee02377708f))

* chore: update project files ([`c191715`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/c1917155588bfa54fb95e0420218738dfd280a02))

* chore: update project files ([`a5a33e3`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/a5a33e3e783362242abf7f6ed8462b1c614279ee))

### Fix

* fix: mark momotor.django.log as deprecated ([`dfa36b0`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/dfa36b09bf3937233d5bb3a97242f6375a420a52))

### Unknown

* 3.2.1

&#39;chore: bump version number&#39; ([`c5e4419`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/c5e441905096c38114f94f879aaf77d6af00a096))


## v3.2.0 (2021-05-20)

### Chore

* chore: add &#34;Framework :: Django&#34; classifiers [skip-ci] ([`02e4d2b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/02e4d2b6be1d44d714801f4d55bdd831dde3e00d))

* chore: update/move PyCharm module files ([`2993c6d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/2993c6db1a1e197f601fdc20f19216f1dbcf21a3))

### Feature

* feat: support Django 3.2 ([`3e49813`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/3e49813de1dd0a1f60bd161e8b20ddf33132981e))

### Unknown

* 3.2.0

&#39;chore: bump version number&#39; ([`df38c73`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/df38c7352109866b4e83223246a553a6c8519ad6))

* doc: correct commit url in CHANGELOG.md ([`51bc401`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/51bc401e8a820b77c2d54af520e5f3435358e8de))


## v3.1.1 (2020-10-23)

### Fix

* fix: the loop parameter is deprecated ([`fa88665`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/fa8866535bb415a74f46c9c8a5d4ca556bb06b6d))

### Unknown

* 3.1.1

&#39;chore: bump version number&#39; ([`ed09f43`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/ed09f43983723f14b0d8c0101302d6ec42a3e7fa))


## v3.1.0 (2020-10-23)

### Chore

* chore: update Python SDK ([`8df6964`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/8df696425f58dd717bb3c19599989924d743cd13))

* chore: update Python version classifiers ([`346b098`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/346b0982976e07c16d89fb4cb61f87008519208a))

### Feature

* feat: bump supported Django versions ([`0ca5a8f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/0ca5a8f330473a4351dab8349f5387f0eb77add6))

### Unknown

* 3.1.0

&#39;chore: bump version number&#39; ([`4977c13`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/4977c1380ef4d12ae252d0fdab77f6602e8b5d7c))


## v3.0.0 (2020-08-17)

### Breaking

* feat: changed minimum Python requirement to 3.7

BREAKING CHANGE: Requires Python 3.7 or higher ([`33d150e`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/33d150eef73e8047b83a96dadf842c1498a3d4aa))

### Unknown

* 3.0.0

&#39;chore: bump version number&#39; ([`84100bf`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/84100bf68098630567aed0f8aa98af30246b9074))


## v2.0.0 (2020-08-07)

### Breaking

* fix: remove imports from `__init__.py` to prevent an &#34;import storm&#34; at load time

BREAKING CHANGE: Moves `BrokerConnection` and `retry_connection` to `momotor.django.connection`. Update import statements ([`329e64f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/329e64f8d2cbd469a532f9be82f2992967fb5687))

### Unknown

* 2.0.0

&#39;chore: bump version number&#39; ([`f5f62b8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/f5f62b822dd98f214d550b115f869c8c48f61298))

* Merge remote-tracking branch &#39;origin/master&#39; ([`118e5d6`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/118e5d6fe1f5ca274ae0a964de5edba70ae73280))


## v1.4.2 (2020-06-30)

### Chore

* chore: update project ([`8ba1c40`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/8ba1c407fce80225ebf93be130f60e3c5882c09a))

### Fix

* fix: Python 3.6 compatibility ([`4ccc57c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/4ccc57c168f117501aac389d7393b9738b672223))

### Unknown

* 1.4.2

&#39;chore: bump version number&#39; ([`a4dbdff`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/a4dbdffd5dfa677b33d81f347994cbd1cb994c37))


## v1.4.1 (2020-06-08)

### Fix

* fix: add asgiref requirement to setup.py ([`15b17d6`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/15b17d68e357ab36d1d5307ac307645dbb86e42a))

### Unknown

* 1.4.1

&#39;chore: bump version number&#39; ([`fd14da7`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/fd14da766347fa779835002bc5360e569de12291))


## v1.4.0 (2020-06-08)

### Feature

* feat: add logging utils ([`d81a9a9`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/d81a9a995430aae49c11ddba887a0f1ff8c6b2cd))

### Fix

* fix: typing of log_exception ([`67cc988`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/67cc988b5547d76e58736c7c7a6920a47a043b62))

* fix: use async logging where possible ([`5860355`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/58603552d010946318bddd8ed86d7f10912209ba))

### Unknown

* 1.4.0

&#39;chore: bump version number&#39; ([`7fb2b66`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/7fb2b6696f051943b6a1ca6d48c882d5519056e0))

* doc: fix package name in index.rst ([`c42c31c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/c42c31c3e8ef1c1248094db938b41afb820dd162))


## v1.3.2 (2020-06-05)

### Fix

* fix: correct Django version pin in setup.py ([`5fdd3c4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/5fdd3c4847e9ad405ec8061c2164c9ffac0c6d90))

### Unknown

* 1.3.2

&#39;chore: bump version number&#39; ([`4eda833`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/4eda833a15ee3701d1bd13a32c775bf1231c6801))


## v1.3.1 (2020-06-04)

### Fix

* fix: Update Django version pin ([`67522c8`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/67522c8b836a7f8568d1ec88065f95de02481322))

### Refactor

* refactor: correct imports for StreamTerminatedError and GRPCError ([`127c7ba`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/127c7bafff4d65354052140c56b3f186d39f7d0b))

### Unknown

* 1.3.1

&#39;chore: bump version number&#39; ([`b329587`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/b329587969bf7bf2172a8f66526a304c799a79c6))

* project: update dependencies ([`07dd2a1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/07dd2a13d8c776beddb5f2b80a2decb22a776287))

* project: update version requirement for momotor-engine-shared ([`3baeb79`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/3baeb7904975b983aa29cc3e7a83d1830432e9ef))

* doc: update documentation ([`f59f5bc`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/f59f5bcfc8b2a0858dcc337784ad180c2a18c46a))

* project: correct docs/build exclusion ([`c95434b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/c95434bbecc7e30f9344aef56a420318c9e83ebb))


## v1.3.0 (2020-04-17)

### Feature

* feat: allow model to be overridden in the model token store ([`01e77a0`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/01e77a021b8fa9db347fadceb294e5e2c94af675))

### Fix

* fix: lock external store to prevent race conditions ([`2f57a08`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/2f57a08a6a731d07260ee8aa665b347644d0c15e))

* fix: set in-memory token when retrieved from external source ([`cfcf54f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/cfcf54f256e2065b36518a8da38cdce501239151))

* fix: rename TOKEN_POOL_CLASS to TOKEN_STORE_CLASS. Still accepting old name with deprecation warning ([`57eab1a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/57eab1a9f0a9345299471b7241f755b9a05414f5))

### Unknown

* 1.3.0

&#39;chore: bump version number&#39; ([`154d16a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/154d16a98b2da64b4688da7b4db22cf935fced9a))

* doc: document set argument and instance variables ([`68de8c1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/68de8c1e4ebfa207444dcbc5add7d991fb8f82ae))

* doc: links to Django documentation for cache and db ([`03dcabb`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/03dcabb82d1bdac3fcabaf2f81b8ab170e3d3985))

* doc: fix typo and other small fixes ([`b6de5bc`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/b6de5bc758df134557139287cac2f1fcf7c26458))

* doc: update connection doc ([`61a094f`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/61a094fd76e2c705d7757ab69844cd6f25bd1b04))

* doc: update intersphinx mapping ([`dce931a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/dce931a9ef068bc77f9dff29c7ba57cb78a6398b))

* doc: document retry_connection ([`acc0461`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/acc0461b6573ea866485f29ab8d53aa9183cd5e3))

* doc: update settings doc ([`a4c6cee`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/a4c6cee606114250913bba29726274c2b47e4882))

* doc: document BrokerConnection ([`9bfcbd1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/9bfcbd16c0a75c2f3557c17547fbbe610bfcb623))

* doc: extend token store documentation ([`a172477`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/a172477b3ce41d3d777270d8f2ddf6b8f3f42612))

* doc: document token store abstract base ([`73c41df`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/73c41df511643938fb57dc9d98ebccdc2ed53a74))

* doc: document token store ([`60b962b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/60b962b1639561ba067ffd7171e4782323f78ee0))

* doc: document settings ([`eafbe48`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/eafbe48ce166b7fb502192e3832d5066afe7b37b))

* doc: enable Django ([`f5c0b2a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/f5c0b2a0b464ee81b5a70a85807769a2b96e431d))

* doc: add sphinx to dependencies ([`a726553`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/a726553da39e7d7c66ef77ad1ab35a8cdf5247e6))

* doc: updated files and added skeleton for documentation ([`deb5182`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/deb5182a1cf89c39fc64979d608627bcdd0d096b))


## v1.2.0 (2019-10-15)

### Feature

* feat: add SSL connection support ([`8c7cb4a`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/8c7cb4a72114653cf6d8c8a88cf11bef0ab74c83))

### Fix

* fix: retry getting stub on connection errors ([`d58f7f4`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/d58f7f4e2dc69ce36a44d354d1a151d29f5194bb))

* fix: add SSL exceptions to list of exceptions to retry ([`f1236ed`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/f1236ed646450b8f68c98cbce8c973a4ccff9798))

### Refactor

* refactor: use contextlib.asynccontextmanager on Python&gt;=3.7 ([`a18ed12`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/a18ed12541d1c0c8873dcade50a89697a562afb0))

### Unknown

* 1.2.0

&#39;[ci skip] Automated release&#39; ([`913f17d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/913f17d8eb66c370a6d465e2fa1a047428a59b94))


## v1.1.1 (2019-10-04)

### Fix

* fix: correct import for Message type ([`fc4ec2c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/fc4ec2ce7b6f21046935f02e372d54a7fc3c457a))

### Unknown

* 1.1.1

&#39;[ci skip] Automated release&#39; ([`a4f034b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/a4f034b9f8e5b669ad4b9093b5aef94cce69a1ff))


## v1.1.0 (2019-09-27)

### Feature

* feat: add Django model field for Resources ([`1ecafaa`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/1ecafaafbe331c115ad92f593501fb455801851d))

### Refactor

* refactor: logging changes

* no uppercase initial characters ([`dc59dd7`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/dc59dd75028dd9a301cd76ef1106d858b28bb68b))

* refactor(conn): use `momotor.rpc.auth.client.get_authenticated_channel` ([`99665c1`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/99665c1cec928d40e6874e34719660136e80bff5))

### Unknown

* 1.1.0

&#39;[ci skip] Automated release&#39; ([`3cb894c`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/3cb894ca210a1fc9ce7fc18348f4301e5007594e))

* Reverted grpclib version pin, since 0.2.5 is unstable due to an issue in h2

See https://github.com/vmagamedov/grpclib/issues/78 and https://github.com/python-hyper/hyper-h2/issues/1183 ([`0e06e13`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/0e06e13a63d1881c5eda5b0de62bc5942b56f65f))


## v1.0.0 (2019-05-23)

### Breaking

* feat: turn into a full Django app

* Configurable through settings
* Multiple storage classes for the authentication tokens

BREAKING CHANGE: requires `MOMOTOR_BROKER` settings to be added

Example of a minimal `MOMOTOR_BROKER` configuration:

```python
MOMOTOR_BROKER = {
    &#39;HOST&#39;: &#39;broker.example.org&#39;,
    &#39;PORT&#39;: 12345,
    &#39;API_KEY&#39;: &#39;8w45teiutngewrgn3498eytjh3e&#39;,
    &#39;API_SECRET&#39;: &#39;...&#39;,
}
```

Existing `MOMOTOR_GEN2` setting can be renamed to `MOMOTOR_BROKER` and will work ([`f8908dd`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/f8908dd87d91c9895e7ffc3932ae762a468bde15))

### Unknown

* 1.0.0

&#39;[ci skip] Automated release&#39; ([`f717728`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/f71772823ebf41cf2114db501825096645980ecd))

* Add InMemoryTokenStore, use it as base for cached and database token stores ([`7bb2422`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/7bb24228f0968aba89758029b89c4a8e5056379c))

* Fix return value of CachedTokenStore.get ([`1d83032`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/1d8303215c28ef7262931de7596ecdecc9452da6))

* Correct async to sync wrapping ([`6ec1a1d`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/6ec1a1db46dd4b0be0502d7b0e2f9212325e797c))

* DateTimeField should be &#39;auto_now_add&#39; ([`abf4f98`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/abf4f98fab5924be0d1b0ad4e6afacf109c9de5e))


## v0.1.0 (2019-05-20)

### Feature

* feat: export retry_connection ([`9865e37`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/9865e37baa7d7282e33fe3450fc9408eed6151eb))

### Unknown

* 0.1.0

&#39;[ci skip] Automated release&#39; ([`e539148`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/e5391484a4eeac3c36b8b07ecb896bf07d50c07e))


## v0.0.0 (2019-05-20)

### Unknown

* Initial commit ([`8c1af8b`](https://gitlab.tue.nl/momotor/engine-py3/momotor-django/-/commit/8c1af8b97c9040527aa9327d91a26214a2552093))
