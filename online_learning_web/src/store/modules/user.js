import axios from "axios";
import { toast } from 'bulma-toast'
import api from "../../api/index";

const namespaced = true;
const state = () => ({
    userId: null,
    username: null,
    refresh: null,
    token: null,
    userAvatar: null,
    isAuthenticated: false,
    userInfo: null,
});

const getters = {
    getUserId: (state) => state.userId,
    getUserName: (state) => state.username,
    getRefresh: (state) => state.refresh,
    getToken: (state) => state.token,
    getUserAvatar: (state) => state.userAvatar,
    getIsAuthenticated: (state) => state.isAuthenticated,
    getUserInfo: (state) => state.userInfo,
};

const actions = {
    async login({ commit }, form) {
        try {
            const response = await api.user.login(form);
            if (response.status === 200) {
                commit('setAuthData', response.data);
                toast({
                    message: '成功登录',
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
            message: '成功退出登录',
            type: 'is-primary',
            position: 'top-center',
            duration: 2000,
        })

    },
    async fetchUserInfo({ commit }, id) {
        const response = await api.user.getUserInfo(id)
        commit('setUserInfo', response.data);

    },

}

const mutations = {
    setUserInfo(state, userInfo) {
        state.userInfo = userInfo;
    },
    setAuthData(state, authData) {
        state.userId = authData.id;
        state.username = authData.username;
        state.refresh = authData.refresh;
        state.token = authData.token;
        state.userAvatar = authData.avatar;
        state.isAuthenticated = true;
        localStorage.setItem('refresh', authData.refresh);
        localStorage.setItem('token', authData.token);
        localStorage.setItem('userName', authData.username);
        localStorage.setItem('userId', authData.id);
        localStorage.setItem('userAvatar', authData.avatar);
    },
    clearAuthData(state) {
        state.userId = null;
        state.userName = null;
        state.token = null;
        state.isAuthenticated = false;
        localStorage.removeItem('refresh');
        localStorage.removeItem('token');
        localStorage.removeItem('userName');
        localStorage.removeItem('userId');
        localStorage.removeItem('userAvatar');
        // delete axios.defaults.headers.common['Authorization'];
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