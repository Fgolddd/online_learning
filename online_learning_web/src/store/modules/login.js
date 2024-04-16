import axios from "axios";

const namespaced = true;
const state = () => ({
    userId: null,
    username: null,
    token: null,
    isAuthenticated: false,
    loginError: null,
});

const getters = {
    getUserId: (state) => state.userId,
    getUserName: (state) => state.username,
    getToken: (state) => state.token,
    getIsAuthenticated: (state) => state.isAuthenticated,
    getLoginError: (state) => state.loginError,
};

const actions = {
    async login({ commit }, credentials) {
        commit('clearLoginError');
        try {
            const response = await axios.post('api/users/login/', credentials);
            commit('setAuthData', response.data);
            console.log(response.data);
            axios.defaults.headers.common['Authorization'] = "Bearer" + response.data.token;
            localStorage.setItem('token', response.data.token)
        } catch (error) {
            commit('setLoginError', error.response?.data?.message || 'An error occurred during login.');
        }
    },

    logout({ commit }) {
        commit('clearAuthData');
    },
}

const mutations = {
    setAuthData(state, authData) {
        state.userId = authData.id;
        state.username = authData.username;
        state.token = authData.token;
        state.isAuthenticated = true;
    },
    clearAuthData(state) {
        state.userId = null;
        state.userName = null;
        state.token = null;
        state.isAuthenticated = false;
    },
    setLoginError(state, error) {
        state.loginError = error;
    },
    clearLoginError(state) {
        state.loginError = null;
    }
}

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations,
};