const roomStore = {
  namespaced: true,
  state: {
    dialog: {
      updateRoom: false,
      destroyRoom: false,
      updateTimetable: false,
      createTimetable: false,

      checkRoomBooking: false,
      bookRoom: false,
      destroyRoomBooking: false
    },
    periods: [1, 2, 3, 4, 5, 6],
    places: [],
    focusDate: '',
    focusPlace: '',
    bookedRoomLists: [],
    availableBookingEvents: [],
    colors: ['red', 'indigo', 'deep-purple', 'pink', 'orange', 'green'],
    timetable: {
      0: ['', '', '', '', '', ''],
      1: ['', '', '', '', '', ''],
      2: ['', '', '', '', '', ''],
      3: ['', '', '', '', '', ''],
      4: ['', '', '', '', '', '']
    }
  },
  mutations: {
    focusDateSetter (state, date) {
      state.focusDate = date
    },
    focusPlaceSetter (state, place) {
      state.focusPlace = place
    }
  },
  actions: {
  }
}

export default roomStore
