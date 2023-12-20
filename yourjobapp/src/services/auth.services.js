import axios from 'axios'
const API_URL = 'https://rafif.pythonanywhere.com/api/rafif/yourjobapp/'
let timeStamp = Date.now()

const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
}

class AuthService{
    login(user){
        return axios
            .post(API_URL + 'login?t=' + timeStamp , {
                    username:user.username,
                    sandi:user.sandi
                },
                {
                    headers:headers
                }
            )
            .then(response => {
                if(response.data.access_token){
                    localStorage.setItem('user',JSON.stringify(response.data));
                }
                return response.data;
            });
    }
    logout(){
        localStorage.removeItem('user');
    }
}

export default new AuthService();