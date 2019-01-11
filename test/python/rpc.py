# coding: utf-8 -*- coding: UTF-8 -*-


import requests
import json

HOST = 'http://192.168.56.105:8069'
SERVER = 'TT'
    
HOST = 'http://192.168.56.103:8069'
SERVER = 'T_project'

URI_LOGIN = HOST + '/json/user/login'
URI_LOGOUT = HOST + '/web/session/destroy'
URI_API       = HOST + '/json/api'


def ret(r):
    print 'status_code:', r.status_code
    print 'raw:', r.raw.read()
    print 'content:', r.content
    #print 'text:', r.text
    print 'headers:', r.headers

def t1(host=HOST):
    headers = {"content-type": "application/json" ,"credentials": "include"  }
    uri = host + '/json/test1'
    params = {}
    data = {}
    rspd = requests.post(uri,params=params,
                      data=json.dumps(data),
                      headers=headers)
                      
    ret(rspd)

print('t1')
#t1()

def jsonrpc(uri, data=None, params=None, sid=None, client=None):
        headers = {"content-type": "application/json"  }
        data1 = {"jsonrpc":"2.0",
                "method":"call",
                "id":123,
                "params":data and data or {}
                }
        
        params1 = params and params.copy() or {}
        if sid:                      
            params1.update( {'session_id':sid} )

        
        if not client:
            client=requests
        
        rspd = client.post(uri,params=params1,
                          data=json.dumps(data1),
                          headers=headers)
        #print rspd
        #ret(rspd)
        
        content = json.loads(rspd.content)
        res = content.get('result',{})
        
        error = content.get('error',{})
        if error:
            print uri, data, sid
            print error
            
            
            return None

        return json.loads(rspd.content).get('result',{})
        

def execute(sid, model, method, *args, **kwargs ):
    return jsonrpc(URI_API,{'model':model, 'method': method, 'args': args, 'kwargs': kwargs},sid=sid )

api = execute
        
class UserSudo(object):
    def login(self,user,psw,db=SERVER):
        """  check ok uid
        """
        result = jsonrpc(URI_LOGIN, {'db': db,'login':user, 'password':psw, 'type':'account'} )
        #result = jsonrpc(URI_LOGIN, {'db': db,'login':user, 'password':psw } )
        
        return result
        #return result.get('sid',None)

    def logout(self):
        return jsonrpc(URI_LOGOUT, {} )

    def register(self,user,psw, db=SERVER):
        """  sudo(), create(), uid
        """
        return jsonrpc(URI_REGISTER, {'db': db,'login':user, 'password':psw} )

    def reset_password(self, user,newpsw, db=SERVER):
        """  sudo(), write(), uid
        """
        return jsonrpc(URI_RESET_PASSWORD, {'db': db,'login':user, 'password':newpsw} )


def get_user():
    print('usid')
    result = UserSudo().login('admin','123')
    
    print result
    
    usid = result.get('sid',None)
    print(usid)

    uid = result.get('uid',None)
    print(uid, type(uid) )

    #UserSudo().logout()


    return usid, uid

if __name__ == '__main__':
    HOST = 'http://192.168.56.105:8069'
    SERVER = 'TT'
    HOST = 'http://192.168.56.103:8069'
    SERVER = 'T_project'

    #url = HOST + '/web/session/authenticate'
    url = HOST + '/json/user/login'

    user = 'admin'
    psw = '123'
    result = jsonrpc(url, {'db': SERVER,'login':user, 'password':psw } )

    print 'login:',result
    
    sid = result.get('session_id')
    print 'sid:',sid

    url = HOST + '/json/api'
    ptn = jsonrpc(url,{'model':'res.partner', 'method': 'search', 'args': [[]], 'kwargs': {}},sid=sid )
    print ptn
    
    
    url = HOST + '/web/session/modules'
    ptn = jsonrpc(url,{},sid=sid )
    print 'modules:',ptn
    
    
    
