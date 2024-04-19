from .__core import YYJinterface


class ChatYYJ(YYJinterface):
    def __init__(self) -> None:
        super().__init__()

        self.__emoji = '\U0001F613'
        self.__describe = '瓦达西瓦YYJ得思，俺是一个来自D7 415的梗小鬼，俺打球像坤坤，俺打王者只会压力己方MVP，天天被狙击仔克制'

        return
    
    def joker(self) -> None:
        print('俺长这样：')
        print(self.__emoji)

        return
    

def main() -> None:
    raise RuntimeError('你无不无聊啊花心思来调这个脚本，菜就多练。')


if __name__ == '__main__':
    main()