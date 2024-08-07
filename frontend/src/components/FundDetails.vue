<template>
  <div v-if="fund">
    <div class="main-title d-flex flex-column align-items-center">
      <div class="mb-3 mt-5">
        <h1>{{ fund.name }}</h1>
      </div>
      <div class="mt-3">
        <button class="btn btn-outline-primary btn-lg">
          <router-link to="/fund_invest"> Invest </router-link>
        </button>
      </div>
    </div>

    <!-- tab navigation  -->
    <ul class="nav nav-tabs">
      <li class="nav-item" v-for="(tab, index) in tabs" :key="index">
        <a
          href="#"
          class="nav-link"
          :class="{ active: activeTab === tab.name }"
          @click.prevent="activeTab = tab.name"
          >{{ tab.label }}</a
        >
      </li>
    </ul>

    <!-- tab content  -->
    <div class="tab-content">
      <component :is="currentTabComponent" :fund="fund" />
    </div>
  </div>
  <div v-else>Loading fund details...</div>
</template>

<script setup>
import { ref, computed, onMounted, shallowRef } from "vue";

import GeneralTab from "../components/FundTabs/GeneralTab.vue";
import PerformanceTab from "../components/FundTabs/PerformanceTab.vue";

import axios from "axios";
import { useRoute } from "vue-router";

const tabs = shallowRef([
  { name: "General", label: "General", component: GeneralTab },
  { name: "Performance", label: "Performance", component: PerformanceTab },
]);

// Reactive variable to store the currently active tab name
const activeTab = ref(tabs.value[0].name);

// Computed property to dynamically return the currently active tab's component
const currentTabComponent = computed(() => {
  return tabs.value.find((tab) => tab.name === activeTab.value).component;
});

const route = useRoute();
const fundId = ref(route.params.id);
const fund = ref(null);

const fetchFundDetails = async () => {
  console.log("fetching fund id");
  try {
    const response = await axios.get(
      `http://localhost:8000/api/funds/${fundId.value}`
    );
    fund.value = response.data;
  } catch (err) {
    console.error("Error fetching funds: ", err);
  }
};

onMounted(fetchFundDetails);
</script>
