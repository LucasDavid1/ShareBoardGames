import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
// Local css
//import "../public/Styles/classes.scss"
// Local icons
//import "../public/Styles/icons.scss"

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
