from pyco_types._common import CommonException, G_Symbol_UNSET


class CoDict(dict):
    ##; attr 只能使用 getattr 的方法访问
    _prviate_attr_map = {}  # type: dict
    ##; data 是缺省字段表, 
    _default_data_map = {}  # type: dict

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def x_set_attr_map(self, **kwargs):
        self._prviate_attr_map = kwargs

    def x_set_data_map(self, **kwargs):
        self._default_data_map = kwargs

    @property
    def x_attr_map(self):
        return self._prviate_attr_map

    @property
    def x_data_map(self):
        return self._default_data_map

    def to_dict(self, verbose=0):
        if verbose <= 0:
            return self
        elif verbose == 1:
            return dict(self, **self.x_data_map)
        elif verbose == 2:
            return dict(self, **self.x_data_map, private_attr_map=self._prviate_attr_map)
        else:
            ## extent
            return dict(self)

    def __getitem__(self, key):
        v = super().get(key, G_Symbol_UNSET)
        if v is G_Symbol_UNSET:
            errno = 0
            if not self.x_data_map:
                errno = 40040
            else:
                v = self.x_data_map.get(key, G_Symbol_UNSET)
                if v is G_Symbol_UNSET:
                    errno = 40041
            if errno:
                raise CommonException(
                    error_msg=f"<CoDict>.getitem({key}) failed! "
                              f"suggest to update with $.x_set_data_map()",
                    errno=errno,
                    origin_data=self,
                    default_map=self.x_data_map
                )
        return v

    def __getattr__(self, item):
        ##; 先调用 __getattribute__，然后因为属性不存在调用 __getattr__
        try:
            return self[item]
        except Exception as e:
            raise CommonException(
                f"<CoDict>.getattr({item}) failed! ({self})",
                errno=40042,
                origin_data=self,
            )

    def __setattr__(self, key: str, value):
        ##; 所有的内部属性，必须使用 "_" 作为前缀
        if key.startswith("_"):
            # Assign to the special 'my_attr' property
            super().__setattr__(key, value)
        else:
            # Set the normal dictionary key-value pair
            self[key] = value

    def __delattr__(self, item):
        try:
            del self[item]
        except KeyError:
            raise AttributeError(f"<CoDict>:: delattr({self}), {item}")
