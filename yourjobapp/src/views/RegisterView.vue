<template>
    <div style="height: 100%; background-color: rgb(226, 221, 221);" class="pa-16 align-center justify-center">
        <v-row align-center class="d-flex align-center justify-center">
            <v-col cols="12" md="12" class="pa-auto">
                <v-card class="pa-3 mx-auto" id="card-container">
                    <v-form @submit.prevent="validate" ref="form" lazy-validation v-model="valid">
                        <v-col>
                            <v-row class="d-flex align-center justify-center">
                                <h1>Sign Up</h1>
                            </v-row>
                            <v-row class="d-flex align-center justify-center mt-5">
                                <v-col cols="12" md="10" sm="12">
                                    <v-text-field 
                                        color="primary" 
                                        v-model="name" 
                                        :rules="nameRules" 
                                        outlined
                                        label="Enter your name" 
                                        style="border-radius: 15px;"
                                        required 
                                    ></v-text-field>
                                </v-col>
                            </v-row>
                            <v-row class="d-flex align-center justify-center">
                                <v-col cols="12" md="10" sm="12">
                                    <v-text-field 
                                        color="primary" 
                                        v-model="userName" 
                                        :rules="userNameRules" 
                                        outlined
                                        label="Enter your username" 
                                        style="border-radius: 15px;"
                                        required 
                                    ></v-text-field>
                                </v-col>
                            </v-row>
                            <v-row class="d-flex align-center justify-center ">
                                <v-col cols="12" md="10" sm="12">
                                    <v-text-field 
                                        color="primary" 
                                        v-model="email" 
                                        :rules="emailRules" 
                                        outlined
                                        label="Enter your email" 
                                        style="border-radius: 15px;"
                                        required 
                                    ></v-text-field>
                                </v-col>
                            </v-row>
                            <v-row class="d-flex align-center justify-center">
                                <v-col cols="12" md="10" sm="12">
                                    <v-text-field 
                                        color="primary" 
                                        v-model="password" 
                                        :rules="passwordRules" 
                                        outlined
                                        type="password"
                                        label="Enter your password" 
                                        style="border-radius: 15px;"
                                        required 
                                    ></v-text-field>
                                </v-col>
                            </v-row>
                            <v-row class="button-row-container">
                                <v-col cols="12" md="4">
                                    <v-btn 
                                        elevation="0" 
                                        color="rgb(49, 43, 43)" 
                                        tile 
                                        @click="validate" 
                                        class="mb-3 pa-0"
                                        text
                                    >
                                        Create Account
                                    </v-btn>
                                </v-col>
                            </v-row>
                        </v-col>
                    </v-form>
                </v-card>
            </v-col>
        </v-row>
        <v-snackbar 
            v-model="snackbar" 
            :timeout="0"
        >
            {{ this.info }}
            <template v-slot:action="{attrs}" v-if="this.info=='Register Berhasil'">
                <v-btn
                    :color="colorInfo"
                    text
                    v-bind="attrs"
                    @click="correctCloseSnackbar"
                >
                    Close
                </v-btn>
            </template>
            <template v-slot:action="{attrs}" v-else>
                <v-btn
                    :color="colorInfo"
                    text
                    v-bind="attrs"
                    @click="failCloseSnackbar"
                >
                    Close
                </v-btn>
            </template>
        </v-snackbar>
    </div>
</template>
<script>
import axios from 'axios'

export default{
    name:'RegisterView',
    data(){
        return{
            valid:true,
            name:'',
            info:'',
            colorInfo:'',
            snackbar:false,
            nameRules: [
                v => !!v || 'Name is required',
                v => (v && v.length >= 3) || 'Name must be min 3 characters',
            ],
            userName:'',
            userNameRules: [
                v => !!v || 'Username is required',
                v => (v && v.length >= 3) || 'Username must be min 3 characters',
            ],
            email:'',
            emailRules: [
                v => !!v || 'Email is required',
                v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
            ],
            password:'',
            passwordRules: [
                v => !!v || 'Password is required',
                v => (v && v.length >= 8) || 'Password must be min 8 characters',
            ],
        }
    },
    methods:{
        validate(){
            const submitForm = this.$refs.form.validate()
            if (submitForm){
                
                const data = {
                    'name':this.name,
                    'username':this.userName,
                    'email':this.email,
                    'sandi': this.password
                }
                axios.post('https://rafif.pythonanywhere.com/api/rafif/yourjobapp/register',data)
                .then(
                    response => {
                        if( response.data.status == '1'){
                            console.log('Register Berhasil')
                            this.info = 'Register Berhasil'
                            this.colorInfo = '#2FBA39'
                            this.snackbar = true
                            
                        }
                    }
                ).catch(
                    error => {
                        var errStatus = error.response.status
                        if (errStatus == 401){
                            console.log('Register gagal')
                            this.info = 'Register Gagal'
                            this.colorInfo = '#E02E2E'
                            this.snackbar = true
                        }
                        else if(errStatus == 400){
                            console.log('Username atau Email sudah terdaftar')
                            this.info = 'Username atau Email sudah terdaftar'
                            this.colorInfo = '#E02E2E'
                            this.snackbar = true
                        }
                        // else if (error.response.status === 500) {
                        //     console.error('Error 500. Refreshing page...');
                        //     window.location.reload(true);
                        // }
                    }
                )
                // axios.post('https://rafif.pythonanywhere.com/api/rafif/yourjobapp/register',data).then(
                //     response => {
                //         console.log('Register Berhasil')
                //     }
                // )
            }
        },
        correctCloseSnackbar(){
            this.snackbar = false
            this.info = ''
            this.colorInfo = ''
            this.$router.push('/login');
        },
        failCloseSnackbar(){
            this.snackbar = false
            this.info = ''
            this.colorInfo = ''
        }
    }
}

</script>

<style scoped>
h1{
    font-size: 300%; 
    color:rgb(87, 75, 75); 
    text-shadow:0px 3px 3px rgb(48, 43, 43);
}
.button-row-container{
    padding-left: 8%;
}
#card-container{
    border-radius: 15px; 
    max-width: 40vw; 
    background-color: rgba(117, 78, 26 ,0.3);
}
@media screen and (max-width:600px) {
    #card-container{
        max-width: 70vw;
    }
    .button-row-container{
        padding-left: 0%;
    }
    h1{
        font-size:200%;
    }
}
</style>