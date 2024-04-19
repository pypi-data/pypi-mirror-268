class YYJinterface(object):
    def __init__(self) -> None:
        pass

    def __call__(self):
        pass

    def __str__(self) -> str:
        pass

    def joker(self) -> None:
        pass

class YYJ(YYJinterface):
    def __init__(self) -> None:
        self.__emoji = '\U0001F613'
        self.__describe = '瓦达西瓦YYJ得思，俺是一个来自D7 415的梗小鬼，俺打球像坤坤，俺打王者只会压力己方MVP，天天被狙击仔克制'

        return
    
    def __call__(self) -> None:
        raise RuntimeError('不是这么玩儿的，试一下print打印')
    
    def __str__(self) -> str:
        raise TypeError(self.__describe + '\n虽然但是，还是给好厚米抛个错，自己捕获去')
    
    def joker(self) -> None:
        print('俺长这样：')
        print(self.__emoji)

        return
    
    @staticmethod
    def joker() -> None:
        print('俺长这样：')
        print('\U0001F613')

        return
    

def main() -> None:
    yyj = YYJ()
    yyj.joker()

    try:
        print(yyj)
    except:
        print('没你事儿了，一边凉快去。')

    return


if __name__ == '__main__':
    main()







