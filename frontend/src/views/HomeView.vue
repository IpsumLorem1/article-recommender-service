<template>
  <div class="wrapper">
    <main>
      <form @submit.prevent="sendRequest" class="form-container">
        <h4 class="form-title">Поиск статей</h4>
        <textarea
          v-model="query"
          class="input-area"
          placeholder="Введите ваш запрос"
        ></textarea>
        <button type="submit" class="submit-button">Отправить</button>
      </form>
      <div v-if="results.length" class="results-container">
        <h5 class="results-title">Результаты поиска:</h5>
        <ul class="results-list">
          <li v-for="(result, index) in results" :key="index" class="result-item">
            <strong>{{ result.title }}</strong> - {{ result.text }}
          </li>
        </ul>
      </div>
    </main>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      query: "", // Поле для ввода запроса
      results: [], // Результаты поиска
    };
  },
  methods: {
    async sendRequest() {
      try {
        const response = await axios.post("/api/search", { query: this.query });
        this.results = response.data.results;
      } catch (error) {
        console.error("Ошибка при выполнении запроса:", error);
      }
    },
  },
};
</script>

<style scoped>
.wrapper {
  min-height: 100vh;
  display: flex;
  flex-flow: column nowrap;
  align-items: center;
  justify-content: center;
  background-color: #f9f9f9;
  padding: 20px;
}

.form-container {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
  width: 100%;
  max-width: 500px;
}

.form-title {
  font-size: 20px;
  font-weight: bold;
  color: #333;
  margin-bottom: 15px;
}

.input-area {
  width: 100%;
  height: 120px;
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  resize: none;
}

.submit-button {
  display: inline-block;
  width: 100%;
  padding: 10px 15px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  text-align: center;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #0056b3;
}

.results-container {
  margin-top: 20px;
  width: 100%;
  max-width: 500px;
}

.results-title {
  font-size: 18px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

.results-list {
  list-style: none;
  padding: 0;
}

.result-item {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: #fff;
  margin-bottom: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
