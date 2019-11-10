class ContactManager:
    wtf = 1

    def test(self):
        self.wtf = 2


manager = ContactManager()

print(manager.wtf)
manager.test()
print(manager.wtf)
