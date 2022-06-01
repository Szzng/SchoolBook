const DjangoBase = 'http://127.0.0.1:8000/'

export default {
  Django_API: `${DjangoBase}api/`,

  /* Setting */
  setting_TabletsPlaces: 'tablets/setting/place/',
  setting_DestroyTabletsPlace: (placeName) => {
    return `tablets/setting/place/${placeName}/`
  },
  setting_ClassroomPlaces: 'rooms/setting/place/',
  setting_DestroyClassroomPlace: (placeName) => {
    return `rooms/setting/place/${placeName}/`
  },
  setting_FixedTimeTable: 'rooms/setting/fixedtimetable/',
  setting_ByPlaceFixedTimeTable: (placeName) => {
    return `rooms/setting/fixedtimetable/${placeName}/`
  },

  /* Book Tablets */
  tabletsAll: 'tablets/',
  tabletsByDate: (place, date) => {
    return `tablets/${place}/${date}/`
  },
  tabletDestroy: (tabletId) => {
    return `tablets/${tabletId}/`
  },
  tabletLeft: (place, date) => {
    return `tablets/left/${place}/${date}/`
  },

  /* Book Room */
  roomAll: 'rooms/',
  roomByDate: (date) => {
    return `rooms/${date}`
  },
  roomDestroy: (roomId) => {
    return `rooms/destroy/${roomId}/`
  }
}
