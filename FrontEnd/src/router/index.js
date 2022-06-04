import Vue from 'vue'
import Router from 'vue-router'

import SettingTabs from '@/components/Setting/SettingTabs.vue'
import SetFixedTimeTable from '@/components/Setting/SetFixedTimeTable.vue'
import SetClassroomPlaces from '@/components/Setting/SetClassroomPlaces.vue'
import ClassroomSettingTabs from '@/components/Setting/ClassroomSettingTabs.vue'

import TabletsTabs from '@/components/Tablets/TabletsTabs.vue'
import TabletsCalendar from '@/components/Tablets/CalendarByPlace.vue'

import ClassRoomCalendar from '@/components/Classroom/CalendarByPlace.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/setting',
      component: SettingTabs,
      props: true,
      children: [
        { path: 'tablets', component: SetClassroomPlaces },
        {
          path: 'classroom',
          component: ClassroomSettingTabs,
          props: true,
          children: [
            { path: 'place', component: SetClassroomPlaces },
            { path: 'fixtimetable', component: SetFixedTimeTable }
          ]
        }
      ]
    },

    {
      path: '/classroom/:place',
      component: ClassRoomCalendar,
      props: true
    },
    {
      path: '/tablets',
      component: TabletsTabs,
      props: true,
      children: [
        { path: ':place', component: TabletsCalendar, props: true }
      ]
    }
  ]
})
