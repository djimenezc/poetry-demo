from poetry_demo.utils import hi_there


class Demo:

    @staticmethod
    def hello_world(name):
        print(f'hello ${name}')

    @staticmethod
    def hi_there():
        return hi_there()


def main():
    print("debug")
    return "Hello World"


if __name__ == '__main__':
    main()

