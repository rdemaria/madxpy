import madxpy

mad=madxpy.Mad()


mad.command('call',file="job.madx")


mad.get_table_double('twiss','betx',4)
mad.get_table_double('twiss','s',104)
mad.get_table_string('twiss','name',9)

betx=mad.get_column_double('twiss','betx')
name=mad.get_column_string('twiss','name')

