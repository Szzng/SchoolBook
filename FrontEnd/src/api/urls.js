const DjangoBase = 'http://127.0.0.1:8000/'

export default {
  Django_API: `${DjangoBase}api/`,

  /* Setting */
  settingTabletsPlaces: '',
  settingClassroomPlaces: '',
  settingFixedTimeTable: '',

  /* Book Tablets */
  tabletsAll: 'tablets/',
  tabletsByDate: (place, date) => {
    return `tablets/${place}/${date}/`
  },
  tabletDestroy: (tabletId) => {
    return `tablets/${tabletId}/`
  },
  tabletLeft: (place, date) => {
    return `tablets/left/${place}/${date}`
  },

  /* Book Room */
  roomAll: 'rooms/',
  roomByDate: (date) => {
    return `rooms/${date}`
  },
  roomDestroy: (roomId) => {
    return `rooms/destroy/${roomId}`
  }
}
