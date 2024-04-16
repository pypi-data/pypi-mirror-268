class Helper():
    """
    从一个数组中获取一个key的值
    """
    @staticmethod
    def arrKey(arr, key, default=None):
        try:
            return arr[key]
        except Exception as e:
            return default

