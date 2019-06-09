from .utils import query, get_paths

class QuerySelectorException(Exception):
  def __init__(self, msg=None):
    if not msg:
      msg = "No selector given to perform the query"
    super().__init__(msg)

class QueryConditionException(Exception):
  def __init__(self, msg=None):
    if not msg:
      msg = "No selector given to perform the query"
    super().__init__(msg)


class Query:

  def __init__(self, iter_):
    """Initialize a query to be performed on the given iterable."""
    self.iter_     = iter_
    self.selector  = None
    self.flat      = False
    self.condition = None
    self.grouping  = None

  def exec(self):
    if not self.selector:
      raise QuerySelectorException()
    select_r  = query(self.iter_, self.selector)
    condition = lambda x: True
    if self.condition:
      condition = self.condition
    for result in select_r:
      if self.flat is True:
        for result_element in result:
          if condition(result_element):
            yield result_element
      else:
        if condition(result):
          yield result

  def where(self, condition):
    if not self.selector:
      raise QuerySelectorException()
    self.condition = condition
    return self

  def flatten(self):
    """Flat selector results.
    This is used to flat lists retrieved by the select statement.
    """
    if not self.selector:
      raise QuerySelectorException()
    if self.condition:
      raise QueryConditionException("The condition for the query has" +\
      " been already set")
    self.flat = True
    return self

  def select(self, field):
    """Given a field, look for it through the dictionary.
    If field is a sequence, then it will be considered as the desired
    path to search for.
    """
    if not isinstance(field, str) and len(field) > 0:
      path = field
    else:
      paths = [path for path in get_paths(self.iter_)\
               if path[-1] == field]
      if not len(paths):
        return ()
      path = paths[0]
    self.selector = path
    return self
