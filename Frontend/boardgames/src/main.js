import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
// Local css
import "../public/Styles/classes.less"
// Local icons
import "../public/Styles/icons.less"

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
