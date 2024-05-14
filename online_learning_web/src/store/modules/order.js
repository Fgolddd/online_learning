import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter()
const namespaced = true;

const state = () => ({
    order: {},
    orderList: [],
});

const getters = {
    getOrder: (state) => state.order,
    getOrderList: (state) => state.orderList,
};

const actions = {
    async createOrder({ commit }) {
        try {
            const response = await axios.post('order/', {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem("token")}`,
                }
            })
            commit('setOrder', response.data);
            console.log(response.data);
            router.push('/order')
        } catch (error) {
            console.log(error);
        }
    },
    async fetchOrderList({ commit }) {
        try {
            const headers = {
                Authorization: `Bearer ${localStorage.getItem("token")}`,
            }
            const response = await axios.get('order/', { headers });
            commit('setOrderList', response.data);
            console.log(response.data);
        } catch (error) {
            console.log(error);
        }
    },
};

const mutations = {
    setOrder(state, order) {
        state.order = order;
    },
    setOrderList(state, orderList) {
        state.orderList = orderList;
    },

};

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations,
};