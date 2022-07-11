class Url:
    def __init__(self,scheme='', authority='', path=None, query=None, fragment=None):
        self.scheme= scheme
        self.authority=authority
        self.path= path
        self.query = query
        self.fragment = fragment

    def __str__(self):
        if self.path is not None:
            path = '/'
            path += '/'.join(self.path)
        else:
            path =''
        if self.query is not None:
            query = str('?')
            for key, value in self.query.items():
                query += f'{str(key)}={str(value)}&'
        else:
            query = ''

        if self.fragment is not None:
            fragment = '#'
            fragment += self.fragment
        else:
            fragment = ''

        result = f'{self.scheme}://{self.authority}{path}{query[:-1]}{fragment}'
        return result

    def __eq__(self, other):
        if self.__str__() == other:
            return True

class HttpsUrl(Url):
    def __init__(self, schema='https', authority='', path=None, query=None, fragment=None):
        super().__init__(schema, authority, path, query, fragment)

class HttpUrl(Url):
    def __init__(self, schema='http', authority='', path=None, query=None, fragment=None):
        super().__init__(schema, authority, path, query, fragment)

class GoogleUrl(Url):
    def __init__(self, schema='https', authority='google.com', path=None, query=None, fragment=None):
        super().__init__(schema, authority, path, query, fragment)

class WikiUrl(Url):
    def __init__(self, schema='https', authority='wikipedia.org', path=None, query=None, fragment=None):
        super().__init__(schema, authority, path, query, fragment)


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'

##############################################

class UrlCreator():

    def __init__(self, scheme='', authority=''):
        self.scheme = scheme
        self.authority = authority

    def __call__(self, *args, **kwargs):
        def _create():
            args1 = '/'
            args1 += '/'.join(args).replace(',','/')
            result = f'{self.scheme}://{self.authority}{args1}'
            return result
        return _create()

    def __getattr__(self, item):
        return item

    def __eq__(self, other):
        if self.__str__() == other:
            return True

url_creator = UrlCreator(scheme='https', authority='docs.python.org')
assert url_creator.docs.v1.api.list == 'https://docs.python.org/docs/v1/api/list'
assert url_creator('api,v1,list') == 'https://docs.python.org/api/v1/list'
assert url_creator(api,v1,list, q='my_list') == 'https://docs.python.org/api/v1/list?q=my_list'

assert url_creator('3').search(q='gettattr', check_keywords='yes', area='default')._create()  == 'https://docs.python.org/3/search?q=getattr&check_keywords=yes&area=default'