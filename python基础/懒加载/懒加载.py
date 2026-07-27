class Client:

    def __getattr__(self, name):
        print("第一次加载", name)

        obj = object()

        setattr(self, name, obj)

        return obj

c = Client()

c.mysql
c.mysql