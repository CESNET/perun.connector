## [1.1.2](https://github.com/CESNET/perun.connector/compare/v1.1.1...v1.1.2) (2022-05-26)


### Bug Fixes

* moved CurlConnector to satosacontrib.perun ([e5ab8bd](https://github.com/CESNET/perun.connector/commit/e5ab8bdf53ea544608d79b12f63e237415e3a999))


### Reverts

* put back __init__.py files ([f7f142d](https://github.com/CESNET/perun.connector/commit/f7f142d9b0ae60ee6585cbd17c8b3ef291b414c1))

## [1.1.1](https://github.com/CESNET/perun.connector/compare/v1.1.0...v1.1.1) (2022-05-26)


### Bug Fixes

* hide implementation files in package ([d8f0921](https://github.com/CESNET/perun.connector/commit/d8f0921fe039b993c6e98dfd1adb1ad2c415ac6c))

# [1.1.0](https://github.com/CESNET/perun.connector/compare/v1.0.2...v1.1.0) (2022-05-26)


### Features

* packages tree, configs changes - attrs_map now has to be passed to Adapters constructor ([efdc828](https://github.com/CESNET/perun.connector/commit/efdc828b44ef863e53a99c3786769bb1abe30539))

## [1.0.2](https://github.com/CESNET/perun.connector/compare/v1.0.1...v1.0.2) (2022-05-23)


### Bug Fixes

* directories changed to packages ([a6372c1](https://github.com/CESNET/perun.connector/commit/a6372c15e74bab090abe87a21bbbdc1e510c3c82))

## [1.0.1](https://github.com/CESNET/perun.connector/compare/v1.0.0...v1.0.1) (2022-05-17)


### Bug Fixes

* publish to pypi ([350c2ac](https://github.com/CESNET/perun.connector/commit/350c2ace261a5f335cef74fdaffba0b4d878eec5))

# 1.0.0 (2022-05-16)


### Bug Fixes

* changed incorrect return type of the method get_user_ext_source ([d4c1177](https://github.com/CESNET/perun.connector/commit/d4c117787b2dfcaf834be77084b5a5d2cdb03d7e))
* config store import in AttributeUtils ([700e348](https://github.com/CESNET/perun.connector/commit/700e348aa11211cf814a1a5b68639544716e7665))
* fixed syntax error and formatting issues ([d661fa8](https://github.com/CESNET/perun.connector/commit/d661fa89c1ef91c22f710b193e40c65d1788358f))
* imports in models, models to_strings, UserExtSource userId -> User ([14b6d55](https://github.com/CESNET/perun.connector/commit/14b6d55ce7a921ebbd7215339ebb62fe9ecaf72d))
* missing abc.abstractmethod tags in AdapterInterface ([53c8e3e](https://github.com/CESNET/perun.connector/commit/53c8e3e1f6e5707597798581b8d02b1a48bb445f))
* openapi config bug ([e5c617e](https://github.com/CESNET/perun.connector/commit/e5c617e610309426da21a65eb08e721fb2d98aab))
* set and get user ext source attributes methods now have right parameters types ([f1d7a10](https://github.com/CESNET/perun.connector/commit/f1d7a104365b3534c398625eae7041c7d3e7d674))
* userExtSource openApi bug ([ae0a343](https://github.com/CESNET/perun.connector/commit/ae0a343b6710eb18ced3b18f5804cff12308f936))


### Features

* added adapters manager ([e509ab5](https://github.com/CESNET/perun.connector/commit/e509ab5b5702e17cd75c31aa095aceddb200cf40))
* added tests for adapters manager ([24710e0](https://github.com/CESNET/perun.connector/commit/24710e0221a10630ddc2facf93b75da74b8497e2))
* added user ext source model content ([4fac95f](https://github.com/CESNET/perun.connector/commit/4fac95fef26cd08e503c9fa758049fe2e9612b43))
* adjusted types and naming of attributes and parameters ([e80b66c](https://github.com/CESNET/perun.connector/commit/e80b66c594a2c3992f8a6e25d683c89550f5b4ba))
* all Adapters functions take object or id of object as parameter ([816c9cd](https://github.com/CESNET/perun.connector/commit/816c9cd9482a31729de5946806fbdd464532d00e))
* changed attributes of user ext source model ([5d2f79e](https://github.com/CESNET/perun.connector/commit/5d2f79e46f7ad12602a344f60c06ca7a2b16ff8c))
* changed project structure ([344137b](https://github.com/CESNET/perun.connector/commit/344137bb24535f934ff3e6163384711493b90770))
* configStore class and config templates ([b93936d](https://github.com/CESNET/perun.connector/commit/b93936d4080dac96ec0ba107befdd630fc117ae7))
* generated openApi client, requirements.txt ([621ef10](https://github.com/CESNET/perun.connector/commit/621ef10a1f8f7754006d0fc39b17299ed56cc985))
* github actions run tests ([a4d1758](https://github.com/CESNET/perun.connector/commit/a4d175841e4d838b6d12d6fa092dec4b078b85b2))
* Implemented AdapterInterface and Models ([1864a6b](https://github.com/CESNET/perun.connector/commit/1864a6bc5035aaca0699abe8278e0d154cf06093))
* implemented attribute utils ([d114854](https://github.com/CESNET/perun.connector/commit/d114854dd24d0986564db411a98742c06281cb57))
* implemented curl connector ([5e16c33](https://github.com/CESNET/perun.connector/commit/5e16c338df1cce2816129c673486e11f32e989c8))
* implemented rpc adapter ([0261aeb](https://github.com/CESNET/perun.connector/commit/0261aeb9b65bbfc8fd43da8b6709840fda5d094a))
* implemented tests for rpc adapter ([f4be4d3](https://github.com/CESNET/perun.connector/commit/f4be4d37f2a805d61266ba9e9fdb1bbac1e74798))
* **incorporated-changes-from-previous-pull-request-comments:** - made HasId an abstract class containing ID, removed __ notation from models' attributes, added toString methods for models, changed id attribute types to string in AdapterInterface, added input validation for member status attribute, removed get_attributes_*_values methods and changed return type of get_*_attributes in AdapterIntefrace ([4e1a4e2](https://github.com/CESNET/perun.connector/commit/4e1a4e225d291568bffead4a52cdf0628ef7ca2c))
* initial commit ([16e4b95](https://github.com/CESNET/perun.connector/commit/16e4b9595ef4e80ef8e22dd5ca974120b0f7e2b1))
* Ldap Connector ([e518634](https://github.com/CESNET/perun.connector/commit/e5186347de1cdaac3b2098665bbe67a436fd4f2c))
* LdapAdapter impemented ([a14c9d7](https://github.com/CESNET/perun.connector/commit/a14c9d738258284732ec84015b48a29168c32ca8))
* openApi regenerated ([bfd853d](https://github.com/CESNET/perun.connector/commit/bfd853d54996939e7dea3eb329a15a594db69461))
* openapi searcher and new usersManager methods ([801ea51](https://github.com/CESNET/perun.connector/commit/801ea51079ba980810c7a46e36ae54e82bb88bad))
* pycurl dependencies to build ([3d7deb8](https://github.com/CESNET/perun.connector/commit/3d7deb832301b3b3125e8899c4b3399a68b54586))
* semantic release ([59a28b7](https://github.com/CESNET/perun.connector/commit/59a28b7da53a21de0253e9bfede35b5990daaf5f))
* tests for LDAP adapter and ldap connector ([db04522](https://github.com/CESNET/perun.connector/commit/db045224505fdc2e97b83a0adbe075195a025a5e))
* updated adapterInterface ([f8e6b7c](https://github.com/CESNET/perun.connector/commit/f8e6b7c5890548033f58f223faa443f1f0caa06e))
* updated flake8 settings ([68138e3](https://github.com/CESNET/perun.connector/commit/68138e3eb0719057b84415b1f4cab28e9769693a))
