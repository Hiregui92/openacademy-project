import functools
import xmlrpclib


HOST = 'localhost'
PORT = 8069
DB = 'odoo_curso'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)
model = 'openacademy.session'
# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print "Logged in as %s (uid:%d)" % (USER, uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# 2. Read the sessions
sessions = call(model, 'search_read', [], ['name', 'seats'])
for session in sessions:
    print "Session %s (%s seats)" % (session['name'], session['seats'])

# 3.create a new session for the "Functional" course
course_ids = call('openacademy.course', 'search', [
                  ('name', 'ilike', 'Functional')])

if len(course_ids) > 0 and course_ids[0] > 0:
    session_id = call(model, 'create', {
        'name': 'My session',
        'course_id': course_ids[0],
    })
else:
    print "There is no course with that name"
