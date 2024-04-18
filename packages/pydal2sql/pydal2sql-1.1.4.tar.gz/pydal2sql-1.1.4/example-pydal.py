# db = DAL("sqlite:memory")
#
# db.define_table('person')
#
# db.define_table('user')
# print(0)
# db
#
#
# print(
#     db(db.user).select()
# )
#
#
# print(
#     db.user.truncate()
# )

import veryfake

import os
import json
import httpx

import typing
import attrs
from attrs import define, field, Factory, asdict, evolve
import copy
import shlex
import hashlib
import random
from pydal.objects import Rows

if typing.TYPE_CHECKING:
    import lorem
    from gluon import URL, auth, request
    from pydal import *
    from pydal.objects import *
    from pydal.validators import *
    from yatl import *
    from sys import something


# db.define_table('my_table', Field('some_string', validator=some_external_variable, default=imported))
db.define_table('my_table', Field("some_string", default=something))

db.define_table("relates", Field("user", "references auth_user"))