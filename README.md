
## 模型

model|中文名字|note
-----|-------|----
project.project|项目|独立的项目
project.work|工程|树状结构的进度管理点
project.worksheet|工单|工程进度清单
project.workfact|汇总报表|时间/工程两个维度上的数据汇总
olap.dim.date|时间维度|时间维度定义


model|field|String|type|note
-----|-----|------|----|----
project.project|name|名称|Char|
project.project|code|编码|Char|
project.project|date_start|Start Date|Date|
project.project|start|Expiration Date|Date|
project.project|user_id|项目经理|Many2one|res.users
project.project|partner_id|客户|Many2one|res.partner
project.project|constructor_id|建设单位|Many2one|res.partner
project.project|supervisor_id|监理单位|Many2one|res.partner
project.project|designer_id|设计单位|Many2one|res.partner
project.project|consultor_id|咨询单位|Many2one|res.partner

model|field|String|type|note
-----|-----|------|----|----
project.work|name|名称|Char|
project.work|code|编码|Char|
project.work|full_name|名称|Char|
project.work|project_id|项目|Many2one|project.project
project.work|partner_id|客户|Many2one|res.partner
project.work|parent_id|父工程|Many2one|project.work
project.work|child_ids|子工程|One2many|project.work
project.work|work_type|工程类型|Selection|('group','组合工程'),<br>('node','末端节点工程'),<br>('item','施工类目'),
project.work|uom_id|度量单位|Many2one|uom.uom
project.work|qty|设计数量|Float|组合工程,数量为1
project.work|price|单价|Float|仅末端节点,才可以设置单价
project.work|amount|设计产值|Float|计算列. 对于非末端节点,计算自下级节点的汇总<br>对于末端节点,计算自数量和单价
project.work|worksheet_ids|工单|One2many|project.worksheet,work_id

model|field|String|type|note
-----|-----|------|----|----
project.worksheet|work_id|工程|Many2one|project.work<br>仅末端节点工程
project.worksheet|date|日期|Date|工单日期
project.worksheet|number|编码|Char|同一日期内的序号
project.worksheet|sequence|排序号|Char|仅做排序用
project.worksheet|name|名称|Char|
project.worksheet|full_name|名称|Char|
project.worksheet|code|编码|Char|
project.worksheet|project_id|项目|Many2one|project.project
project.worksheet|uom_id|度量单位|Many2one|uom.uom
project.worksheet|price|单价|Float|
project.worksheet|qty|施工数量|Float|
project.worksheet|state|状态|Selection|('draft', '草稿'),<br>('post', '已过账'),<br>('done', '结束'),<br>('cancel', '取消'),



model|function|args|return|note
-----|--------|------|----|----
project.worksheet|post||None|api.multi,<br>将工单信息汇总到报表
project.worksheet|write|{'post':1}|Boolean|api.multi,<br>相当于post函数


model|field|String|type|note
-----|-----|------|----|----
project.workfact|work_id|工程|Many2one|project.work
project.workfact|date_id|日期维度|Many2one|olap.dim.date
project.workfact|date_type|日期维度类型|Selection|('day','日'),<br>('week','周'),<br>('month','月'),<br>('quarter','季'),<br>('year','年'),
project.workfact|date|日期|Date|日期
project.workfact|name|名称|Char|
project.workfact|full_name|名称|Char|
project.workfact|project_id|项目|Many2one|project.project
project.workfact|uom_id|度量单位|Many2one|uom.uom
project.workfact|price|单价|Float|
project.workfact|work_type|工程类型|Selection|参考project.work模型
project.workfact|qty|设计数量|Float|
project.workfact|amount|设计产值|Float|
project.workfact|worksheet_ids|包含的工单|Many2many|project.worksheet,
project.workfact|last_workfact_id|期初值来自于|Many2one|project.workfact
project.workfact|qty_open|期初数量|Float|work_type=node,<br>来自于last_workfact_id.qty_close;<br>work_type=group,该值无效
project.workfact|qty_delta|本期数量|Float|work_type=node,<br>每日汇总自worksheet_ids,<br>每周月汇总自日;<br>work_type=group,该值无效
project.workfact|qty_close|期末数量|Float|期初+本期=期末
project.workfact|amount_open|期初产值|Float|work_type=node,<br>计算自qty_open*price;<br>work_type=group,汇总自下级工程
project.workfact|amount_delta|本期产值|Float|work_type=node,<br>计算自qty_delta*price;<br>work_type=group,汇总自下级工程
project.workfact|amount_close|期末产值|Float|期初+本期=期末
project.workfact|rate|期末完成率|Float|累计完成产值 / 设计产值

model|field|String|type|note
-----|-----|------|----|----
olap.dim.date|date|日期|Date|
olap.dim.date|daykey|日|Integer|yyyymmdd
olap.dim.date|weekkey|周|Integer|yyyyww
olap.dim.date|monthkey|月|Integer|yyyymm
olap.dim.date|quarterkey|季|Integer|yyyy0q
olap.dim.date|year|年|Integer|yyyy
olap.dim.date|day|日|Integer|本月内的日序号
olap.dim.date|week|周|Integer|本年的周序号
olap.dim.date|month|月|Integer|本年的月序号
olap.dim.date|quarter|季|Integer|本年的季序号

model|function|args|return|note
-----|--------|------|----|----
olap.dim.date|get_by_key|date_type,key|id|api.multi,<br>根据key值查找对应的id
olap.dim.date|get_childs|date_type, parent|ids|api.multi,<br>根据parent,查找包含哪些“日”
