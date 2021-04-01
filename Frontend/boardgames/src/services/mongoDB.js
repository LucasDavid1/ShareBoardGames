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
};

export default Service;