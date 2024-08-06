<template>
  <div class="fund-invest">
    <h2>Invest in Fund</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="amount">Amount</label>
        <input
          type="number"
          id="amount"
          v-model="amount"
          class="form-control"
          required
        />
      </div>
      <div class="form-group">
        <label for="units">Number of Units</label>
        <input
          type="number"
          id="units"
          v-model="units"
          class="form-control"
          required
        />
      </div>
      <button type="submit" class="btn btn-primary">Invest</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";

const amount = ref("");
const units = ref("");

const submitForm = () => {
  const investmentDetails = {
    amount: amount.value,
    units: units.value,
  };

  // Perform necessary actions, like sending data to the server or updating the state
  console.log("Investment Details:", investmentDetails);

  // Reset the form
  amount.value = "";
  units.value = "";
};
</script>

<style scoped>
.fund-invest {
  max-width: 400px;
  margin: auto;
}
</style>
