import axios from "axios";

const namespaced = true;

const state = () => ({
    courses: [],
});

const getters = {
    getCourses: (state) => state.courses,
    // 在Vuex store的getters对象中定义
    getCourseById: (state) => (id) => state.courses.find((course) => course.id === id),
};

const actions = {
    async fetchCourses({ commit }) {
        // 使用实际的API URL替换此处的占位符
        const response = await axios.get('course/')
        commit('setCourses', response.data);

    },
};

const mutations = {
    setCourses(state, courses) {
        state.courses = courses;
    },
};

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations,
};