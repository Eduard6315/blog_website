<template>
  <div>
    <h1>Регистрация</h1>
    <form @submit.prevent="handleRegistration" v-if="!showMessage">
      <input type="text" v-model="formData.username" placeholder="Username" autocomplete="off"><br>
      <input type="email" v-model="formData.email" placeholder="Email" autocomplete="username"><br>
      <input type="password" v-model="formData.password" placeholder="Password" autocomplete="current-password"><br>
      <button type="submit">Зарегистрируйтесь</button>
    </form>
    <div class="registration" v-if="showMessage">
      {{ message }}
    </div>
     <div class="nonregistration" v-if="showMessage_2">
      {{ message_2}}
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
        email: '',
        password: '',
      },
      showMessage: false,
      message: '',
       showMessage_2: false,
      message_2: '',

    };
  },
  methods: {
    handleRegistration() {
      const config = {
        headers: {
          'Content-Type': 'application/json',
        },
      };

      axios
        .post('http://127.0.0.1:8000/api/registration/', this.formData, config)
        .then((response) => {
          const token = response.data.token; // Получение токена из ответа
          console.log(token); // Вывод токена в консоль для отладки

          // Сохранение токена в localStorage или сессии для последующего использования
          localStorage.setItem('token', token); // Сохранение токена в localStorage
          // или
          // sessionStorage.setItem('token', token); // Сохранение токена в сессии

          // Устанавливаем сообщение о регистрации и показываем его
          this.message = 'Вы успешно зарегистрированы!' ;
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);

          // Устанавливаем сообщение об ошибке и показываем его
          this.message_2 = 'Ошибка при регистрации. Пожалуйста, попробуйте еще раз.';
          this.showMessage_2 = true;
        });
    },
  },
};
</script>

<style>
  .registration {
    color: green;
    font-weight: bold;
  }
  .nonregistration {
    color: red;
    font-weight: bold;
  }

  input {
    border: 1px solid gray;
    padding: 5px;
    margin-bottom: 10px;
  }
</style>