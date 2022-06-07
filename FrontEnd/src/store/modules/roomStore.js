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
    rooms: [],
    booking: {},
    focusDate: '',
    focusRoom: '',
    roomBookingLists: [],
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
    focusRoomSetter (state, room) {
      state.focusRoom = room
    },
    bookingSetter (state, booking) {
      state.booking = booking
    }
  },
  actions: {
  }
}

export default roomStore
