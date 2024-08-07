<template>
  <h2>{{ fund?.name }}</h2>
  <Line v-if="chartData" :data="chartData" :options="chartOptions" />
</template>

<script setup>
import { ref, defineProps, onMounted } from "vue";
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

const chartData = ref(null);
const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: true,
});
const generateChartData = () => {
  // Generate random data
  const data = Array.from({ length: 7 }, () => Math.floor(Math.random() * 100));

  chartData.value = {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
      {
        label: "Fund Performance",
        backgroundColor: "#f87979",
        data,
      },
    ],
  };
};

defineProps({
  fund: Object,
});

onMounted(() => {
  generateChartData();
});
</script>
