const generalStore = {
  namespaced: true,
  state: {
    dialog: {
      success: false,
      login: false,
      logout: false
    },
    successMsg: '',
    access: {token: '', exp: ''},
    school: { name: 'Guest' },
    code: ' '
  }
}

export default generalStore
