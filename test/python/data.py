# coding: utf-8 -*- coding: UTF-8 -*-


records = {}

records['project.project'] = [{'code':'BJ16.17','name': '北京地铁16号线17标段'}]

records['project.task'] = [
  {'project_id': 'BJ16.17', 'code': '1',       'name':'某某车站', },
  {'project_id': 'BJ16.17', 'code': '1.1',     'name':'车站附属', },
  {'project_id': 'BJ16.17', 'code': '1.1.1',   'name':'1号风井',  },
  {'project_id': 'BJ16.17', 'code': '1.1.1.1', 'name':'竖井',  'is_leaf': True, 'uom_id': 'm', 'price': 10000,'qty':28.91 },
  {'project_id': 'BJ16.17', 'code': '1.1.2',   'name':'1号横通道', },
  {'project_id': 'BJ16.17', 'code': '1.1.2.1', 'name':'第1层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':59.26 },
  {'project_id': 'BJ16.17', 'code': '1.1.2.2', 'name':'第2层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':59.26 },
  {'project_id': 'BJ16.17', 'code': '1.1.2.3', 'name':'第3层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':59.26 },
  {'project_id': 'BJ16.17', 'code': '1.1.2.4', 'name':'第4层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':59.26 },
  {'project_id': 'BJ16.17', 'code': '1.1.3',   'name':'2号风井',  },
  {'project_id': 'BJ16.17', 'code': '1.1.3.1', 'name':'竖井',  'is_leaf': True, 'uom_id': 'm', 'price': 10000,'qty':30.4 },
  {'project_id': 'BJ16.17', 'code': '1.1.4',   'name':'2号横通道', },
  {'project_id': 'BJ16.17', 'code': '1.1.4.1', 'name':'第1层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':49.4 },
  {'project_id': 'BJ16.17', 'code': '1.1.4.2', 'name':'第2层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':49.4 },
  {'project_id': 'BJ16.17', 'code': '1.1.4.3', 'name':'第3层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':49.4 },
  {'project_id': 'BJ16.17', 'code': '1.1.4.4', 'name':'第4层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':49.4 },
  {'project_id': 'BJ16.17', 'code': '1.2',     'name':'车站主体',  },
  {'project_id': 'BJ16.17', 'code': '1.2.1',  'name':'导洞1',  },
  {'project_id': 'BJ16.17', 'code': '1.2.1.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':95.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.1.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':98.4 },
  {'project_id': 'BJ16.17', 'code': '1.2.1.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':55.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.2',  'name':'导洞2',  },
  {'project_id': 'BJ16.17', 'code': '1.2.2.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':95.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.2.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':98.4 },
  {'project_id': 'BJ16.17', 'code': '1.2.2.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':55.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.3',  'name':'导洞3',  },
  {'project_id': 'BJ16.17', 'code': '1.2.3.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':95.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.3.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':98.4 },
  {'project_id': 'BJ16.17', 'code': '1.2.3.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':55.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.4',  'name':'导洞4',  },
  {'project_id': 'BJ16.17', 'code': '1.2.4.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':95.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.4.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':98.4 },
  {'project_id': 'BJ16.17', 'code': '1.2.4.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':55.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.5',  'name':'导洞5',  },
  {'project_id': 'BJ16.17', 'code': '1.2.5.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':95.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.5.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':98.4 },
  {'project_id': 'BJ16.17', 'code': '1.2.5.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':55.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.6',  'name':'导洞6',  },
  {'project_id': 'BJ16.17', 'code': '1.2.6.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':95.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.6.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':98.4 },
  {'project_id': 'BJ16.17', 'code': '1.2.6.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':55.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.7',  'name':'导洞7',  },
  {'project_id': 'BJ16.17', 'code': '1.2.7.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':95.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.7.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':98.4 },
  {'project_id': 'BJ16.17', 'code': '1.2.7.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':55.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.8',  'name':'导洞8',  },
  {'project_id': 'BJ16.17', 'code': '1.2.8.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':95.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.8.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':98.4 },
  {'project_id': 'BJ16.17', 'code': '1.2.8.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm', 'price': 6000,'qty':55.1 },
  {'project_id': 'BJ16.17', 'code': '1.2.9',    'name':'条基(导洞5)', 'is_leaf': True, 'uom_id': 'm', 'price': 2000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.10',   'name':'条基(导洞8)', 'is_leaf': True, 'uom_id': 'm', 'price': 2000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.11',   'name':'边桩(导洞1)', 'is_leaf': True, 'uom_id': 'Unit(s)', 'price': 3000,'qty':128 },
  {'project_id': 'BJ16.17', 'code': '1.2.12',   'name':'边桩(导洞4)', 'is_leaf': True, 'uom_id': 'Unit(s)', 'price': 3000,'qty':144 },
  {'project_id': 'BJ16.17', 'code': '1.2.13',   'name':'冠梁(导洞1)', 'is_leaf': True, 'uom_id': 'm', 'price': 2000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.14',   'name':'冠梁(导洞4)', 'is_leaf': True, 'uom_id': 'm', 'price': 2000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.15',   'name':'导洞内扣拱及回填(导洞1)', 'is_leaf': True, 'uom_id': 'm', 'price': 1500,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.16',   'name':'导洞内扣拱及回填(导洞4)', 'is_leaf': True, 'uom_id': 'm', 'price': 1500,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.17',   'name':'导洞内二衬及边墙(导洞1)', 'is_leaf': True, 'uom_id': 'm', 'price': 2000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.18',   'name':'导洞内二衬及边墙(导洞4)', 'is_leaf': True, 'uom_id': 'm', 'price': 2000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.18',   'name':'底纵梁(导洞6)', 'is_leaf': True, 'uom_id': 'm', 'price': 3000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.20',   'name':'底纵梁(导洞7)', 'is_leaf': True, 'uom_id': 'm', 'price': 3000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.21',   'name':'钢管柱',  },
  {'project_id': 'BJ16.17', 'code': '1.2.21.1', 'name':'挖孔', 'is_leaf': True, 'uom_id': 'Unit(s)', 'price': 30000,'qty':72 },
  {'project_id': 'BJ16.17', 'code': '1.2.21.2', 'name':'安装', 'is_leaf': True, 'uom_id': 'Unit(s)', 'price': 30000,'qty':72 },
  {'project_id': 'BJ16.17', 'code': '1.2.21.3', 'name':'浇注', 'is_leaf': True, 'uom_id': 'Unit(s)', 'price': 30000,'qty':72 },
  {'project_id': 'BJ16.17', 'code': '1.2.22',   'name':'顶纵梁及中跨二初扣拱',  },
  {'project_id': 'BJ16.17', 'code': '1.2.22.1', 'name':'防水',    'is_leaf': True, 'uom_id': 'm', 'price': 1000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.22.2', 'name':'钢筋安装', 'is_leaf': True, 'uom_id': 'm', 'price': 3000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.22.3', 'name':'支模',    'is_leaf': True, 'uom_id': 'm', 'price': 1000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.22.4', 'name':'浇注',    'is_leaf': True, 'uom_id': 'm', 'price': 1000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.23',   'name':'边跨初支扣拱(导洞I)',  'is_leaf': True, 'uom_id': 'm', 'price': 2000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.24',   'name':'边跨初支扣拱(导洞II)', 'is_leaf': True, 'uom_id': 'm', 'price': 2000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.25',   'name':'边跨二衬扣拱(导洞I)',  'is_leaf': True, 'uom_id': 'm', 'price': 1500,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.26',   'name':'边跨二衬扣拱(导洞II)', 'is_leaf': True, 'uom_id': 'm', 'price': 1500,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.27',   'name':'站厅层土方开挖', 'is_leaf': True, 'uom_id': 'm', 'price': 20000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.28',   'name':'站厅层底板',  },
  {'project_id': 'BJ16.17', 'code': '1.2.28.1', 'name':'支模', 'is_leaf': True, 'uom_id': 'm', 'price': 1000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.28.2', 'name':'钢筋', 'is_leaf': True, 'uom_id': 'm', 'price': 2000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.28.3', 'name':'浇筑', 'is_leaf': True, 'uom_id': 'm', 'price': 3000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.29',   'name':'站厅层侧墙',  },
  {'project_id': 'BJ16.17', 'code': '1.2.29.1', 'name':'防水', 'is_leaf': True, 'uom_id': 'm', 'price': 1000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.29.2', 'name':'钢筋', 'is_leaf': True, 'uom_id': 'm', 'price': 2000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.29.3', 'name':'支模', 'is_leaf': True, 'uom_id': 'm', 'price': 1000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.29.4', 'name':'浇筑', 'is_leaf': True, 'uom_id': 'm', 'price': 3000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.30',   'name':'站台层土方开挖', 'is_leaf': True, 'uom_id': 'm', 'price': 20000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.31',   'name':'格栅封底', 'is_leaf': True, 'uom_id': 'm', 'price': 2000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.32',   'name':'站台层底板',  },
  {'project_id': 'BJ16.17', 'code': '1.2.32.1', 'name':'支模', 'is_leaf': True, 'uom_id': 'm', 'price': 1000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.32.2', 'name':'钢筋', 'is_leaf': True, 'uom_id': 'm', 'price': 2000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.32.3', 'name':'浇筑', 'is_leaf': True, 'uom_id': 'm', 'price': 1000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.33',   'name':'站台层侧墙',  },
  {'project_id': 'BJ16.17', 'code': '1.2.33.1', 'name':'防水', 'is_leaf': True, 'uom_id': 'm', 'price': 1000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.33.2', 'name':'钢筋', 'is_leaf': True, 'uom_id': 'm', 'price': 2000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.33.3', 'name':'支模', 'is_leaf': True, 'uom_id': 'm', 'price': 1000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '1.2.33.4', 'name':'浇筑', 'is_leaf': True, 'uom_id': 'm', 'price': 1000,'qty':256.6 },
  {'project_id': 'BJ16.17', 'code': '2',       'name':'某某区间', },
  {'project_id': 'BJ16.17', 'code': '2.1',     'name':'区间附属', },
  {'project_id': 'BJ16.17', 'code': '2.1.1',   'name':'一号风井', },
  {'project_id': 'BJ16.17', 'code': '2.1.1.1', 'name':'竖井', 'is_leaf': True, 'uom_id': 'm', 'price': 10000,'qty':33.86 },
  {'project_id': 'BJ16.17', 'code': '2.1.2',   'name':'一号横通道', },
  {'project_id': 'BJ16.17', 'code': '2.1.2.1', 'name':'第1层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':36.75 },
  {'project_id': 'BJ16.17', 'code': '2.1.2.2', 'name':'第2层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':36.75 },
  {'project_id': 'BJ16.17', 'code': '2.1.2.3', 'name':'第3层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':36.75 },
  {'project_id': 'BJ16.17', 'code': '2.1.2.4', 'name':'第4层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':36.75 },
  {'project_id': 'BJ16.17', 'code': '2.1.3',   'name':'L1号临时施工竖井', },
  {'project_id': 'BJ16.17', 'code': '2.1.3.1', 'name':'竖井', 'is_leaf': True, 'uom_id': 'm', 'price': 10000,'qty':32.96 },
  {'project_id': 'BJ16.17', 'code': '2.1.4',   'name':'L1号临时施工横通道', },
  {'project_id': 'BJ16.17', 'code': '2.1.4.1', 'name':'第1层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':41.85 },
  {'project_id': 'BJ16.17', 'code': '2.1.4.2', 'name':'第2层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':41.85 },
  {'project_id': 'BJ16.17', 'code': '2.1.4.3', 'name':'第3层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':41.85 },
  {'project_id': 'BJ16.17', 'code': '2.1.4.4', 'name':'第4层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':41.85 },
  {'project_id': 'BJ16.17', 'code': '2.1.5',   'name':'二号风井', },
  {'project_id': 'BJ16.17', 'code': '2.1.5.1', 'name':'竖井', 'is_leaf': True, 'uom_id': 'm', 'price': 10000,'qty':31.98 },
  {'project_id': 'BJ16.17', 'code': '2.1.6',   'name':'二号横通道', },
  {'project_id': 'BJ16.17', 'code': '2.1.6.1', 'name':'第1层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':46.2 },
  {'project_id': 'BJ16.17', 'code': '2.1.6.2', 'name':'第2层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':46.2 },
  {'project_id': 'BJ16.17', 'code': '2.1.6.3', 'name':'第3层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':46.2 },
  {'project_id': 'BJ16.17', 'code': '2.1.6.4', 'name':'第4层', 'is_leaf': True, 'uom_id': 'm', 'price': 8000,'qty':46.2 },
  {'project_id': 'BJ16.17', 'code': '2.2',     'name':'区间正线初支', },
  {'project_id': 'BJ16.17', 'code': '2.2.1',   'name':'左线', },
  {'project_id': 'BJ16.17', 'code': '2.2.1.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':98.98 },
  {'project_id': 'BJ16.17', 'code': '2.2.1.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':330.12 },
  {'project_id': 'BJ16.17', 'code': '2.2.1.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':151.42 },
  {'project_id': 'BJ16.17', 'code': '2.2.1.4', 'name':'分段开挖4', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':107.18 },
  {'project_id': 'BJ16.17', 'code': '2.2.2',   'name':'右线', },
  {'project_id': 'BJ16.17', 'code': '2.2.2.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':98.98 },
  {'project_id': 'BJ16.17', 'code': '2.2.2.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':330.12 },
  {'project_id': 'BJ16.17', 'code': '2.2.2.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':151.42 },
  {'project_id': 'BJ16.17', 'code': '2.2.2.4', 'name':'分段开挖4', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':107.18 },
  {'project_id': 'BJ16.17', 'code': '2.3',     'name':'区间正线二衬', },
  {'project_id': 'BJ16.17', 'code': '2.3.1',   'name':'左线', },
  {'project_id': 'BJ16.17', 'code': '2.3.1.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':98.98 },
  {'project_id': 'BJ16.17', 'code': '2.3.1.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':330.12 },
  {'project_id': 'BJ16.17', 'code': '2.3.1.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':151.42 },
  {'project_id': 'BJ16.17', 'code': '2.3.1.4', 'name':'分段开挖4', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':107.18 },
  {'project_id': 'BJ16.17', 'code': '2.3.2',   'name':'右线', },
  {'project_id': 'BJ16.17', 'code': '2.3.2.1', 'name':'分段开挖1', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':98.98 },
  {'project_id': 'BJ16.17', 'code': '2.3.2.2', 'name':'分段开挖2', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':330.12 },
  {'project_id': 'BJ16.17', 'code': '2.3.2.3', 'name':'分段开挖3', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':151.42 },
  {'project_id': 'BJ16.17', 'code': '2.3.2.4', 'name':'分段开挖4', 'is_leaf': True, 'uom_id': 'm', 'price': 5000,'qty':107.18 },
]


