import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Cookies from 'js-cookie'
import { v4 as uuidv4 } from 'uuid'
// import myrest from '@/utils/myrest'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: { title: 'Blog -首页' }
  },
  {
    path: '/comm',
    component: () => import(/* webpackChunkName: "about" */ '../views/My_Test.vue'),
    meta: { title: 'Blog -留言' }
  },
  {
    path: '/visitors',
    component: () => import(/* webpackChunkName: "about" */ '../views/VisitorsView.vue'),
    meta: { title: 'Blog -访客' }
  },
  {
    path: '/404',
    component: () => import(/* webpackChunkName: "about" */ '../views/404.vue'),
    meta: { title: 'Blog -404' }
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/about2',
    name: 'about2',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView2.vue')
  },
  {
    path: '/about3',
    name: 'about3',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView3.vue')
  },
  {
    path: '/about4',
    name: 'about4',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView4.vue')
  }
]

const router = new VueRouter({
  routes,
  mode: 'history',
  base: '/'
})

// 路由守卫？放在路由实例后面
router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title
  }
  // myrest.user_history(to.path) // 记录用户访问地址 传到后端 废弃咯 后端根据nginx报头记录
  if (!Cookies.get('user_uuid')) {
    Cookies.set('user_uuid', uuidv4())
  }
  router.app.$store.state.global_route = to.path // 顶部导航栏 下面的蓝杠渲染
  const { resolved } = router.resolve(to.path)
  if (resolved.matched.length) {
    next()
  } else {
    next('/404') // 如果 to.path 没有匹配的路由，跳转到404页面
  }
})

router.onError((error) => {
  // 代码来自于其他人的解决方案，只改了一下正则
  const pattern = /Loading chunk .* failed/g
  const isChunkLoadFailed = error.message.match(pattern)
  if (isChunkLoadFailed) {
    location.reload()
  }
})

export default router
