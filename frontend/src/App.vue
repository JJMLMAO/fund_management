<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-body-tertiary" id="navFund">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/">Fund Manager</router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNavAltMarkup"
          aria-controls="navbarNavAltMarkup"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <router-link class="nav-link" to="/">Funds</router-link>
            <router-link class="nav-link" to="/my_portfolio"
              >Portfolio</router-link
            >
          </div>
        </div>
      </div>
    </nav>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script></script>
