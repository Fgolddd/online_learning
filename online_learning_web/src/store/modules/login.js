import axios from "axios";
import { toast } from 'bulma-toast'


const namespaced = true;
const state = () => ({
    userId: null,
    username: null,
    token: null,
    isAuthenticated: false,
});

const getters = {
    getUserId: (state) => state.userId,
    getUserName: (state) => state.username,
    getToken: (state) => state.token,
    getIsAuthenticated: (state) => state.isAuthenticated,

};

const actions = {
    async login({ commit }, credentials) {
        try {
            const response = await axios.post('user/login/', credentials);
            if (response.status === 200) {
                commit('setAuthData', response.data);
                toast({
                    message: 'Login successful!',
                    type: 'is-primary',
                    position: 'top-center',
                    duration: 2000,
                })
            }

        } catch (error) {
            const message = error.response.data.detail
            toast({
                message: message,
                type: 'is-danger',
                position: 'top-center',
                duration: 2000,
            })
        }
    },

    logout({ commit }) {
        commit('clearAuthData');
        toast({
            message: 'Logout successful!',
            type: 'is-primary',
            position: 'top-center',
            duration: 2000,
        })

    },
}

const mutations = {
    setAuthData(state, authData) {
        state.userId = authData.id;
        state.username = authData.username;
        state.token = authData.token;
        state.isAuthenticated = true;
        localStorage.setItem('token', authData.token);
        localStorage.setItem('userName', authData.username);
        localStorage.setItem('userId', authData.id);
        axios.defaults.headers.common['Authorization'] = `Bearer ${authData.token}`;
    },
    clearAuthData(state) {
        state.userId = null;
        state.userName = null;
        state.token = null;
        state.isAuthenticated = false;
        localStorage.removeItem('token');
        localStorage.removeItem('userName');
        localStorage.removeItem('userId');
        delete axios.defaults.headers.common['Authorization'];
    },
    async register(state, form) {
        try {
            const response = await axios.post('user/register/', form);
            if (response.status === 201) {
                toast({
                    message: "注册成功",
                    type: 'is-primary',
                    position: 'top-center',
                    duration: 2000,
                })
            }
        } catch (error) {
            const message = error.response.data.error;
            toast({
                message: message,
                type: 'is-danger',
                position: 'top-center',
                duration: 2000,
            })
        }
    },
}

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations,
};