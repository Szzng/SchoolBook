import Vue from 'vue'
import Router from 'vue-router'
import BackGround from '@/components/Tablets/BackGround.vue'
import CalendarByPlace from '@/components/Tablets/CalendarByPlace.vue'
import RoomCalendar from '@/components/Rooms/Calendar.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    { path: '/computerRoom', component: RoomCalendar },
    {
      path: '/tablets',
      component: BackGround,
      props: true,
      children: [
        { path: ':place', component: CalendarByPlace, props: true }
      ]
    }
  ]
})
