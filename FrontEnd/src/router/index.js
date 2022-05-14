import Vue from 'vue'
import Router from 'vue-router'
// import TabletsCalendar from '@/components/Tablets/TabletCalendar.vue'
import TabletCalendar from '@/components/Tablets/TabletCalendar.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    { path: '/tablets', component: TabletCalendar }
    // { path: '/computerrooms', component: TabletCalendar }
    // {
    //   path: '/tablets',
    //   component: TabletsCalendar,
    //   props: true,
    //   children: [
    //     {
    //       path: ':code',
    //       name: 'NewsList',
    //       props: true,
    //       component: () => import('@/components/RisingStock/NewsList.vue')
    //     }
    //   ]
    // }
  ]
})
