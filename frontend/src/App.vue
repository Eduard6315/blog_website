<template>
  <header>
    <div class="logo">
      <img alt="Vue logo" src="@/assets/logo.svg" width="125" height="125" />
    </div>

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
          <router-link to="/" exact>Home</router-link>
          <router-link to="/about" exact>About</router-link>
          <router-link v-if="!isLoggedIn" to="/login">Войти</router-link>
          <button v-else @click="logout">Выйти</button>
          <router-link v-if="!isLoggedIn" to="/registration">Зарегистрироваться как гость</router-link>
        </nav>
    </div>
  </header>

  <router-view />
</template>

<script setup>
import { ref } from 'vue';
import HelloWorld from './components/HelloWorld.vue';

const isLoggedIn = ref(false);

function showLoginModal() {
  // Отобразить модальное окно для входа пользователя
}

function showGuestRegistrationForm() {
  // Отобразить форму регистрации гостя
}

function logout() {
  // Выполнить выход пользователя
}
</script>

<style scoped>
/* Ваши стили для хэдера */
</style>