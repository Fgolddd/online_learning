import axios from "axios";

const namespaced = true;

const state = () => ({
    userInfo: {},
    videoInfo: {},
});

const getters = {
    getUserInfo: (state) => state.userInfo,
    getVideoInfoById: (state) => state.videoInfo,
};

const actions = {
    async fetchUserInfo({ commit }, id) {
        const headers = {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
        }
        const response = await axios.get(`user/info/${id}`, { headers })
        commit('setUserInfo', response.data);
    },
    async fetchVideoInfo({ commit }, id) {
        const headers = {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
        }

        const response = await axios.get(`course/video/${id}`, { headers })
        commit('setVideoInfo', response.data);

    },
};

const mutations = {
    setUserInfo(state, userInfo) {
        state.userInfo = userInfo;
    },
    setVideoInfo(state, videoInfo) {
        state.videoInfo = videoInfo;
    },
};

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations,
};