const bookStore = {
  namespaced: true,
  state: {
    dialog: {
      checkTabletsBooking: false,
      checkComputerRoomsBooking: false,
      bookTablets: false,
      bookComputerRooms: false
    },
    periods: [1, 2, 3, 4, 5, 6],
    places: {'전산실': 58, '준비물실': 52},
    bookedTabletsLists: []
  },
  mutations: {
  },
  actions: {
  }
}

export default bookStore
