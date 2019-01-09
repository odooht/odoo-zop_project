# coding: utf-8 -*- coding: UTF-8 -*-


records = {}

records['project.project'] = [{'code':'BJ16.17','name': '北京地铁16号线17标段'}]

records['project.task'] = [
  {'project_id': 'BJ16.17', 'code': '1',       'name':'某某车站', },
  {'project_id': 'BJ16.17', 'code': '1.1',     'name':'车站附属', },
  {'project_id': 'BJ16.17', 'code': '1.1.1',   'name':'1号风井',  },
  {'project_id': 'BJ16.17', 'code': '1.1.1.1', 'name':'竖井',  'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.1.2',   'name':'1号横通道', },
  {'project_id': 'BJ16.17', 'code': '1.1.2.1', 'name':'第1层', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.1.2.2', 'name':'第2层', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.1.2.3', 'name':'第3层', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.1.2.4', 'name':'第4层', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.1.3',   'name':'2号风井',  },
  {'project_id': 'BJ16.17', 'code': '1.1.3.1', 'name':'竖井',  'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.1.4',   'name':'2号横通道', },
  {'project_id': 'BJ16.17', 'code': '1.1.4.1', 'name':'第1层', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.1.4.2', 'name':'第2层', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.1.4.3', 'name':'第3层', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.1.4.4', 'name':'第4层', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2',     'name':'车站主体',  },
  {'project_id': 'BJ16.17', 'code': '1.2.1',  'name':'导洞1',  },
  {'project_id': 'BJ16.17', 'code': '1.2.2',  'name':'导洞2',  },
  {'project_id': 'BJ16.17', 'code': '1.2.3',  'name':'导洞3',  },
  {'project_id': 'BJ16.17', 'code': '1.2.4',  'name':'导洞4',  },
  {'project_id': 'BJ16.17', 'code': '1.2.5',  'name':'导洞5',  },
  {'project_id': 'BJ16.17', 'code': '1.2.6',  'name':'导洞6',  },
  {'project_id': 'BJ16.17', 'code': '1.2.7',  'name':'导洞7',  },
  {'project_id': 'BJ16.17', 'code': '1.2.8',  'name':'导洞8',  },
  {'project_id': 'BJ16.17', 'code': '1.2.1.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.1.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.1.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.2.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.2.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.2.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.3.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.3.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.3.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.4.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.4.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.4.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.5.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.5.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.5.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.6.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.6.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.6.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.7.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.7.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.7.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.8.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.8.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.8.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.9',    'name':'条基(导洞5)', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.10',   'name':'条基(导洞8)', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.11',   'name':'边桩(导洞1)', 'is_leaf': True, 'uom_id': 'Unit(s)' },
  {'project_id': 'BJ16.17', 'code': '1.2.12',   'name':'边桩(导洞4)', 'is_leaf': True, 'uom_id': 'Unit(s)' },
  {'project_id': 'BJ16.17', 'code': '1.2.13',   'name':'冠梁(导洞1)', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.14',   'name':'冠梁(导洞4)', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.15',   'name':'导洞内扣拱及回填(导洞1)', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.16',   'name':'导洞内扣拱及回填(导洞4)', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.17',   'name':'导洞内二衬及边墙(导洞1)', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.18',   'name':'导洞内二衬及边墙(导洞4)', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.18',   'name':'底纵梁(导洞6)', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.20',   'name':'底纵梁(导洞7)', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.21',   'name':'钢管柱',  },
  {'project_id': 'BJ16.17', 'code': '1.2.21.1', 'name':'挖孔', 'is_leaf': True, 'uom_id': 'Unit(s)' },
  {'project_id': 'BJ16.17', 'code': '1.2.21.2', 'name':'安装', 'is_leaf': True, 'uom_id': 'Unit(s)' },
  {'project_id': 'BJ16.17', 'code': '1.2.21.3', 'name':'浇注', 'is_leaf': True, 'uom_id': 'Unit(s)' },
  {'project_id': 'BJ16.17', 'code': '1.2.22',   'name':'顶纵梁及中跨二初扣拱',  },
  {'project_id': 'BJ16.17', 'code': '1.2.22.1', 'name':'防水',    'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.22.2', 'name':'钢筋安装', 'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.22.3', 'name':'支模',    'is_leaf': True, 'uom_id': 'm' },
  {'project_id': 'BJ16.17', 'code': '1.2.22.4', 'name':'浇注',    'is_leaf': True, 'uom_id': 'm' },

  
  {'project_id': 'BJ16.17', 'code': '2',    'name':'某某区间', },
  
]
