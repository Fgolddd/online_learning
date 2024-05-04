import axios from "axios";

const namespaced = true;

const state = () => ({
    order: {}
});

const getters = {
    getOrder: (state) => state.order,
};

const actions = {
    async createOrder({ commit }) {
        // 使用实际的API URL替换此处的占位符
        const response = await axios.post('order/', {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`,
            },
        })
        commit('setOrder', response.data);

    },
};

const mutations = {
    setOrder(state, order) {
        state.order = order;
    },
};

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations,
};