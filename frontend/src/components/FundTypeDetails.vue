<template>
  <div v-for="fund in filteredFunds" :key="fund.id">
    <h1>{{ fund.investment_type }}</h1>
  </div>
  <div class="d-flex">
    <div class="card" v-for="fund in filteredFunds" :key="fund.id">
      <div class="card-body">
        <h5 class="card-title">{{ fund.name }}</h5>
        <p class="card-text">
          {{ fund.description }}
        </p>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item">{{ fund.investment_type }}</li>
        <li class="list-group-item">{{ fund.current_nav }}</li>
        <li class="list-group-item">{{ fund.ytd_return }}</li>
      </ul>
      <div class="card-body d-flex justify-content-end">
        <button class="btn btn-secondary">
          <router-link
            :to="{
              name: 'fund_details',
              params: { id: fund.id },
            }"
          >
            View
          </router-link>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";

// const router = useRouter();
const route = useRoute();

const investmentType = ref(route.params.type);
const funds = ref([]);

const filteredFunds = computed(() => {
  return funds.value.filter(
    (fund) => fund.investment_type === investmentType.value
  );
});

const fetchFunds = async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/funds/");
    funds.value = response.data;
  } catch (err) {
    console.error("Error fetching funds:", err);
  }
};

onMounted(fetchFunds);
</script>
