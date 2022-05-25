import Vue from 'vue'
import Router from 'vue-router'

import TabletsBackGround from '@/components/Tablets/BackGround.vue'
import TabletsCalendar from '@/components/Tablets/CalendarByPlace.vue'

import ClassroomBackGround from '@/components/Classroom/BackGround.vue'
import ClassRoomCalendar from '@/components/Classroom/CalendarByPlace.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/classroom/computer',
      component: ClassroomBackGround,
      props: true,
      children: [
        { path: ':place', component: ClassRoomCalendar, props: true }
      ]
    },
    {
      path: '/tablets',
      component: TabletsBackGround,
      props: true,
      children: [
        { path: ':place', component: TabletsCalendar, props: true }
      ]
    }
  ]
})
