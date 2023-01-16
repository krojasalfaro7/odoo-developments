try:
    from xmlrpc import client as xmlrpclib
except ImportError:
    import xmlrpclib

common = xmlrpclib.ServerProxy('http://localhost:8070/xmlrpc/common')
print(common.version())
uid = common.authenticate("bd", "admin", "1dbb326e7f50c9e4c230b4dc67e7d480e793c096", {})

print("RESPUESTA", uid)
