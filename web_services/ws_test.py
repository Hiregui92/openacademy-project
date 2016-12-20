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

# 3. Create a new session for the "Functional" course
course_ids = call('openacademy.course', 'search', [
                  ('name', 'ilike', 'Functional')])
course_id = 0
if len(course_ids) > 0 and course_ids[0] > 0:
    course_id = course_ids[0]
    session_id = call(model, 'create', {
        'name': 'My session',
        'course_id': course_id,
    })
else:
    print "There is no course with that name"

# 4. Responsible
responsible_ids = call('res.partner', 'search', [('name', '=', 'Vauxoo')])
if len(responsible_ids) > 0 and responsible_ids[0] > 0 and course_id > 0:
    responsible_id = responsible_ids[0]
    new_session_id = call(model, 'create', {
        'name': 'My session + RESPONSIBLE',
        'instructor_id': responsible_id,
        'course_id': course_id,
        # 'attendee_ids': [(4, responsible_id)],
        'attendee_ids': [(4, 7), (4, 3)]
    })
else:
    print "no se puede =("
