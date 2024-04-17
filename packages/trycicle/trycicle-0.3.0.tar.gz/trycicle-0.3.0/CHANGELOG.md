# CHANGELOG



## v0.3.0 (2024-04-16)

### Documentation

* docs: add cache example to readme ([`dfc5336`](https://gitlab.com/phooijenga/trycicle/-/commit/dfc5336bed36ac37c10d65a1979f8f22af6bbef8))

### Feature

* feat: refactor how extends are applied

Previously the parser would construct a set of partial job objects.
When a job was requested from the config, it would resolve each field
independenly, following the extends keyword to parent jobs if necessary.

This meant that to merge fields like `variables`, special handling was
necessary, which was not available to other fields (like `cache`).

The parser now merges values from `extends`, `default` and globals in
the same way (and only when the job is requested from the config). ([`b2cb7ea`](https://gitlab.com/phooijenga/trycicle/-/commit/b2cb7ea332b0989e3ea12cc6e283f72994092110))

* feat: implement caches ([`d2dce55`](https://gitlab.com/phooijenga/trycicle/-/commit/d2dce554de404deb17adc0ba719fa2ddee793882))

### Fix

* fix: add source directory name to cache key ([`3a2eb24`](https://gitlab.com/phooijenga/trycicle/-/commit/3a2eb242e6fd8d498b5f2cb7402bf917134ea04e))

* fix: ensure directories exist when copying cache ([`f813d6f`](https://gitlab.com/phooijenga/trycicle/-/commit/f813d6f44b81473abe475a909dccfa69a62c7639))

* fix: use user cache directory ([`5356312`](https://gitlab.com/phooijenga/trycicle/-/commit/535631254c76b2999a6218f08fc0787690a752cd))

* fix: allow cache without key ([`0d83b73`](https://gitlab.com/phooijenga/trycicle/-/commit/0d83b7347197010b6d6317091d3e555c3b2176d2))

### Test

* test: add cache test ([`a4d9c4c`](https://gitlab.com/phooijenga/trycicle/-/commit/a4d9c4ce229a967671c90d640900ca90e432888b))


## v0.2.2 (2024-03-31)

### Chore

* chore(release): version 0.2.2 ([`8e574c6`](https://gitlab.com/phooijenga/trycicle/-/commit/8e574c69e96d0334ef167994e681eba825abfa43))

### Fix

* fix(ci): skip version job only ([`4d01c5e`](https://gitlab.com/phooijenga/trycicle/-/commit/4d01c5ea12619264ad098c27bd7280190f0c21de))


## v0.2.1 (2024-03-31)

### Chore

* chore(release): version 0.2.1 [skip ci] ([`c3ac08e`](https://gitlab.com/phooijenga/trycicle/-/commit/c3ac08e69dfed126cc6963e1d737b9c8d55d75f4))

### Fix

* fix(ci): skip pipeline on version commit ([`8bf80a8`](https://gitlab.com/phooijenga/trycicle/-/commit/8bf80a827428caa1aaed0ef8d76306c04ae2e8f0))


## v0.2.0 (2024-03-31)

### Chore

* chore(release): 0.2.0 ([`84fc81b`](https://gitlab.com/phooijenga/trycicle/-/commit/84fc81b1fd371c768ecfe9cfe480490c12d72776))

### Feature

* feat: automate releases ([`6d1ba46`](https://gitlab.com/phooijenga/trycicle/-/commit/6d1ba467136808d1477ed1197848e4984c1b632a))

* feat: use prebuilt images in CI ([`d0d0275`](https://gitlab.com/phooijenga/trycicle/-/commit/d0d0275aa29560f58d2c93a0c0be4821ba8b3c27))

* feat: build images to be used in CI ([`9466d2d`](https://gitlab.com/phooijenga/trycicle/-/commit/9466d2d3f1713268cedd2a9bf8e2ee9b36c58384))

### Fix

* fix(ci): job token can not push to repository ([`79d8348`](https://gitlab.com/phooijenga/trycicle/-/commit/79d8348bf64fcd56f9644b043fefcf2a166af35e))


## v0.1.1+1 (2024-03-19)

### Unknown

* Add tags to CI workflow rules ([`2c55ce2`](https://gitlab.com/phooijenga/trycicle/-/commit/2c55ce25db97d993fd6ac8ac014774dc6173d50a))


## v0.1.1 (2024-03-19)

### Unknown

* Version 0.1.1 ([`bf7a1e4`](https://gitlab.com/phooijenga/trycicle/-/commit/bf7a1e425c847c0e70740ea48118315fe431aa21))

* Publish tags to PyPI ([`302cac0`](https://gitlab.com/phooijenga/trycicle/-/commit/302cac06471a09282990d98e45574105e5ba7178))

* Remove private classifier ([`a9d4494`](https://gitlab.com/phooijenga/trycicle/-/commit/a9d44945aae89d8a069cee69d20287a41d1b5a9c))

* Flush output after each line ([`fd80b90`](https://gitlab.com/phooijenga/trycicle/-/commit/fd80b903ab1012b76c1e54df79f49d76c87038fb))

* Add LICENSE ([`7a6e623`](https://gitlab.com/phooijenga/trycicle/-/commit/7a6e623a7cecc8795b840cb52ab517216ba74ff4))

* Add interactive debugger

Closes #6. ([`c72bc59`](https://gitlab.com/phooijenga/trycicle/-/commit/c72bc59f2b07a7e0fbd75610ab0979e207c6af9e))

* Label containers ([`fc8471f`](https://gitlab.com/phooijenga/trycicle/-/commit/fc8471fe269e2b7b3382384595f249c6c36ffd69))

* Reset log level before running integration tests ([`1f66207`](https://gitlab.com/phooijenga/trycicle/-/commit/1f66207eccffadb6f796ee7a8f540a8aae3a6bca))

* Add instructions to set up tab completion to readme

Closes #7. ([`14ce3a8`](https://gitlab.com/phooijenga/trycicle/-/commit/14ce3a821be9f4fff4e100429be79de04d292150))

* Add shell completion for jobs and variables ([`cdbc707`](https://gitlab.com/phooijenga/trycicle/-/commit/cdbc70793f456fbf211aa23677a0718db48674fc))
