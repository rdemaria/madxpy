"""
make libmadx-linux64-gnu
libs/madx/../../build/libs/madx/libmadx-linux64-gnu.so
void    pro_input(char* statement);
double  get_variable(const char* name);
void    set_variable(const char* name, double* value);


int     double_from_table_row(const char* table, const char* name, const int* row, double* val);
int     string_from_table_row(const char* table, const char* name, const int* row, char* string);

TODO:
int     table_exists(const char* table);
int     table_column_exists(const char* table, const char* name);
int     table_cell_exists(const char* table, const char* name, const int*     row);
"""

import os
import ctypes as ct

_int = ct.c_int
_double = ct.c_double

_char_p = ct.c_char_p
_double_p = ct.POINTER(ct.c_double)
_int_p = ct.POINTER(ct.c_int)

_double1 = ct.c_double*1
_int1 = ct.c_int*1
_char50 = ct.c_char*15


class expr(object):
    def __init__(self, expr):
        self.expr = expr


def _mklist(args):
   out = []
   for k, v in args.items():
       if isinstance(v, expr):
           out.append(f"{k}:={v!r}")
       else:
           out.append(f"{k}={v!r}")
   out = ','.join(out)
   out = out.replace('[', '{').replace(']', '}')
   return out


_mod_path = os.path.dirname(os.path.abspath(__file__))
_mad_path = os.path.join(_mod_path, "libmadx-linux64-gnu.so")


class Mad(object):
    def __init__(self, mad_path=_mad_path):
        lib = ct.CDLL(mad_path)
        lib.mad_init(0, "")
        lib.mad_init.argtypes = [_int, _char_p]
        lib.pro_input_.argtypes = [_char_p]
        lib.get_variable_.argtypes = [_char_p]
        lib.get_variable_.restype = _double
        lib.set_variable_.argtypes = [_char_p, _double_p]
        lib.double_from_table_row_.argtypes = [_char_p, _char_p, _int_p, _double_p]
        lib.string_from_table_row_.argtypes = [_char_p, _char_p, _int_p, _char_p]
        self.lib= lib
    def input(self, command):
        self.lib.pro_input_(command.encode())
    def __del__(self):
        return self.lib.mad_fini()
    def get_variable(self, name):
        return self.lib.get_variable_(name.encode())
    def set_variable(self, name, value):
        value= _double(value)
        self.lib.set_variable_(name.encode(), value)
    def set_expression(self, name, expr):
        self.input(f"{name}:={expr};")
    def command(self, name, **args):
        cmd = "{},{};".format(name, _mklist(args))
        self.input(cmd)
    def element(self, label, command, **args):
        cmd= "{}:{},{};".format(label, command, _mklist(args))
        self.input(cmd)
    def get_table_double(self,table,column,row):
        value=_double()
        row=_int(row)
        self.lib.double_from_table_row_(table.encode(),column.encode(),row,value)
        return value.value
    def get_table_string(self,table,column,row):
        value=_char50()
        row=_int(row)
        self.lib.string_from_table_row_(table.encode(),column.encode(),row,value)
        return value.value.decode()

