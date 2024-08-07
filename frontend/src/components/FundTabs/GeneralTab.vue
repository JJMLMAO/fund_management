<template>
  <div v-if="fund">
    <h2>General details of {{ fund.name }}</h2>
    <p>{{ fund.description }}</p>
    {{ fund.risk_profile }}
    <div class="row">
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h3>Investment type</h3>
            <h5>{{ fund.investment_type }}</h5>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h3>Current NAV</h3>
            <h5>{{ fund.current_nav }}</h5>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h3>YTD Return</h3>
            <h5>{{ fund.ytd_return }}</h5>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h3>Currency</h3>
            <h5>{{ fund.currency }}</h5>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h3>Risk Profile</h3>
            <h5>{{ fund.risk_profile }}</h5>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h3>Shariah Compliant</h3>
            <h5>{{ fund.shahriah_compliant }}</h5>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else>Loading fund details...</div>
</template>

<script setup>
import { defineProps } from "vue";

defineProps({
  fund: Object, // Define prop to receive the fund object
});
</script>
