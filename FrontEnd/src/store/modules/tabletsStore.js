const tabletsStore = {
  namespaced: true,
  state: {
    dialog: {
      checkTabletsBooking: false,
      bookTablets: false,
      destroyTablet: false
    },
    periods: [1, 2, 3, 4, 5, 6],
    places: {'전산실': 58, '준비물실': 52},
    bookedTabletsLists: [],
    left: []
  },
  mutations: {
  },
  actions: {
  }
}

export default tabletsStore
