import madxpy

mad=madxpy.Mad()

mad.input("a=3;")
mad.input("value,a;")
mad.set_variable("a",234.)
mad.input("value,a;")
mad.get_variable("a")




