from repoze.lru import LRUCache
import RUtils.singleton
import RUtils.config


class RMemorySessionStore(RUtils.singleton.Singleton):
    def __init__(self):
        if hasattr(self, '_init'):
            return
        self._init = True
        self.config = RUtils.config.RConfig()
        self._cache = LRUCache(self.config.session_cache_size)

    def push(self, token_id, data):
        self._cache.put(token_id, data)

    def get(self, token):
        return self._cache.get(token, None)

    def remove(self, session_id):
        try:
            self._cache.put(session_id, None)
        except KeyError:
            pass

    def contains(self, session_id):
        return self._cache.get(session_id) is not None
