import datetime


class Log():
    # 输出日志
    @staticmethod
    def echo(msg, type = 'info'):
        msg = "["+str(datetime.datetime.now())+"] "+type+" "+msg;
        if type == "error":
            print(f"\033[1;31m" + msg + "\033[0m")
        elif type == "warn":
            print(f"\033[33m"+msg+"\033[0m")
        elif type == "success":
            print(f"\033[32m"+msg+"\033[39m")
        else:
            print(f"\033[30m"+msg+"\033[30m")
