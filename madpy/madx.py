"""
make libmadx-linux64-gnu
libs/madx/../../build/libs/madx/libmadx-linux64-gnu.so
void    pro_input(char* statement);
double  get_variable(const char* name);
void    set_variable(const char* name, double* value);

int     table_exists(const char* table);
int     table_column_exists(const char* table, const char* name);
int     table_cell_exists(const char* table, const char* name, const int*     row);

int     double_from_table_row(const char* table, const char* name, const int* row, double* val);
int     string_from_table_row(const char* table, const char* name, const int* row, char* string);


"""

import os
import ctypes as ct


class expr(object):
    def __init__(self,expr):
        self.expr=expr

def _mklist(args):
   out=[]
   for k,v in args.items():
       if isisntance(v,expr):
           out.append(f"{k}:={v!r}")
       else:
           out.append(f"{k}={v!r}")
   out=','.join(out)
   out=out.replace('[','{').replace(']','}')
   return out


_mod_path=os.path.dirname(os.path.abspath(__file__))
_mad_path=os.path.join(_mod_path,"libmadx-linux64-gnu.so")

class Mad(object):
    def __init__(self,mad_path=_mad_path):
        lib=ct.CDLL(mad_path)
        lib.mad_init(0,"")
        lib.mad_init.argtypes=[ct.c_int,ct.c_char_p]
        lib.pro_input_.argtypes=[ct.c_char_p]
        lib.get_variable_.argtypes=[ct.c_char_p]
        lib.get_variable_.restype=ct.c_double
        lib.set_variable_.argtypes=[ct.c_char_p,ct.c_double*1]
        self.lib=lib
    def input(self,command):
        self.lib.pro_input_(command.encode())
    def __del__(self):
        return  self.lib.mad_fini()
    def get_variable(self,name):
        return self.lib.get_variable_(name.encode())
    def set_variable(self,name,value):
        value=(ct.c_double*1)(value)
        return self.lib.set_variable_(name.encode(),value)
    def command(self,name,**args):
        cmd="{},{};".format(name,_mklist(args))
        self.input(cmd)
    def element(self,label,command,**args):
        cmd="{}:{},{};".format(label,command,_mklist(args))
        self.input(cmd)


mad=Mad()
mad.input("a=3;")
mad.input("value,a;")
mad.set_variable("a",234.)
mad.input("value,a;")
mad.get_variable("a")



