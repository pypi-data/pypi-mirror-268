import xmlrpc.client
from functools import reduce
from .common import assert_same_model, cache, log_request, model, frozendict
from .utils import is_relational_field
from typing import Union


class RecordSet:
    def __init__(self, name, env, ids: list[int] = None, context: frozendict = None):
        self._name = name
        self._env = env
        self._curr = -1
        self._ids = self._sanitize_ids(ids or list())

        """
        Each recordset has its own context, but inherits it:
            1) from the recordset it was created
            2) from the general environment 
        """
        self._context = context.copy() if context is not None else frozendict()

        self.logger = self._env.logger

    def __str__(self):
        return f"{self._name}({', '.join(map(str, self._ids))})"

    __repr__ = __str__

    def __bool__(self):
        return bool(self._ids)

    def __len__(self):
        return len(self._ids)

    def __iter__(self):
        self._curr = -1
        return self

    def __next__(self):
        if self._curr < len(self) - 1:
            self._curr += 1
            return self._recordset(self._ids[self._curr])
        raise StopIteration

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self._recordset(self._ids[item])
        elif isinstance(item, str):
            return getattr(self, item)

    def __getattr__(self, attr):
        if attr != 'fields_get' and self._env.cache[self._name].field_exists(attr):
            return self._env.cache[self._name].get(self._ids, attr, context=self._context)
        else:
            def wrapper(*args, **kw):
                return self._execute(attr, *args, **kw)
            return wrapper

    # --- Operators ---
    @assert_same_model('union')
    def __or__(self, other):
        return self._recordset(self.ids + other.ids)

    @assert_same_model('union')
    def __ior__(self, other):
        self._ids += other.ids
        return self

    def ensure_one(self):
        if len(self) != 1:
            raise ValueError(f"Expected singleton: {self}")

    # --- Properties ---
    @property
    def env(self):
        return self._env

    @property
    def ids(self):
        return self._ids

    @property
    def context(self):
        return self._context

    @property
    def id(self):
        return False if not self._ids else self._ids[0]

    @property
    def _model(self):
        return self._env[self._name]
        # return self._recordset(list())

    @property
    def model_cache(self):
        return self._env.cache[self._name]


    def _recordset(self, ids: Union[list[int], int]):
        ids = [ids] if isinstance(ids, int) else ids
        return self.__class__(self._name, self._env, ids, context=self._context)

    @staticmethod
    def _sanitize_ids(ids: Union[list[int], int]):
        ids = ids if isinstance(ids, list) else [ids]
        seen = set()
        return [i for i in ids if not (i in seen or seen.add(i))]

    @staticmethod
    def _format_domain(domain: list[tuple]) -> list[list]:
        return list(map(lambda e: e if isinstance(e, str) else list(e), domain))

    @log_request
    def _execute(self, method, *args, **kw):
        """ Add ids in args if method is not @model decorated"""
        if not (m := getattr(self, method, None)) or (getattr(m, '_api', None) != 'model'):
            args = [self._ids] + list(args)
        kw['context'] = self.context | kw.get('context', dict())

        try:
            return self._env.models.execute_kw(
                self._env._db,
                self._env.uid,
                self._env._password,
                self._name,
                method,
                args,
                kw,
            )

        except Exception as e:
            if isinstance(e, xmlrpc.client.Fault) and 'cannot marshal' in str(e):
                return None
            self.logger.error(f"Error while executing {self._name}.{method}():")
            self.logger.debug(f"args / kwargs:\n {args} \n {kw}")
            self.logger.error("Odoo API Response:\n" + str(e).replace('\\n', '\n'))
            raise e

    # --------------------------------------------
    #                   ORM
    # --------------------------------------------


    def browse(self, ids: Union[int, list[int]]) -> "RecordSet":
        return self._recordset(ids)

    # def fields_get(self, attributes: list[str] = None):
    #     return self._execute('fields_get', attributes=attributes)

    @model
    def check_object_reference(self, module, xml_id):
        # Extra safety check, don't delete (even if nobody should use it directly)
        if self._name != 'ir.model.data':
            return self['ir.model.data'].check_object_reference(module, xml_id)
        return self._execute('check_object_reference', module, xml_id)

    def with_context(self, **kw):
        self._context = self._context.copy(**kw)
        return self


    # --- CRUD ---


    @model
    def search(self, domain: list[tuple], **kw):
        ids = self._execute('search', self._format_domain(domain), **kw)
        return self._recordset(ids)

    @cache('read')
    def read(self, fields: list[str] = None, **kw) -> list[dict]:
        fields = fields or list()
        res = self._execute('read', fields=fields, **kw)
        return res

    @model
    def search_read(self, domain: list[tuple], fields: list[str] = None, **kw):
        fields = fields or list()
        res = self._execute('search_read', self._format_domain(domain), fields=fields, **kw)
        return self._recordset([r.get('id') for r in res])

    @model
    def search_count(self, domain: list[tuple]):
        return self._execute('search_count', self._format_domain(domain))

    @model
    @cache('create')
    def create(self, vals_list: Union[dict, list[dict]]):
        vals_list = vals_list if isinstance(vals_list, list) else [vals_list]
        ids = self._execute('create', vals_list)
        return self._recordset(ids)

    @cache('write')
    def write(self, vals: dict):
        return self._execute('write', vals)

    @cache('delete')
    def unlink(self):
        res = self._execute('unlink')
        return res

    def copy(self):
        res_id = self._execute('copy')
        return self._recordset(res_id)


    # --- ORM helpers ---


    def mapped(self, field: str):
        """ Perform a read only if any of the record has dirty cache """
        if not self.env.cache_enabled or self.cache_expired(field):
            read_res = self.read([field])
            if not self.env.cache_enabled:
                self.env.logger.warning(f"With cache disabled, the result of mapped() is quite different from Odoo's behavior in case of relational fields. It only returns a list with raw results from API for now.")
                return [rec.get(field) for rec in read_res]

        res = [getattr(rec, field) for rec in self]
        # Return a recordset if the field is relational
        if is_relational_field(self.get_field_info(field, 'type')):
            res = reduce(lambda a, b: a | b, res)
            res = res.with_context(**self.context)

        return res


    def filtered(self, func: Union[callable, str]):
        if isinstance(func, str):
            name = func
            func = lambda rec: rec[name]
            # func = lambda rec: any(rec.mapped(name))      # Odoo behavior
        return self.browse([rec.id for rec in self if func(rec)])

    def filtered_domain(self, domain: list[tuple]):
        return self.search([('id', 'in', self.ids)] + domain)



    # --------------------------------------------
    #              CACHE HELPERS
    # --------------------------------------------


    def cache_expired(self, field: str):
        return self.model_cache.cache_expired(field, self.ids)

    def get_field_info(self, field: str, info: str):
        if self.model_cache.field_exists(field):
            return self.model_cache.fields[field][info]
        return None


