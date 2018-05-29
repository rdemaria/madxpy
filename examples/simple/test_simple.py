import madxpy

mad=madxpy.Mad()

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




