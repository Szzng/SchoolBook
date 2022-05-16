const bookStore = {
  namespaced: true,
  state: {
    dialog: {
      checkTabletsBooking: false,
      checkComputerRoomsBooking: false,
      bookTablets: false,
      bookComputerRooms: false
    },
    bookedTabletsLists: []
  },
  mutations: {
  },
  actions: {
  }
}

export default bookStore
