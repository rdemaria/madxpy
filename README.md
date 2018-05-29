# madxpy
A madx wrapper



## Install

Install the python package

```bash
pip install madxpy
```

Build the madx shared library object

```
git clone  https://github.com/MethodicalAcceleratorDesign/MAD-X.git
cd MAD-X
make libmadx-linux64-gnu
cp build/libs/madx/libmadx-linux64-gnu.so SOMEWHERE/madxpy/madxpy/
cd ..
```

## Usage

```python
import madxpy

mad=madxpy.Mad("MAD-X/libs/madx/libmadx-linux64-gnu.so")

mad.input("a=3;")
mad.input("value,a;")
mad.set_variable("a",234.)
mad.input("value,a;")
mad.get_variable("a")

mad.command('create',table="tab",column=['a','b','c'])
mad.input('write,table=tab;')
mad.set_variable("b",2);
mad.set_variable("c",5);
mad.input('fill,table=tab;')
mad.get_table_double('tab','a',1)
mad.get_table_double('tab','b',1)
mad.get_table_double('tab','c',1)
```


