class JsonWrapperException(Exception):
    pass


class Wrapper:

    def __init__(self, collection=None):
        if collection:
            self._static_load(self, collection)

    def __repr__(self):
        res = "{"
        for e in self.__dict__.items():
            if len(res) > 1:
                res += ', '
            val = f'"{e[1]}"' if isinstance(e[1], str) else e[1]
            res += f'"{e[0]}": {val}'
        res += "}"
        return res

    @staticmethod
    def _set_attribute(instance, name, value):
        if name.find('$') > -1:
            name = name.replace('$', '')
        if name.find('-') > -1:
            name = name.replace('-', '_')
        if name.find('#') > -1:
            name = name.replace('#', '')
        if not hasattr(instance, name):
            setattr(instance, name, value)

    @staticmethod
    def _static_load(instance, collection):
        if isinstance(collection, dict):
            for el in collection.items():
                n, v = el[0], el[1]
                if isinstance(v, dict):
                    Wrapper._set_attribute(instance, n, Wrapper(v))
                elif isinstance(v, list):
                    li = v
                    # the code assume if first element is list or dict, the others are same type
                    if isinstance(v[0], dict) or isinstance(v[0], list):
                        li = [Wrapper(ele) for ele in v]
                    Wrapper._set_attribute(instance, n, li)
                else:
                    Wrapper._set_attribute(instance, n, v)
        if isinstance(collection, list):
            Wrapper._set_attribute(instance, 'list', [Wrapper(el) for el in collection])


class JONFactory:

    @staticmethod
    def wrap(instance):
        if isinstance(instance, dict):
            return Wrapper(instance)
        if isinstance(instance, list):
            return [Wrapper(el) for el in instance]
        raise JsonWrapperException(f'Type({type(instance)}) handing not supported!')
