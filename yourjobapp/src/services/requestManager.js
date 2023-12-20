import axios,{ Canceler, CancelTokenSource } from 'axios';

const PendingRequest = {
    request : new Promise(()=>{}),
    cancel : () => {Canceler}
}

let pendingRequest = [];

export function addPendingRequest(request,cancelTokenSource){
    pendingRequest.push({request,cancel:cancelTokenSource});
}

export function cancelAllRequest(){
    pendingRequest.forEach(({cancel})=>{
        cancel('All requests canceled');
    });
    pendingRequest = [];
}