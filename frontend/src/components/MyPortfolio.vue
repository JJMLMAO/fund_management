<template>
  <div class="my-portfolio">
    <div class="row">
      <div class="col">
        <div class="portfolio-summary">
          <h2>My Portfolio</h2>
          <div class="d-flex justify-content-between">
            <h4>Total Earnings:</h4>
            <div class="card">
              <h3>
                <strong>{{ totalEarnings.toFixed(2) }}</strong>
              </h3>
            </div>
          </div>
        </div>

        <div class="myfunds">
          <h2>My Funds</h2>
          <div class="card-deck d-flex">
            <div
              v-for="fund in portfolio.funds"
              :key="fund.fundName"
              class="card"
            >
              <div class="card-body">
                <h5 class="card-title">{{ fund.fundName }}</h5>
                <p class="card-text">
                  Amount Invested: {{ fund.amountInvested.toFixed(2) }}
                </p>
                <p class="card-text">Units Owned: {{ fund.unitsOwned }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col">
        <h2>Genral info</h2>
        <div class="card-deck">
          <div class="card mb-3">
            <div class="card-body d-flex justify-content-between">
              <div>
                <h5 class="card-title">Risk profile</h5>
              </div>
              <div>
                <span class="badge text-bg-danger">High</span>
              </div>
            </div>
          </div>
          <div class="card mb-3">
            <div class="card-body d-flex justify-content-between">
              <div>
                <h5 class="card-title">Preferred currency</h5>
              </div>
              <div>
                <span class="badge text-bg-primary">MYR</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";

// Mock data for demonstration purposes
const portfolio = ref({
  funds: [
    {
      fundName: "Fund A",
      amountInvested: 1000,
      unitsOwned: 10,
      currentPricePerUnit: 120,
    },
    {
      fundName: "Fund B",
      amountInvested: 2000,
      unitsOwned: 20,
      currentPricePerUnit: 90,
    },
    {
      fundName: "Fund C",
      amountInvested: 1500,
      unitsOwned: 15,
      currentPricePerUnit: 110,
    },
  ],
});

// Compute total earnings
const totalEarnings = computed(() => {
  return portfolio.value.funds.reduce((total, fund) => {
    const currentValue = fund.unitsOwned * fund.currentPricePerUnit;
    return total + (currentValue - fund.amountInvested);
  }, 0);
});

onMounted(() => {
  // Fetch portfolio data from backend or state management store
  // Example: fetchPortfolio();

  // For now, using mock data. Replace the mock data with actual fetched data.
  console.log("Portfolio data loaded:", portfolio.value);
});

// Example function to fetch portfolio data (replace with actual implementation)
// async function fetchPortfolio() {
//   try {
//     const response = await fetch('/api/portfolio'); // Replace with your API endpoint
//     const data = await response.json();
//     portfolio.value = data;
//   } catch (error) {
//     console.error('Error fetching portfolio:', error);
//   }
// }
</script>
