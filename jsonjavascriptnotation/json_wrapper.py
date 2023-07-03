class JsonWrapperException(Exception):
    pass


class Wrapper:

    def __init__(self, collection=None):
        self.__wrapper_normalized_names = {}
        if collection:
            self._static_load(self, collection)

    def __repr__(self):
        res = "{"
        for e in self.__dict__.items():
            name = e[0]
            if name == "_Wrapper__wrapper_normalized_names":
                continue
            if len(res) > 1:
                res += ', '
            if isinstance(e[1], str):
                val = f'"{e[1]}"'
            elif isinstance(e[1], bool):
                val = 'true' if e[1] else 'false'
            else:
                val = e[1]
            if name in self.__wrapper_normalized_names.keys():
                name = self.__wrapper_normalized_names[name]
            res += f'"{name}": {val}'
        res += "}"
        return res

    @staticmethod
    def _normalize(instance, name):
        res = name
        normalized = False
        if res.find('$') > -1:
            res = res.replace('$', '')
            normalized = True
        if res.find('-') > -1:
            res = res.replace('-', '_')
            normalized = True
        if res.find('#') > -1:
            res = res.replace('#', '')
            normalized = True
        if normalized:
            instance.__wrapper_normalized_names.update({res: name})
        return res

    @staticmethod
    def _set_attribute(instance, name, value):
        nname = Wrapper._normalize(instance, name)
        if not hasattr(instance, nname):
            setattr(instance, nname, value)

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
