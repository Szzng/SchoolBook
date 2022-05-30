import Vue from 'vue'
import Router from 'vue-router'

import SettingBackGround from '@/components/Setting/SettingBackGround.vue'
import SetFixedTimeTable from '@/components/Setting/SetFixedTimeTable.vue'
import SetClassroomPlaces from '@/components/Setting/SetClassroomPlaces.vue'
import ClassroomSettingTabs from '@/components/Setting/ClassroomSettingTabs.vue'

import TabletsBackGround from '@/components/Tablets/BackGround.vue'
import TabletsCalendar from '@/components/Tablets/CalendarByPlace.vue'

import ClassroomBackGround from '@/components/Classroom/BackGround.vue'
import ClassRoomCalendar from '@/components/Classroom/CalendarByPlace.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/setting',
      component: SettingBackGround,
      props: true,
      children: [
        { path: '/tablets', component: SetClassroomPlaces },
        {
          path: '/classroom',
          component: ClassroomSettingTabs,
          props: true,
          children: [
            { path: '/place', component: SetClassroomPlaces },
            { path: '/fixtimetable', component: SetFixedTimeTable }
          ] }
      ]
    },

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
