import { createStore } from 'vuex';
import login from './modules/login';
import post from './modules/post';
import course from './modules/course';
import userInfo from './modules/userInfo';
import cart from './modules/cart';
export default createStore({
    modules: {
        login,
        post,
        course,
        userInfo,
        cart
    },
});