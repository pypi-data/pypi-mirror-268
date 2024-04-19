# **CheeseSignal**

一款简单的信号系统。

## **安装**

系统要求：Linux。

Python要求：目前仅保证支持3.11及以上版本的Python，新版本会优先支持Python的最新稳定版本。

```
pip install CheeseSignal
```

## **使用**

使用方式较为简单，通过函数或装饰件连接至某个信号，随后等待信号发送。

```python
import time

from CheeseSignal import signal

signal = Signal()

def receiver1(*args, **kwargs):
    print(arg, kwargs)
signal.connect(receiver1)

@signal.connect()
def receiver2(*args, **kwargs):
    return args, kwargs

while True:
    print(signal.send('Hello', 'World', {
        'Cheese': 'Signal'
    }))
    time.sleep(1)
```

## **接口文档**

### **`class Signal`**

```python
from CheeseSignal import Signal

signal = Signal()
```

#### **`self.receivers: List[Receiver]`**

【只读】 接收器的列表，按注册顺序排序。

#### **`self.total_send_num: int`**

【只读】 总计信号发送次数。

#### **`def connect(self, fn: Callable, *, expected_receive_num: int = 0, auto_remove: bool = False)`**

通过函数注册响应函数。

- **参数**

    - `expected_receive_num`: 期望接受信号的次数，超过该次数则不再响应信号；0为无限次。

    - `auto_remove`: 是否自动删除响应次数超出期望次数的接收器。

- **报错**

    - `ValueError`: 已有重复的函数接收器。

#### **`def connect(self, *, expected_receive_num: int = 0, auto_remove: bool = False)`**

通过装饰器注册响应函数。

- **参数**

    - `expected_receive_num`: 期望接受信号的次数，超过该次数则不再响应信号；0为无限次。

    - `auto_remove`: 是否自动删除响应次数超出期望次数的接收器。

- **报错**

    - `ValueError`: 已有重复的函数接收器。

#### **`def send(self, *args, **kwargs) -> List[Any]`**

发送信号。

#### **`async def async_send(self, *args, **kwargs) -> List[Any]`**

在协程环境中发送信号，并请保证所有接收函数都是协程函数。

```python
import asyncio

from CheeseSignal import Signal

async def run_asyncio():
    signal = Signal()
    await signal.async_send('data1', 'data2', **{
        'key1': 'value1',
        'key2': 'value2'
    })

asyncio.run(run_asyncio())
```

#### **`def disconnect(self, fn: Callable)`**

断开接收器。

```python
from CheeseSignal import Signal

def receiver(*args, **kwargs):
    ...

signal = Signal()
signal.connect(receiver)
signal.disconnect(receiver)
```

- **报错**

    - `ValueError`: 未找到该函数的接收器。

#### **`def reset(self)`**

重置统计数据；所有的接收器的统计数据也会同步清空。

#### **`def disconnect_all(self)`**

断开所有接收器。

#### **`def get_receiver(self, fn: Callable) -> Receiver`**

获取接收器。

```python
from CheeseSignal import Signal

def receiver(*args, **kwargs):
    ...

signal = Signal()
signal.connect(receiver)

print(signal.get_receiver(receiver))
```

- **报错**

    - `ValueError`: 未找到该函数的接收器。

#### **`def index(self, fn: Callable) -> index`**

获取接收器的顺序位置。

```python
from CheeseSignal import Signal

def receiver(*args, **kwargs):
    ...

signal = Signal()
signal.connect(receiver)

print(signal.index(receiver))
```

- **报错**

    - `ValueError`: 未找到该函数的接收器。

### **`class Receiver`**

正常使用并不需要手动创建该类。

```python
from CheeseSignal import Receiver
```

#### **`def __init__(self, fn: Callable, *, expected_receive_num: int, auto_remove: bool)`**

- **参数**

    - `expected_receive_num`: 期望接受信号的次数，超过该次数则不再响应信号；0为无限次。

    - `auto_remove`: 是否自动删除响应次数超出期望次数的接收器。

#### **`self.expected_receive_num: int`**

期望接受信号的次数，超过该次数则不再响应信号；0为无限次。

#### **`self.auto_remove: bool`**

是否自动删除响应次数超出期望次数的接收器。

#### **`self.total_receive_num: int`**

【只读】 总计信号接受次数。

#### **`self.remaining_receive_num: int`**

【只读】 剩余的期望信号接受次数；返回为-1代表无期望信号接受次数。

#### **`self.receivable: bool`**

【只读】 当前Receiver是否处于可接收信号状态。

#### **`self.unreceivable: bool`**

【只读】 当前Receiver是否处于不可接收信号状态。

#### **`def reset(self)`**

重统计置数据。

在有期望信号接受次数的情况下，`auto_remove is False`的接收器会重新开始计数并接收信号。
