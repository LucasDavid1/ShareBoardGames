<template>
  <div class="home">    
    <i class="lu-error" title="Play" v-loading="loading"></i>
    <div class="row" v-for="category in categories">
      <div class="container">
        <div class="row">
          <div class="col-sm-2">
            <h5>{{ category }}</h5>        
          </div>  
          <div class="col-sm-10"></div>    
        </div>        
        <div class="row" v-if="games.find(x => x.category === category)">
          <div 
            class="col-sm-3 mr-1 mt-1 game-box" 
            v-loading="loading"
            @click="toGameDetail(specific_game)"
            v-for="specific_game in games.find(x => x.category === category).games_getted">
            {{ specific_game.name }}
          </div>
        </div>
        <div class="row mt-0 mb-0">
          <div class="col-sm-12">
            <hr style="border-top: 1px solid #a6c8ea">    
          </div>          
        </div>        
      </div>
    </div> 
  </div>
</template>

<script>
import mongoDB from "@/services/mongoDB.js";

export default {
  name: 'Home',
  data () {
    return {
      loading: true,
      games: [],
      categories: [],
      limit: 20
    }
  },
  created() {
    mongoDB
      .getCategories(6) // Se trae 6 categorias de juegos.
      .then(response => {
        this.categories = response
        response.forEach(el => {
          mongoDB
          .getGamesByCategories(this.limit, el) // Se trae 'limit' juegos por categoria.
          .then(games_getted => {
            this.games.push({
              category: el,
              games_getted: games_getted
            })
            this.loading = false        
          })
        })         
      })            
  },
  methods: {
    toGameDetail(game) {
      this.$router.push({name: "GameDetail", params: {game: game}})
    }
  }
};
</script>
