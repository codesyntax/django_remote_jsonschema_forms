from django.utils.encoding import force_str
from django.utils.functional import Promise

from django_remote_jsonschema_forms import logger


def resolve_promise(o):
    if isinstance(o, dict):
        for k, v in o.items():
            o[k] = resolve_promise(v)
    elif isinstance(o, (list, tuple)):
        o = [resolve_promise(x) for x in o]
    elif isinstance(o, Promise):
        try:
            o = force_str(o)
        except Exception as e:
            logger.warning(e)

            try:
                o = [resolve_promise(x) for x in o]
            except Exception as ex:
                logger.warning(ex)
                raise Exception("Unable to resolve lazy object %s" % o)
    elif callable(o):
        o = o()

    return o
