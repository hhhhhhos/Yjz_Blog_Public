import myrest from '@/utils/myrest'

export function api1 (vuethis, data = {}) {
  return myrest.rest_test({
    // 发送评论到数据库
    vuethis,
    url: '/send/comments',
    method: 'post',
    data
  })
}

export function api2 (vuethis, params) {
  return myrest.rest_test({
    // 获取当前页评论
    vuethis,
    url: '/table/info',
    method: 'get',
    params
  })
}

export function api3 (vuethis, params) {
  return myrest.rest_test({
    // 获取当前页ip历史记录
    vuethis,
    url: '/iphistory/info',
    method: 'get',
    params
  })
}

export function api4 (vuethis, params) {
  return myrest.rest_test({
    // 获取当前评论id子评论
    vuethis,
    url: '/subcomment/info',
    method: 'get',
    params
  })
}

export function api5 (vuethis, data, className) {
  return myrest.rest_test({
    // 获取table信息和数量
    vuethis,
    url: '/table/' + className + '/info',
    method: 'post',
    data
  })
}

export function api6 (vuethis, modelName, typeName) {
  return myrest.rest_test({
    // 获取models的types数量
    vuethis,
    url: '/models/' + modelName + '/types/' + typeName,
    method: 'get'
  })
}

export function api7 (vuethis, data, params) {
  return myrest.rest_test({
    // 给名为modelname的表新增data信息 modelname包含在params参数里
    vuethis,
    url: 'send',
    method: 'post',
    data,
    params
  })
}

export function api8 (vuethis, modelName, typeName, params) {
  return myrest.rest_test({
    // 获取models的types数量 带params参数
    vuethis,
    url: '/models/' + modelName + '/types/' + typeName,
    method: 'get',
    params
  })
}
