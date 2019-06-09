# BFS on trees described by adjacent lists
def traverse(graph, root):
  stack = graph[root]
  while stack:
    node = stack.pop(0)
    print(node)
    stack.extend(graph[node])

def traverse2(graph, root):
  stack = [(root,)]
  while stack:
    path = stack.pop(0)
    print(path)
    node = path[-1]
    dirs = graph[node]
    add = [tuple(list(path) + [dir]) for dir in dirs]
    stack.extend(add)
# ----------------------------------------------------------------------
def get_paths(iter_):
  """Identify all paths (sequences of keys) from
  any dictionary within the iterable given.

  Use an approach analogous to iterative BFS, keeping a stack.
  A stack is used both to add new paths to explore from the iterable,
  and to enumerate all paths.
  Both stacks grow in the same way.

  By removing the first element of the paths stack, the outer
  key for the iterable is given.

  When encountering a list,
  add the outer path as many time as the length of the list.
  """
  paths = set()
  if isinstance(iter_, dict):
    stack_paths = [(key,) for key in iter_.keys()]
    stack = [iter_[k] for k in iter_]
    paths.update(set(stack_paths))
  else:
    stack_paths = [None] * len(iter_)
    stack = [element for element in iter_]
  # --------------------------------------------------------------------
  while stack:
    local_iter_ = stack.pop(0)
    outer_path  = stack_paths.pop(0)
    if isinstance(local_iter_, dict):
      if outer_path is None:
        outer_path = ()
      local_paths = [tuple(list(outer_path) + [key])\
                     for key in local_iter_.keys()]
      stack_paths.extend(local_paths)
      paths.update(set(stack_paths))
      stack.extend(list(local_iter_.values()))
    elif isinstance(local_iter_, (list, set, tuple)):
      # repeat outer path for the length of the iterable
      local_paths = [outer_path] * len(local_iter_)
      stack_paths.extend(local_paths)
      stack.extend(local_iter_.copy())
  return paths
# ----------------------------------------------------------------------
def query(iter_, path=[]):
  """Return all values of dictionaries within the iterable
  by following the set of keys described by the given path.
  """
  if isinstance(path, tuple):
    path = list(path)
  if not isinstance(path, list):
    raise ValueError("The given path is not a list")
  stack = [iter_]
  stack_paths = [path.copy()]
  while stack:
    local_iter_ = stack.pop(0)
    local_path = stack_paths.pop(0)
    ckey = local_path[0]                # get current key
    if isinstance(local_iter_, dict):
      try:
        new_iters = local_iter_[ckey]
      except KeyError:
        continue # simply ignore this search branch
      if len(local_path[1:]) > 0:
        stack.extend(new_iters)
        stack_paths.extend([local_path[1:]] * len(new_iters))
      else:
        yield new_iters
    elif isinstance(local_iter_, (list, set, tuple)):
      stack.extend([element for element in local_iter_])
      stack_paths.extend([local_path] * len(local_iter_))

if __name__ == "__main__":
  pass
