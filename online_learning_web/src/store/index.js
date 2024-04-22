import { createStore } from 'vuex';
import login from './modules/login';
import post from './modules/post';
import course from './modules/course';
import userInfo from './modules/userInfo';
export default createStore({
    modules: {
        login,
        post,
        course,
        userInfo
    },
});