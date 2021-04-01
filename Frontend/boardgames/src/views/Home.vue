<template>
  <div class="home">
    <p>Hola hola</p>
    <i class="lu-error" title="Play"></i>
  </div>
</template>

<script>
import mongoDB from "@/services/mongoDB.js";

export default {
  name: 'Home',
  data () {
    return {
      games: []
    }
  },
  created() {
    mongoDB
      .getAllGames(1)
      .then(response => {
        console.log(response)
      })
  }
};
</script>
