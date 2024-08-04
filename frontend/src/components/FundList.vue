<template>
  <button class="btn btn-dark" @click="fetchMessage">Fetch from Django</button>
  <div>
    <h1>Funds</h1>
    <ul>
      <li v-for="fund in funds" :key="fund.id">
        <router-link :to="{ path: `/fund/${fund.id}` }">
          {{ fund.name }} - NAV: ${{ fund.nav }}
        </router-link>
      </li>
    </ul>
  </div>

  <div class="d-flex">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Fund Type</h5>

        <p class="card-text">Some quick example</p>
      </div>
      <div class="card-footer d-flex justify-content-end">
        <div>
          <button class="btn btn-secondary">
            <router-link to="/fund">Explore</router-link>
          </button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Fund Type 2</h5>

        <p class="card-text">Some quick example</p>
      </div>
      <div class="card-footer d-flex justify-content-end">
        <div>
          <button class="btn btn-secondary">
            <router-link to="/fund">Explore</router-link>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const funds = ref([]);

const message = ref("No Message yet");

const fetchMessage = async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/api/test/");
    message.value = response.data.message;
  } catch (error) {
    console.error("Error fetching message:", error);
    message.value = "Error fetching message";
  }
};

// const fetchFunds = async () => {
//   try {
//     const response = await axios.get("http://localhost:8000/api/api/funds");
//   } catch {
//     console.log("error");
//   }
// };

// onMounted(fetchFunds);
</script>
