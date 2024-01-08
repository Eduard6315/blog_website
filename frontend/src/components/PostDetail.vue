<template>
          <div>
          <h2>{{ post.title }}</h2>
          <p>{{ post.content }}</p>
          <h3>Комментарии:</h3>
          <ul>
            <li v-for="comment in post.comments" :key="comment.id">
              {{ comment.text }}
            </li>
          </ul>
          <form @submit.prevent="createComment">
            <input type="text" v-model="newCommentText" placeholder="Ваш комментарий" required>
            <button type="submit">Добавить комментарий</button>
          </form>
      <p>{{ post.text }}</p>
      <button @click="deletePost(post.id)">Удалить пост</button>
    </div>
    <div class="post_delete" v-if="showMessage">
      {{ message }}
    </div>

</template>


<script>
import axios from 'axios';

const yourAuthToken = localStorage.getItem('token');

export default {
  data() {
  return {
    post: null,
    delete_post: {
      token: '',
       text: '',
    },
    showMessage: false,
    newCommentText: '',
  };
},

          created() {
            this.fetchPost();
          },
          methods: {
            fetchPost() {
              const postId = this.$route.params.id;
              axios.get(`http://127.0.0.1:8000/api/posts/${postId}/`, {
                headers: { Authorization: `Bearer ${yourAuthToken}` }
              })
                .then(response => {
                  this.post = response.data;
                })
                .catch(error => {
                  console.error(error);
                });
            },

             createComment() {
                // Отправка данных на сервер с использованием axios или другой библиотеки для HTTP-запросов
                const postId = this.$route.params.id;
                const data = {
                  text: this.newCommentText,
                  post_id: postId
                };
               axios.post(`http://127.0.0.1:8000/api/posts/${postId}/comments/create/`, data)
                  .then(response => {
                    // Обработка успешного ответа сервера
                    console.log(response.data);
                     // Обновление списка комментариев
                       this.fetchPost();
                  })
                  .catch(error => {
                    // Обработка ошибки
                    console.error(error);
                  });
              },


           deletePost(postId) {
          const token = localStorage.getItem('token');
          if (!token) {
            console.log("Требуется аутентификация для удаления поста.");
            return;
          }
          const deletePostData = {
            token: token
          };
          axios.delete(`http://127.0.0.1:8000/api/posts/delete/${postId}/`, {
            headers: {
              'Authorization': `Bearer ${token}`
            },
            data: {
              token: token
            }
          })
            .then((response) => {
              if (response.status === 204) {
                console.log('Пост успешно удален');
                // Удаление удаленного поста из списка постов
                this.$router.push('/posts');
              } else {
                console.error('Ошибка при удалении поста');
              }
            })
            .catch((error) => {
              console.error('Ошибка при отправке DELETE-запроса:', error);
              if (error.response && error.response.status === 403) {
                console.log("Только администраторы могут удалять посты.");
                this.message = 'Только администраторы могут удалять посты.';
                this.showMessage = true;
              } else {
                console.error(error);
              }
            });
           }
          },
        };
</script>

<style>
  .post_delete {
    color: red;
    font-weight: bold;
  }


  input {
    border: 1px solid gray;
    padding: 5px;
    margin-bottom: 10px;
  }
</style>