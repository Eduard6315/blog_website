    import { createRouter, createWebHistory } from 'vue-router';
    import HomeView from '../views/HomeView.vue';
    import PostList from '../components/PostList.vue';
    import AboutView from '../views/AboutView.vue';
    import Login from '../components/Login.vue';
    import Registration from '../components/Registration.vue';
    import PostDetail from '../components/PostDetail.vue';


    const router = createRouter({
      history: createWebHistory(import.meta.env.BASE_URL),
       routes: [
        {
          path: '/',
          name: 'home',
          component: HomeView
        },
        {
          path: '/about',
          name: 'about',
          component: AboutView
        },
        {
          path: '/login',
          name: 'login',
          component: Login
        },
        {
          path: '/registration',
          component: Registration
        },
        {
          path: '/posts',
          name: 'Posts',
          component: PostList
        },
         {
          path: '/posts/:id',
          name: 'post-detail',
          component: PostDetail,
          props: true,
        },

      ]
    });

    export default router;