# coding: utf-8 -*- coding: UTF-8 -*-

from rpc import get_user, execute
from data import records


def project_one():
    rec =records['project.project'][0]
    domain = [('code','=',rec['code'])]
    game_id = find('project.project', domain, record=rec  )
    
    return game_id

def search_one(model, domain):
    ids = execute(usid, model, 'search', domain, limit=1)
    return ids and ids[0] or None

def find(model, domain, record=None ):
    ids = execute(usid, model, 'search', domain, limit=1)
    print 'find',model, domain, record, ids

    if not ids:
        id = execute(usid, model, 'create', record )
        print 'create, id=',model, id
        return id
    
    id = ids[0]
    print 'write, id=',model, id
    execute(usid, model, 'write', id, record )
    return id


def work2_one(rec):
    rec = rec.copy()
    rec['project_id'] = project_id

    uom = rec.get('uom_id')
    if uom:
        uom_id = search_one('uom.uom', [('name','=',uom  )])
        rec['uom_id'] = uom_id
    
    model = 'project.work'
    domain = [('code','=',rec['code']),('project_id','=',project_id) ]
    id = find(model, domain, record=rec )
    print id
    if id:
        #print execute(usid, model, 'read', id)
        pass


def work2_one_parent(rec):
    rec = rec.copy()
    rec['project_id'] = project_id
    ss = rec['code'].split('.')
    
    pcode = '.'.join(ss[0:-1])
    
    nrec = {}
    
    if pcode:
        uom_id = search_one('project.work', [('code','=',pcode),('project_id','=',project_id) ])
        nrec['parent_id'] = uom_id
    
    #print pcode, rec['code'],nrec
    model = 'project.work'
    domain = [('code','=',rec['code']),('project_id','=',project_id) ]
    id = find(model, domain, record=nrec )
    print id
    if id:
        #print execute(usid, model, 'read', id)
        pass


def work2_multi():
    for rec in records['project.work']:
        work2_one(rec)

def work2_multi_parent():
    for rec in records['project.work']:
        work2_one_parent(rec)



def work3_one_fname(rec):
    nrec = {'set_full_name':1 }
    model = 'project.work'
    domain = [('code','=',rec['code']),('project_id','=',project_id) ]
    id = find(model, domain, record=nrec )
    print id
    if id:
        #print execute(usid, model, 'read', id)
        pass

def work3_fname():
    for rec in records['project.work']:
        work3_one_fname(rec)
    
def work3_one_amount(rec):
    nrec = {  'set_amount':1}
    model = 'project.work'
    domain = [('code','=',rec['code']),('project_id','=',project_id) ]
    id = find(model, domain, record=nrec )
    print id
    if id:
        #print execute(usid, model, 'read', id)
        pass


def work3_amount():
    for rec in records['project.work']:
        work3_one_amount(rec)


def date_one(rec):
    model = 'olap.dim.date'
    domain = [('date','=',rec['date']) ]
    id = find(model, domain, record=rec )
    print id
    if id:
        #print execute(usid, model, 'read', id)
        pass

def date_multi():
    for rec in records['olap.dim.date']:
        date_one(rec)


def worksheet_one(rec):
    rec = rec.copy()
    domain = [('code','=',rec['work_id']),('project_id','=',project_id) ]
    work_id = search_one('project.work', domain )
    rec['work_id'] = work_id
    
    model = 'project.worksheet'
    domain = [('date','=',rec['date']),('number','=',rec['number']),('work_id','=',work_id) ]
    id = find(model, domain, record=rec )
    print id
    if id:
        #print execute(usid, model, 'read', id)
        pass

def worksheet_multi():
    for rec in records['project.worksheet']:
        worksheet_one(rec)

def worksheet_one_fname(rec):
    nrec = {'set_name':1 }
    domain = [('code','=',rec['work_id']),('project_id','=',project_id) ]
    work_id = search_one('project.work', domain )
    print 'fname,search work', domain, work_id
    if not work_id:
        print 'error'
        
    model = 'project.worksheet'
    domain = [('date','=',rec['date']),('number','=',rec['number']),('work_id','=',work_id) ]
    
    id = find(model, domain, record=nrec )
    print id
    if id:
        #print execute(usid, model, 'read', id)
        pass

def worksheet_one_post(rec):
    nrec = {'post':1 }
    domain = [('code','=',rec['work_id']),('project_id','=',project_id) ]
    work_id = search_one('project.work', domain )
    
    model = 'project.worksheet'
    domain = [('date','=',rec['date']),('number','=',rec['number']),('work_id','=',work_id) ]
    
    id = find(model, domain, record=nrec )
    print id
    if id:
        #print execute(usid, model, 'read', id)
        pass

def worksheet_fname():
    for rec in records['project.worksheet']:
        worksheet_one_fname(rec)
    
def worksheet_post():
    for rec in records['project.worksheet']:
        worksheet_one_post(rec)
    


usid, uid = get_user()
print usid, uid

project_id = project_one()

""" 
work2_multi()
work2_multi_parent()
work3_fname()
work3_amount()

date_multi()
worksheet_multi()
worksheet_fname()

"""
print 'create worksheet'
worksheet_multi()
print 'name worksheet'
worksheet_fname()
worksheet_post()

""" 
wsids = execute(usid, 'project.worksheet', 'search', [] )

if wsids:
    id = wsids[0]
    print execute(usid, 'project.worksheet', 'read', id,['name','date'] )
    print execute(usid, 'project.worksheet', 'write', id,{'date':'2019-1-1'} )
    print execute(usid, 'project.worksheet', 'read', id,['name','date'] )
"""