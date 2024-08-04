import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import FundList from "./components/FundList.vue";
import FundDetails from "./components/FundDetails.vue";
import "./assets/custom.css";
// import FundDetail from "./components/FundDetail.vue";
// import UserPortfolio from "./components/UserPortfolio.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: FundList },
    { path: "/fund/", component: FundDetails },

    // { path: "/fund/:id", component: FundDetail, props: true },
    // { path: "/portfolio", component: UserPortfolio },
  ],
});

const app = createApp(App);
app.use(router);
app.mount("#app");
