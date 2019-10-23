import Vue from 'vue'
import Router from 'vue-router'
import MedicalServicesChecker from '@/components/MedicalServicesChecker'
import Results from '@/components/Results'

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: 'medical_services_checker',
            component: MedicalServicesChecker
        },
        {
            path: 'results/:data',
            name: 'results',
            component: Results
        },
    ]
})
