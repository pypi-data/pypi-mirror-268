# EasyID
___

## Installation

`
pip install easy_id
`

---

## Basic Usage

```python
from easy_id import *

if __name__ == "__main__":
    generator = EasyID(EasyIdType.NANOID)
    print(generator.generate())

```

---

## Advanced Usage

```python
from easy_id import *

config = {
    "epoch": 1543392060,
    "machine_id": 0,
}

if __name__ == "__main__":
    generator = EasyID(EasyIdType.SNOWFLAKE, config)
    print(generator.generate())
```

