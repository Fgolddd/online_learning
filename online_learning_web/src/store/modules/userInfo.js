import axios from "axios";

const namespaced = true;

const state = () => ({
    userInfo: {},
});

const getters = {
    getUserInfo: (state) => state.userInfo,
};

const actions = {
    async fetchUserInfo({ commit }, id) {
        const headers = {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
        }
        const response = await axios.get(`users/profiles/${id}`, { headers })
        commit('setUserInfo', response.data);
    },
};

const mutations = {
    setUserInfo(state, userInfo) {
        state.userInfo = userInfo;
    },
};

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations,
};