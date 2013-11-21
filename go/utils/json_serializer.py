# See: http://stackoverflow.com/a/2251213/806988
from json import dumps, loads, JSONEncoder

from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.db import models
from django.utils.functional import curry


class DjangoJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            # `default` must return a python serializable
            # structure, the easiest way is to load the JSON
            # string produced by `serialize` and return it
            return loads(serialize('json', obj))
        elif isinstance(obj, models.Model):
            return obj.to_dict()
        return JSONEncoder.default(self, obj)

# partial function, we can now use dumps(my_dict) instead
# of dumps(my_dict, cls=DjangoJSONEncoder)
model_to_json = curry(dumps, cls=DjangoJSONEncoder)
