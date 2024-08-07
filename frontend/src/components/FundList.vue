<template>
  <h1>Funds</h1>

  <div class="d-flex flex-wrap">
    <div class="card" v-for="fund in funds" :key="fund.id">
      <div class="card-body">
        <h5 class="card-title">{{ fund.investment_type }}</h5>

        <p class="card-text">{{ fund.description }}</p>
      </div>
      <div class="card-footer d-flex justify-content-end">
        <div>
          <button class="btn btn-outline-secondary">
            <router-link
              :to="{
                name: 'fund_type_details',
                params: { type: fund.investment_type },
              }"
              >Explore</router-link
            >
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const funds = ref([]);
const error = ref(null);

const fetchFunds = async () => {
  try {
    console.log("Fetching funds...");
    const response = await axios.get("http://localhost:8000/api/funds/");
    console.log("Response:", response.data);
    funds.value = response.data;
    console.log("funds value: ", funds.value);
  } catch (err) {
    console.error("Error fetching funds:", err);
    error.value = "An error occurred while fetching funds.";
  }
};

onMounted(fetchFunds);
</script>
