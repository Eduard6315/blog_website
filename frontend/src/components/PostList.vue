<template>
  <div>
    <h2>Посты</h2>
    <ul>
      <li v-for="post in posts" :key="post.id">
        <router-link :to="`/posts/${post.id}`">
          {{ post.title }}
        </router-link>
      </li>
    </ul>
    </div>
    <form @submit.prevent="createPost">
      <input v-model="newPost.title" type="text" id="postTitle" name="postTitle" placeholder="Заголовок поста">
      <textarea v-model="newPost.content" id="postBody" name="postBody" placeholder="Текст поста"></textarea>
      <button type="submit">Создать пост</button>
    </form>
    <div class="post_create" v-if="showMessage">
      {{ message }}
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      posts: [],
      newPost: {
        title: '',
        content: '',
         token: ''
      },
      delete_post: {
        token: ''
      },
       showMessage: false,
      message: '',

    }
  },
  mounted() {
    this.fetchPosts();
  },
  methods: {
    fetchPosts() {
      axios.get('http://127.0.0.1:8000/api/posts/')
        .then(response => {
          this.posts = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    createPost() {
      // Получение токена доступа из localStorage
      const token = localStorage.getItem('token');

      // Проверка наличия токена доступа
      if (!token) {
       console.log("Требуется аутентификация для создания поста.");
       return;
     }
      this.newPost.token = token;
      // Отправка запроса на создание поста с токеном доступа в заголовке
      axios.post('http://127.0.0.1:8000/api/posts/create/', this.newPost, {
        headers: {
          'Content-Type': 'application/json; charset=utf-8',
          'Authorization': `Bearer ${this.newPost.token}`
        },
      })
        .then((response) => {
          this.posts.push(response.data);
          this.newPost = { title: '', content: '', token: '' };
        })
        .catch(error => {
          if (error.response && error.response.status === 403) {
            console.log("Только администраторы могут создавать посты.");
            this.message = 'Только администраторы могут создавать посты.';
            this.showMessage = true;
          } else {
            console.error(error);
          }
        });

      }
     }

    }
</script>

<style>
  .post_create {
    color: red;
    font-weight: bold;
  }


  input {
    border: 1px solid gray;
    padding: 5px;
    margin-bottom: 10px;
  }
</style>