const generalStore = {
  namespaced: true,
  state: {
    dialog: {
      success: false,
      login: false,
      logout: false
    },
    successMsg: '',
    school: {name: 'Guest'}
  }
}

export default generalStore
