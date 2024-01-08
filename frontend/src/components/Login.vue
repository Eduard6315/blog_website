<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="handleLogin">
      <input type="text" v-model="formData.username" placeholder="Username" autocomplete="off"><br>
      <input type="password" v-model="formData.password" placeholder="Password" autocomplete="current-password"><br>
      <button type="submit">Login</button>
    </form>
    <div class="login" v-if="showMessage">
      {{ message }}
    </div>
  </div>
</template>



<script>
import axios from 'axios';

export default {
  data() {
    return {
      formData: {
        username: '',
        password: ''
      },
       showMessage: false,
      message: '',
    };
  },
    methods: {
      async handleLogin() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/login/', this.formData);
          console.log(response.data);
          if (response.data.token) {
            localStorage.setItem('token', response.data.token);  // Сохранение токена в localStorage
            // Перенаправление на страницу /posts
            this.$router.push('/posts');
          } else {
            console.error('Ошибка: токен не был получен в ответе сервера');
          }
        } catch (error) {
          if (error.response.status === 401 && error.response.data.code === 'token_not_valid') {
            console.error('Ошибка: токен не действителен');
            // Дополнительные действия при недействительном токене
          } else {
            console.error(error); // Вывод ошибки в консоль для отладки
            // Дополнительные действия при возникновении других ошибок
            this.message = 'Неверный логин или пароль. Пожалуйста, попробуйте еще раз.';
            this.showMessage = true;
          }
        }
    }
  }
};
</script>



<style>
  .login {
    color: red;
    font-weight: bold;
  }

  input {
    border: 1px solid gray;
    padding: 5px;
    margin-bottom: 10px;
  }
</style>