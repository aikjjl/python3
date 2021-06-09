for a in range(0,1001):
    for b in range(0,1001):
        for c in range(0,1001):
             if a+b+c==1000 and a**2+b**2==c**2:
                print(a,b,c)


shortcuts -- get_client_by_request
    from blueking.component.shortcuts import get_client_by_request
    # 默认从django settings中获取APP认证信息：应用ID和安全密钥
    # 默认从django request中获取用户登录态bk_token
    client = get_client_by_request(request)
    # 参数
    kwargs = {'bk_biz_id': 1}
    result = client.cc.get_app_host_list(kwargs)

shortcuts -- get_client_by_user
    from blueking.component.shortcuts import get_client_by_user
    # 默认从django settings中获取APP认证信息：应用ID和安全密钥
    # 默认从user中获取username，user为User对象或直接为User中username数据
    user = 'username'
    client = get_client_by_user(user)
    # 参数
    kwargs = {'bk_biz_id': 1}
    result = client.cc.get_app_host_list(kwargs)