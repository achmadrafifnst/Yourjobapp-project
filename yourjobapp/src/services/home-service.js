import axios from 'axios';
import authHeader from '@/services/auth-header';
import {addPendingRequest} from '@/services/requestManager';


class HomeServices{
    getHome(){
        let cancelTokenSource = axios.CancelToken.source();
        const request = axios.get('https://rafif.pythonanywhere.com/api/rafif/yourjobapp/home',{
            cancelToken:cancelTokenSource.token,
            headers:authHeader()
        });
        addPendingRequest(request,cancelTokenSource);
        return request;
    }
    getMain(){
        let cancelTokenSource = axios.CancelToken.source();
        const request = axios.get('https://rafif.pythonanywhere.com/api/rafif/yourjobapp/main',{
            cancelToken:cancelTokenSource.token,
            headers:authHeader()
        });
        addPendingRequest(request,cancelTokenSource);
        return request;
    }
    submitForm(data){
        let cancelTokenSource = axios.CancelToken.source();
        const request = axios.post('https://rafif.pythonanywhere.com/api/rafif/yourjobapp/recommendation',data,{
            cancelToken:cancelTokenSource.token,
            headers:authHeader()
        });
        addPendingRequest(request,cancelTokenSource);
        return request;
    }
}

export default new HomeServices();