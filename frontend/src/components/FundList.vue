<template>
  <div>
    <button @click="fetchMessage">Fetch from Django</button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

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
</script>
