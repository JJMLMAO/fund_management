<template>
  <h2>Performance for International Growth Funds</h2>
  <Line :data="chartData" :options="chartOptions" />
</template>

<script setup>
import { ref } from "vue";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "vue-chartjs";
import * as chartConfig from "../utils/chartConfig.js";

// Register necessary Chart.js components
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const chartData = ref(chartConfig.data);
const chartOptions = ref(chartConfig.options);
</script>
