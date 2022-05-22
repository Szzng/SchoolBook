import Vue from 'vue'
import Router from 'vue-router'
import TabletCalendar from '@/components/Tablets/Calendar.vue'
import RoomCalendar from '@/components/Rooms/Calendar.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    { path: '/tablets', component: TabletCalendar },
    { path: '/computerRoom', component: RoomCalendar }
  ]
})
