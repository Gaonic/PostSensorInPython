import pycurl
import cStringIO
 
buf = cStringIO.StringIO()
 
c = pycurl.Curl()
c.setopt(c.URL, 'https://osp.gaonic.com/create_sensor')
c.setopt(c.POSTFIELDS, 'name=PythonTest&mac_add=00:03:6a:11:ff:00&latitude=32.1670&longitude=34.8367&sensor[Water Quality]=10')
#c.setopt(c.VERBOSE, True)
c.setopt(c.WRITEFUNCTION, buf.write)
c.perform()
 
print buf.getvalue()
buf.close()
