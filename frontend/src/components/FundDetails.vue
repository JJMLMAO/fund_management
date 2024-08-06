<template>
  <div class="main-title d-flex flex-column align-items-center">
    <div class="mb-3 mt-5">
      <h1>International Growth Funds</h1>
    </div>
    <div class="mt-3">
      <button class="btn btn-primary btn-lg">
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
    <component :is="currentTabComponent" />
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import GeneralTab from "../components/FundTabs/GeneralTab.vue";
import PerformanceTab from "../components/FundTabs/PerformanceTab.vue";

const tabs = ref([
  { name: "General", label: "General", component: GeneralTab },
  { name: "Performance", label: "Performance", component: PerformanceTab },
]);

// Reactive variable to store the currently active tab name
const activeTab = ref(tabs.value[0].name);

// Computed property to dynamically return the currently active tab's component
const currentTabComponent = computed(() => {
  return tabs.value.find((tab) => tab.name === activeTab.value).component;
});
</script>
