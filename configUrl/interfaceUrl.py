'''



这个地方封装的接口地址信息


'''
ip='http://192.168.83.42'


def interfaceUrl1():
    #查询用户行为轨迹
    url=ip+"/api/scrm/rest/customer/behavior/trace/list"
    return url

def interfaceUrl2():
    #导出客户管理列表
    url=ip+"/api/scrm/common/customer/export"
    return url


def interfaceUrl3():
    #添加跟进记录
    url=ip+"/api/scrm/rest/customer/follow/record/"
    return url



def interfaceUrl4():
    #查询跟进记录
    url=ip+"/api/scrm/rest/customer/follow/record/list"
    return url


def interfaceUrl5():
    #修改跟进记录
    url=ip+"/api/scrm/rest/customer/follow/record/"
    return url


def interfaceUrl6():
    #删除记录
    url=ip+"/api/scrm/rest/customer/follow/record/"
    return url


def interfaceUrl7():
    #查询所有客户阶段
    url=ip+"/api/scrm/rest/customer/follow/state/all"
    return url


def interfaceUrl8():
    #查询客户阶段详情列表
    url=ip+"/api/scrm/rest/customer/follow/state/list"
    return url


def interfaceUrl9():
    #删除客户阶段
    url=ip+"/api/scrm/rest/customer/follow/state/"
    return url

def interfaceUrl10():
    #删除客户阶段
    url=ip+"/api/scrm/rest/customer/follow/state/"
    return url

def interfaceUrl11():
    #新增阶段
    url=ip+"/api/scrm/rest/customer/follow/state/"
    return url

def interfaceUrl12():
    #编辑客户阶段
    url=ip+"/api/scrm/rest/customer/follow/state/"
    return url

def interfaceUrl13():
    #添加提醒员工
    url=ip+"/api/scrm/rest/customer/follow/state/member/remind"
    return url

def interfaceUrl14():
    #分页查询客户管理列表
    url=ip+"/api/scrm/rest/customer/page"
    return url

def interfaceUrl15():
    #查询客户列表
    url=ip+"/api/scrm/rest/customer/list"
    return url

def interfaceUrl16():
    #设置客户状态
    url=ip+"/api/scrm/rest/customer/state"
    return url

def interfaceUrl17():
    #根据id查询客户详细信息
    url=ip+"/api/scrm/rest/customer/details"
    return url

def interfaceUrl18():
    #根据客户姓名、员工、客户标签查询
    url=ip+"/api/scrm/rest/customer/condition"
    return url

def interfaceUrl19():
    #批量设置客户状态
    url=ip+"/api/scrm/rest/customer/"
    return url

def interfaceUrl20():
    #转移客户
    url=ip+"/api/scrm/rest/customer/trans"
    return url

def interfaceUrl21():
    #刷新客户数据
    url=ip+"/api/scrm/rest/customer/reload"
    return url

def interfaceUrl22():
    #根据外部联系人ID获取客户信息
    url=ip+"/api/scrm/rest/customer/list/byexternaluserid"
    return url

def interfaceUrl23():
    #通过员工ID获取员工当天已添加客户数
    url=ip+"/api/scrm/rest/customer/added/customer/number"
    return url

def interfaceUrl24():
    #根据租户查询客户公海
    url=ip+"/api/scrm/rest/customer/international/waters/"
    return url

def interfaceUrl25():
    #分页条件查询
    url=ip+"/api/scrm/rest/customer/international/waters/page"
    return url

def interfaceUrl26():
    #新增公海
    url=ip+"/api/scrm/rest/customer/international/waters/"
    return url

def interfaceUrl27():
    #修改公海
    url=ip+"/api/scrm/rest/customer/international/waters/"
    return url

def interfaceUrl28():
    #删除客户公海
    url=ip+"/api/scrm/rest/customer/international/waters/{id}"
    return url

def interfaceUrl29():
    #给用户打标签
    url=ip+"/api/scrm/rest/customer/label/relation/"
    return url

def interfaceUrl30():
    #删除客户与标签之
    url=ip+"/api/scrm/rest/customer/label/relation/"
    return url

def interfaceUrl31():
    #添加待办事项
    url=ip+"/api/scrm/rest/customer/todo/"
    return url

def interfaceUrl32():
    #查询记录
    url=ip+"/api/scrm/rest/customer/todo/list"
    return url

def interfaceUrl33():
    #查询记录
    url=ip+"/api/scrm/rest/customer/todo/"
    return url

def interfaceUrl34():
    #修改记录
    url=ip+"/api/scrm/rest/customer/todo/state"
    return url

def interfaceUrl35():
    #修改状态
    url=ip+"/api/scrm/rest/customer/todo/state"
    return url

def interfaceUrl36():
    #删除
    url=ip+"/api/scrm/rest/customer/todo/"
    return url

def interfaceUrl37():
    #查询今日待办事项
    url=ip+"/api/scrm/rest/customer/todo/today"
    return url

def interfaceUrl38():
    #查询全部待办事项
    url=ip+"/api/scrm/rest/customer/todo/all"
    return url

def interfaceUrl39():
    #处理待办
    url=ip+"/api/scrm/rest/customer/todo/setstate"
    return url

def interfaceUrl40():
    #公海客户列表查询
    url=ip+"/api/scrm/rest/customer/international/list"
    return url

def interfaceUrl41():
    #公海客户分页,条件查询
    url=ip+"/api/scrm/rest/customer/international/page"
    return url

def interfaceUrl42():
    #添加公海用户
    url=ip+"/api/scrm/rest/customer/international/save"
    return url

def interfaceUrl43():
    #导入excel公海用户  自动回收: 清空员工id 自动提醒 给员工发消息,客户还有多久回收至公海
    url=ip+"/api/scrm/rest/customer/international/import"
    return url

def interfaceUrl44():
    #下载模板
    url=ip+"/api/scrm/rest/customer/international/download-templates"
    return url

def interfaceUrl45():
    #对客户公海的客户进行打标签
    url=ip+"/api/scrm/rest/customer/international/labeling"
    return url

def interfaceUrl46():
    #删除客户公海的客户标签
    url=ip+"/api/scrm/rest/customer/international/remove-label"
    return url

def interfaceUrl47():
    #将一些客户移动到其他公海
    url=ip+"/api/scrm/rest/customer/international/move-other-waters"
    return url

def interfaceUrl48():
    #将一些客户批量分配给其他员工
    url=ip+"/api/scrm/rest/customer/international/bulk-allocation"
    return url

def interfaceUrl49():
    #批量删除公海客户
    url=ip+"/api/scrm/rest/customer/international/del-clues"
    return url

def interfaceUrl50():
    #分页查询微信线索
    url=ip+"/api/scrm/rest/customer/wechat/clue/page"
    return url

def interfaceUrl51():
    #公共客户下拉
    url=ip+"/api/scrm/tool/customer/select/list"
    return url

def interfaceUrl52():
    #客户阶段公共下拉
    url=ip+"/api/scrm/tool/customer/select/followstage/list"
    return url

def interfaceUrl53():
    #通知提醒
    url=ip+"/api/scrm/rest/enterpriseriskcontrol/del/log/"
    return url

def interfaceUrl54():
    #通知提醒详情
    url=ip+"/api/scrm/rest/enterpriseriskcontrol/del/log/rule"
    return url

def interfaceUrl55():
    #列表分页
    url=ip+"/api/scrm/rest/enterpriseriskcontrol/del/log/list"
    return url

def interfaceUrl56():
    #通知提醒
    url=ip+"/api/scrm/rest/enterpriseriskcontrol/ramind/log/"
    return url

def interfaceUrl57():
    #通知提醒详情
    url=ip+"/api/scrm/rest/enterpriseriskcontrol/ramind/log/rule"
    return url

def interfaceUrl58():
    #列表分页
    url=ip+"/api/scrm/rest/enterpriseriskcontrol/ramind/log/list"
    return url

def interfaceUrl59():
    #新增活码
    url=ip+"/api/scrm/rest/expandcustomer/channel/activecode/"
    return url

def interfaceUrl60():
    #修改活码
    url=ip+"/api/scrm/rest/expandcustomer/channel/activecode/"
    return url

def interfaceUrl61():
    #根据ID删除渠道活码
    url=ip+"/api/scrm/rest/expandcustomer/channel/activecode/{id}"
    return url

def interfaceUrl62():
    #分页
    url=ip+"/api/scrm/rest/expandcustomer/channel/activecode/page"
    return url

def interfaceUrl63():
    #获取详情
    url=ip+"/api/scrm/rest/expandcustomer/channel/activecode/{id}"
    return url

def interfaceUrl64():
    #获取编辑页面详情
    url=ip+"/api/scrm/rest/expandcustomer/channel/activecode/edit/{id}"
    return url

def interfaceUrl65():
    #通过ID查询数据统计
    url=ip+"/api/scrm/rest/expandcustomer/channel/activecode/total/{id}"
    return url

def interfaceUrl66():
    #通过ID与时间查询统计图
    url=ip+"/api/scrm/rest/expandcustomer/channel/activecode/chart/{id}"
    return url

def interfaceUrl67():
    #通过ID与时间查询统计图  ！！！！！！！文档不存在
    url=""
    print("！！！！！！！接口文档不存在")
    return url

def interfaceUrl68():
    #智能名片查询接口
    url=ip+"/api/scrm/common/card/detail"

    return url

def interfaceUrl69():
    #获取智能名片信息
    url=ip+"/api/scrm/rest/expandcustomer/scrm/intellect/card/"

    return url

def interfaceUrl70():
    #修改智能名片信息
    url=ip+"/api/scrm/rest/expandcustomer/scrm/intellect/card/"

    return url


def interfaceUrl71():
    #新增一客一码
    url=ip+"/api/scrm/rest/expandcustomer/code/"

    return url

def interfaceUrl72():
    #分页查询一客一码
    url=ip+"/api/scrm/rest/expandcustomer/code/list"

    return url

def interfaceUrl73():
    #分页查询邀请客户详情
    url=ip+"/api/scrm/rest/expandcustomer/code/log/list"

    return url

def interfaceUrl74():
    #根据客户id查询一客一码详情
    url=ip+"/api/scrm/rest/expandcustomer/code/query"

    return url

def interfaceUrl75():
    #新增一客一码使用情况
    url=ip+"/api/scrm/rest/expandcustomer/code/log/"

    return url

def interfaceUrl76():
    #分页条件查询
    url=ip+"/api/scrm/rest/expandcustomer/intellect/card/member/list"

    return url

def interfaceUrl77():
    #开通名片
    url=ip+"/api/scrm/rest/expandcustomer/intellect/card/member/"

    return url

def interfaceUrl78():
    #启用或者禁用名片
    url=ip+"/api/scrm/rest/expandcustomer/intellect/card/member/"

    return url

def interfaceUrl79():
    #自动拉群分页查询
    url=ip+"/api/scrm/rest/group/auto/joingroup/page"

    return url

def interfaceUrl80():
    #根据主键删除自动拉群任务
    url=ip+"/api/scrm/rest/group/auto/joingroup/{id}"

    return url

def interfaceUrl81():
    #获取自动拉群详情
    url=ip+"/api/scrm/rest/group/auto/joingroup/{id}"

    return url

def interfaceUrl82():
    #新增自动拉群
    url=ip+"/api/scrm/rest/group/auto/joingroup/"

    return url

def interfaceUrl83():
    #根据条件查询群聊列表
    url=ip+"/api/scrm/rest/group/groupchat/list"

    return url

def interfaceUrl84():
    #客群添加SOP规则
    url=ip+"/api/scrm/rest/group/add/sop"

    return url


def interfaceUrl85():
    #分页查询客群列表
    url=ip+"/api/scrm/rest/group/list"

    return url


def interfaceUrl86():
    #查询客群详情-统计图
    url=ip+"/api/scrm/rest/group/statistical/chart"

    return url



