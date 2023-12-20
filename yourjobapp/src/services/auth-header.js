export default function authHeader(){
    let user = JSON.parse(localStorage.getItem('user'))||null;
    if(user && user.access_token){
        const headerAuth = {
            "Access-Control-Allow-Origin": '*',
            'Content-Type': 'application/json',
            "Authorization": 'Bearer ' + user.access_token
        }
        return headerAuth
    }else{
        return {};
    }
}