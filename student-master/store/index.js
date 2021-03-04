import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        realURL: "http://127.0.0.1:8000/",
        user_id: null,
    },
    mutations: {
        login(state, user_id) {
            state.user_id = user_id;
        },
        login_out(state) {
            state.user_id = null;
        }
    }
})

export default store
