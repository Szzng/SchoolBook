import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/General/Home.vue'

import SettingTabs from '@/components/Setting/SettingTabs.vue'
import SetRoom from '@/components/Setting/SetRoom.vue'
import SetTool from '@/components/Setting/SetTool.vue'

import ToolTabs from '@/components/Tool/ToolTabs.vue'
import ToolCalendar from '@/components/Tool/ToolCalendar.vue'

import RoomTabs from '@/components/Room/RoomTabs.vue'
import RoomCalendar from '@/components/Room/RoomCalendar.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      children: [
        { path: ':code', component: Home }
      ]
    },
    {
      path: '/:code/setting',
      name: 'setting',
      component: SettingTabs,
      children: [
        { path: 'tool', name: 'settingTool', component: SetTool },
        { path: 'room', name: 'settingRoom', component: SetRoom }
      ]
    },

    {
      path: '/:code/tool',
      name: 'tools',
      component: ToolTabs,
      children: [
        { path: ':tool', name: 'tool', component: ToolCalendar }
      ]
    },

    {
      path: '/:code/room',
      name: 'rooms',
      component: RoomTabs,
      children: [
        { path: ':room', name: 'room', component: RoomCalendar }
      ]
    }

  ]
})
