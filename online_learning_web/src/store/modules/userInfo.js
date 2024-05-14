import axios from "axios";

const namespaced = true;

const state = () => ({
    userInfo: {},
    videoInfo: {},
    myCourse: []
});

const getters = {
    getUserInfo: (state) => state.userInfo,
    getVideoInfoById: (state) => state.videoInfo,
    getMyCourse: (state) => state.myCourse,
};

const actions = {
    async fetchUserInfo({ commit }, id) {
        const headers = {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
        }
        const response = await axios.get(`user/info/${id}`, { headers })
        commit('setUserInfo', response.data);
    },


};

const mutations = {
    setUserInfo(state, userInfo) {
        state.userInfo = userInfo;
    },
    setVideoInfo(state, videoInfo) {
        state.videoInfo = videoInfo;
    },
    setMyCourse(state, myCourse) {
        state.myCourse = myCourse;
    },
};

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations,
};