class UnitTest:
    import inspect

    @classmethod
    def call(cls):
        instance = cls()
        methods = cls.inspect.getmembers(instance, predicate=cls.inspect.ismethod)
        tests = [name for name, method in methods if name.startswith("test_")]

        # executa todos os testes
        for test in tests:
            getattr(instance, test)()
            print(".", end="")
        print("\n\nTodos os testes passaram!")

    def _assert(self, truthy):
        if not truthy:
            raise Exception("Asserção falhou.")
