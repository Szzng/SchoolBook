const roomStore = {
  namespaced: true,
  state: {
    dialog: {
      checkRoomBooking: false,
      bookRoom: false,
      destroyRoomBooking: false
    },
    periods: [1, 2, 3, 4, 5, 6],
    bookedRoomLists: []
  },
  mutations: {
  },
  actions: {
  }
}

export default roomStore
