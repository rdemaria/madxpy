from cffi import FFI
ffi = FFI()

ffi.cdef("""
void mad_init(int argc, char *argv[]);
void mad_fini(void);
double  get_variable_(const char* name);
void    set_variable_(const char* name, double* value);
void    pro_input_(char* statement);

int     table_exists(const char* table);
int     table_column_exists(const char* table, const char* name);
int     table_cell_exists(const char* table, const char* name, const int*     row);
int     double_from_table_row(const char* table, const char* name, const int* row, double* val);
int     string_from_table_row(const char* table, const char* name, const int* row, char* string);

""")

mad=ffi.dlopen('../build/libs/madx/libmadx-linux64-gnu.so')

mad.mad_init(0,ffi.new("char[]", ""))
mad.pro_input_(ffi.new("char[]","a=3;"))
mad.pro_input_(ffi.new("char[]","value,a;"))
mad.get_variable_("a")









