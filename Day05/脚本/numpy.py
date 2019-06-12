import json
import numpy as np


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    # 字典类型中有中文编码
    dict = {'id': 1, 'title': b'\xe7\xac\xac\xe4\xb8\x80\xe7\xab\xa0 \xe7\xa7\xa6\xe7\xbe\xbd'}
    # 转Json对象
    #dict = json.dumps(dict, cls=MyEncoder, ensure_ascii=False, indent=4)
    # 转字典类型
    #dict = json.loads(dict)
    print(dict)
