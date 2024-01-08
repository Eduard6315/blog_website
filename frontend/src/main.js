import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import Registration from './components/Registration.vue';


const app = createApp(App)


app.use(createPinia())
app.use(router)

app.component('Registration', Registration)


app.mount('#app')