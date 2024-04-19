======
Coppyr
======

Coppyr (Copp-**er**) is a collecton of useful Python boilerplate that I find
myself reusing frequently between projects.

- subp_
- singleton_
   - Singleton_
   - Namespace_
- Context_
- lazyproperty_
- CoppyrError_


subp
----

``subp.call``
  Convenience wrapper around ``subprocess.run`` that abstracts many of the
  common options and features (such as ``subprocess.PIPE`` passing).

  ::
 
    >>> from coppyr import subp
    >>> retcode, stdout, stederr = subp.call("lsb_release -a")
    >>> print retcode
    0
    >>> print stdout
    ['Distributor ID:\tUbuntu', 'Description:\tUbuntu 18.04.3 LTS',
    'Release:\t18.04', 'Codename:\tbionic', '']
    >>> print stderr
    ['No LSB modules are available.', '']

  *Note*: ``STDOUT`` and ``STDERR`` are returned as ``List`` objects with each
  line as a ``String``.  This includes empty lines which become empty strings.


singleton
---------

.. _Singleton:

``singleton.Singleton``
  Base object that implements the Singleton pattern pythonically.  Future inits
  of this object will return previously the first created object.

  ::

    >>> from coppyr.types import Singleton
    >>> first = Singleton()
    >>> first
    <singleton.Singleton object at 0x7fa72df4cd30>
    >>> second = Singleton()
    >>> second
    <singleton.Singleton object at 0x7fa72df4cd30>

  This object can be used as a base class or mixin to add Singleton behavior to
  custom objects.

  **Warning:**  When inheriting from Singleton it is neccessary to override the
  ``_instance`` class attribute to ensure that you don't inadvertantly store your
  subclass instance in the parent class variable
  (``types.Singleton._instance``).  For the same reason, you should also
  override ``_init`` as well.

  ::

    class MySingletonClass(Singleton):
        _instance = None
        _init = False

.. _Namespace:

``singleton.Namespace``
  Simple Singleton object that stores KV pairs.

  ::

    >>> from coppyr.singleton import Namespace
    >>> ns = Namespace()
    >>> ns.foo = "bar"
    >>> ns.foo
    'bar'
    >>> ns2 = Namespace()
    >>> ns2.foo
    'bar'

  Returns ``None`` if the key is not in the namespace.

  ::

    >>> ns.baz
    >>>

  **Warning:** Just like ``Singleton``, child objects should override the
  class ``_instance`` and ``_init`` attributes.

  __getattr__(self, attr)

    When an attribute does not exist, a ``Namespace`` will return ``None``
    instead of raising an ``AttributeError``.


Context
-------

``Context``
  This is intended as an interpreter local object that can store common state
  between executing threads/coroutines.  It's a convenient tool to provide
  access to shared utilities such as logging, environment information, and
  other shared utilities for an application.

  ::

    >>> from coppyr import Context
    >>> context = Context()
    >>> context.action_id
    '15_100000'
    >>> context.inc_action_id()
    >>> context.action_id
    '15_100001'


lazyproperty
------------

``lazyproperty``
  This is a decorator that will turn a class method into a property that is
  evaluated once.  This is a useful performance optimization for class elements
  that require computation but do not change overtime.

  ::

    >>> from coppyr import lazyproperty
    >>> class Foo:
    ...     def __init__(self):
    ...         self.a = 5
    ...         self.b = 6
    ...
    ...     @lazyproperty
    ...     def c(self):
    ...         return self.a + self.b
    ...
    >>> x = Foo()
    >>> x.c
    11
    >>> x.a = 6
    >>> x.c
    11  # c remains 11


CoppyrError
-----------

``CoppyrError``
  Simple boilerplate for readable, consistent, custom error messages.  Adds a
  `dict` representation that can be used for easy(ish) conversion to JSON for
  web use cases.

  ::

    >>> from coppyr import CoppyrError
    >>> class MyError(CoppyrError):
    ...     description = "Doom 2: Hell on earth."
    ... 
    >>> err = MyError()
    >>> raise err
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    __main__.MyError: Doom 2: Hell on earth.
    >>> err
    MyError(message=Doom 2: Hell on earth., payload={})
    >>> err.to_dict()
    {'error': 'MyError', 'message': 'Doom 2: Hell on earth.', 'payload': {}}
 
