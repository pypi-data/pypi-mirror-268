from functools import partial  # 锁定参数
import subprocess

# 防止乱码
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs


from functools import partial  # 锁定参数
import subprocess

# 防止乱码
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs


def js_read(file=None, code=None, encoding="utf-8"):
    """
    :param code:需要添加在文件开头  javascript 代码  示例 code = "var a = 10;\n"
    :param file: 需要手动添加文件路径，或者javascript的代码格式(function fn(){return xxx;};
    有条件判断增加相应的条件判断，或者循环)
    :param mode: 只读模式
    :param encoding: 默认utf-8
    """
    try:
        # 读取javascript 代码
        with open(file, mode="r", encoding=encoding) as f:
            if code:
                js_code = code + f.read()
            else:
                js_code = f.read()
            # 加载 javascript 代码
        js = execjs.compile(js_code)
    except:
        # 做一个适配同时兼容 javascript 代码 不用读出javascript代码文件
        if code:
            js = execjs.compile(f"{code}{file}")
        else:
            js = execjs.compile(file)
    return js




