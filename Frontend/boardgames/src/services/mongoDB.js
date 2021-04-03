import axios from "axios";

const axiosInstance = axios.create({
    headers: {
      "Access-Control-Allow-Origin": "*"
    }
  });

const customHeaders = {
'content-type': 'application/json;charset=utf-8',
"Access-Control-Allow-Origin": "*"
};  

const Service = {
    ping: function(limit) {
        return new Promise((resolve, reject) => {            
            axios({
                method: 'get',
                url: 'http://127.0.0.1:8000/games_info/ping/',
                params: {
                  limit: 5
                }
              })
              .then(response => {
                resolve(response);
              })
              .catch(err => reject(err));
        });
      },
      getAllGames: function(limit) {
        return new Promise((resolve, reject) => {
            axios({
                method: 'get',
                url: 'http://127.0.0.1:8000/games_info/all/',
                params: {
                  limit : limit
                }
              })
            .then(response => {
              resolve(response.data);
            })
            .catch(err => reject(err));
        });
      },
      getCategories: function(limit) {
        return new Promise((resolve, reject) => {
            axios({
                method: 'get',
                url: 'http://127.0.0.1:8000/games_info/categories/',
                params: {
                  limit : limit
                }
              })
            .then(response => {
              resolve(response.data);
            })
            .catch(err => reject(err));
        });
      },
      getGamesByCategories: function(limit, category) {
        return new Promise((resolve, reject) => {
            axios({
                method: 'get',
                url: 'http://127.0.0.1:8000/games_info/games-by-categories/',
                params: {
                  limit : limit,
                  category : category
                }
              })
            .then(response => {
              resolve(response.data);
            })
            .catch(err => reject(err));
        });
      },
      getGamesByName: function(limit, name) {
        return new Promise((resolve, reject) => {
            axios({
                method: 'get',
                url: 'http://127.0.0.1:8000/games_info/by-name/',
                params: {
                  limit : limit,
                  game_name : name
                }
              })
            .then(response => {
              resolve(response.data);
            })
            .catch(err => reject(err));
        });
      },
};

export default Service;