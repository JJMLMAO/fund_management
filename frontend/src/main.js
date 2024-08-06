import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import FundList from "./components/FundList.vue";
import FundTypeDetails from "./components/FundTypeDetails.vue";
import FundDetails from "./components/FundDetails.vue";
import FundInvest from "./components/FundInvest.vue";
import MyPortfolio from "./components/MyPortfolio.vue";

import "./assets/custom.css";
// import FundDetail from "./components/FundDetail.vue";
// import UserPortfolio from "./components/UserPortfolio.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: FundList },
    { path: "/fund_type_details/", component: FundTypeDetails },
    { path: "/fund_details/", component: FundDetails },
    { path: "/fund_invest/", component: FundInvest },
    { path: "/my_portfolio", component: MyPortfolio },

    // { path: "/fund/:id", component: FundDetail, props: true },
    // { path: "/portfolio", component: UserPortfolio },
  ],
});

const app = createApp(App);
app.use(router);
app.mount("#app");
