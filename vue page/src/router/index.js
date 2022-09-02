import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)


export default new Router({
  routes: [
    {
      path: '/',//推荐收集方法
      component:() => import('@/components/pages/Home Page')
    },
    {
      path: '/Collection Choice',//方法或工具选择
      component:() => import('@/components/pages/Collection Choice')
    },
    {
      path: '/Recommended collection method',//推荐收集方法
      component:() => import('@/components/pages/Recommended collection method')
    },
    {
      path: '/Recommended collection method tool',//推荐收集方法
      component:() => import('@/components/pages/Recommended collection method tool')
    },
    {
      path: '/Recommended collection method tool func',//推荐收集方法
      component:() => import('@/components/pages/Recommended collection method tool func')
    },
    {
      path: '/Recommended vulnerability scanning methods',//推荐漏洞扫描方法
      component: () => import('@/components/pages/Recommended vulnerability scanning methods')
    },
    {
      path: '/Recommended vulnerability scanning methods tool',//推荐漏洞扫描方法
      component: () => import('@/components/pages/Recommended vulnerability scanning methods tool')
    },
    {
      path: '/VulnerabilityscanTool',//推荐漏洞工具
      component: () => import('@/components/pages/VulnerabilityscanTool')
    },
    {
      path: '/Recommended penetration steps',//渗透步骤推荐
      component: () => import ('@/components/pages/Recommended penetration steps')
    },
    {
      path: '/Recommended penetration steps func',//渗透步骤推荐1
      component: () => import ('@/components/pages/Recommended penetration steps func')
    },
    {
      path: '/TestStep',//渗透步骤推荐1
      component: () => import ('@/components/pages/TestStep')
    },
    {
      path: '/HMZR',//后门植入
      component: () => import ('@/components/pages/HMZR')
    },
    {
      path: '/HMZR func',//后门植入
      component: () => import ('@/components/pages/HMZR func')
    },
    {
      path: '/TestHMZR',//后门植入
      component: () => import ('@/components/pages/TestHMZR')
    },

    {
      path: '/Trace removal recommendations', //痕迹清除推荐
      component: () => import('@/components/pages/Trace removal recommendations')
    },
    {
      path: '/Trace removal recommendations func', //痕迹清除推荐1
      component: () => import('@/components/pages/Trace removal recommendations func')
    },
    {
      path: '/RemovalRecommendations', //痕迹清除推荐2
      component: () => import('@/components/pages/RemovalRecommendations')
    },
    {
      path: '/GetInformation', //信息收集工具
      component: () => import('@/components/pages/GetInformation')
    },
    {
      path: '/GetInformationTool', //信息收集工具
      component: () => import('@/components/pages/GetInformationTool')
    },
    {
      path: '/All information display',//所有信息展示
      component: () => import('@/components/pages/All information display')
    } , 
    {
      path: '/Privilege promotion', //权限提升
      component: () => import('@/components/pages/Privilege promotion')
    },
    {
      path: '/Privilege promotion func', //权限提升
      component: () => import('@/components/pages/Privilege promotion func')
    },
  ]
})
