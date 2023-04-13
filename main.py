class Phone:
    number = "088543678"

    def change_number(self, new_number) -> None:
        self.number = new_number

    _counter = 0

    def take_call(self, _counter) -> None:
        self._counter += 1
        print("Звонок принят")

    def summ_call(self, take_call) -> None:
        return take_call(self)


xiaomi = Phone()
samsung = Phone()
iphone = Phone()


xiaomi.change_number("023486659")
samsung.change_number("065379078")
iphone.change_number("056587675")

xiaomi.take_call(2)
samsung.take_call(10)
iphone.take_call(5)

phones = [xiaomi, samsung, iphone]


def all_calls(phones) -> int:
    return sum(phones.take_call() for i in phones)


