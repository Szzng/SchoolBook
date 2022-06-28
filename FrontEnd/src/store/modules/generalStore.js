const generalStore = {
  namespaced: true,
  state: {
    dialog: {
      success: false,
      error: false,
      login: false,
      logout: false
    },
    successMsg: '',
    errorMsg: '',
    access: {token: '', exp: ''},
    school: { name: 'Guest' },
    code: ' '
  }
}

export default generalStore
