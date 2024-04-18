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

from typedal import TypedTable
from typedal.fields import ReferenceField


@db.define
class MyTable(TypedTable):
    some_string: str
    some_other = TypedField(default=something)


@db.define
class Relates(TypedTable):
    table: MyTable
    user = ReferenceField("auth_user")
