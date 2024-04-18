from itertools import chain
from random import shuffle
from threading import Condition, Lock
from typing import Iterable


class Resource:
    usage: int

    def __init__(self, resource):
        self.resource = resource
        self.usage = 0

    def __lt__(self, other):
        return self.usage.__lt__(other.usage)


class ResourceLoan:
    def __init__(self, balancer, instance):
        self._lock = Lock()
        self._balancer = balancer
        self._instance = instance

    def __enter__(self):
        return self._instance.resource

    def release(self):
        with self._lock:
            if self._balancer:
                self._balancer._release(self._instance)
                self._balancer = None

    def __exit__(self, type, value, traceback):
        self.release()


class ResourceBalancer:
    def __init__(self):
        self._active = list()
        self._ghosts = list()
        self._condition = Condition()

    def _available(self):
        return next(iter(self._active), None)

    def usage_min(self) -> int:
        """Returns the usage-level for the least used resource"""
        return min((r.usage for r in self._active), default=0)

    def wait_for_change(self, value_fn, prev, timeout=None):
        def predicate():
            new_value = value_fn()
            if new_value != prev:
                return (new_value,)
            else:
                return None

        with self._condition:
            maybe_new = self._condition.wait_for(predicate=predicate, timeout=timeout)
            if maybe_new:
                return maybe_new[0]
            else:
                return prev

    def active_count(self):
        return len(self._active)

    def acquire(self) -> ResourceLoan:
        with self._condition:
            winner = self._condition.wait_for(self._available)
            winner.usage += 1
            self._active.sort()
            return ResourceLoan(self, winner)

    def _release(self, instance):
        with self._condition:
            instance.usage -= 1
            self._active.sort()
            self._condition.notify_all()

    def provision(self, resources: Iterable[object]):
        with self._condition:
            new_resources = set(resources)

            active, ghosts = self._active, self._ghosts
            self._ghosts = []
            self._active = []

            for instance in chain(active, ghosts):
                try:
                    new_resources.remove(instance.resource)
                    self._active.append(instance)
                except KeyError:
                    if instance.usage > 0:
                        self._ghosts.append(instance)

            for new_resource in new_resources:
                self._active.append(Resource(new_resource))

            shuffle(self._active)
            self._active.sort()
            self._condition.notify_all()
